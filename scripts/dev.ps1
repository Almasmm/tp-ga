# Start the tp-ga platform locally: FastAPI and Next.js, both on the loopback interface only.
#
#   powershell -ExecutionPolicy Bypass -File scripts/dev.ps1                  # API :8000, UI :3000 (production build)
#   powershell -ExecutionPolicy Bypass -File scripts/dev.ps1 -ApiPort 8010    # another API port
#   powershell -ExecutionPolicy Bypass -File scripts/dev.ps1 -Dev             # Next.js dev server
#   powershell -ExecutionPolicy Bypass -File scripts/dev.ps1 -Stop            # stop the servers this script started
#
# The script stops only the processes it started itself (recorded in platform/data/logs/servers.json);
# if a port is taken by another program it reports that and exits. Logs: platform/data/logs/.
param([switch]$Dev, [switch]$Stop, [switch]$NoBuild, [int]$ApiPort = 8000, [int]$WebPort = 3000)

$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $PSScriptRoot
$python = Join-Path $root ".venv\Scripts\python.exe"
$logs = Join-Path $root "platform\data\logs"
$pidFile = Join-Path $logs "servers.json"
$web = Join-Path $root "platform\web"
New-Item -ItemType Directory -Force $logs | Out-Null

function Stop-OwnServers {
    if (-not (Test-Path $pidFile)) { return }
    $ids = Get-Content $pidFile | ConvertFrom-Json
    foreach ($id in @($ids.api, $ids.web)) {
        if (-not $id) { continue }
        # stop the recorded process with its whole tree (npm -> cmd -> node -> next)
        & taskkill.exe /PID $id /T /F 2>&1 | Out-Null
    }
    Remove-Item $pidFile
}

function Test-PortFree([int]$port) {
    $listener = [System.Net.Sockets.TcpListener]::new([System.Net.IPAddress]::Loopback, $port)
    try { $listener.Start(); return $true } catch { return $false } finally { $listener.Stop() }
}

if ($Stop) { Stop-OwnServers; Write-Host "Servers stopped."; exit 0 }
if (-not (Test-Path $python)) {
    throw "Missing .venv. Run: python -m venv .venv; .venv\Scripts\pip install -e "".[dev]"" -r platform\backend\requirements.txt"
}
Stop-OwnServers
Start-Sleep -Milliseconds 500
foreach ($port in $ApiPort, $WebPort) {
    if (-not (Test-PortFree $port)) {
        throw "Port $port on 127.0.0.1 is used by another program. Choose another one, e.g. -ApiPort 8010 or -WebPort 3001."
    }
}

$api = Start-Process -FilePath $python -PassThru -WindowStyle Hidden `
    -WorkingDirectory (Join-Path $root "platform\backend") `
    -ArgumentList "-m", "uvicorn", "app.main:app", "--host", "127.0.0.1", "--port", "$ApiPort" `
    -RedirectStandardOutput (Join-Path $logs "api.out.log") -RedirectStandardError (Join-Path $logs "api.err.log")

# next.config.mjs reads these when the server starts (and bakes the API address into a build)
$env:TPGA_API_ORIGIN = "http://127.0.0.1:$ApiPort"
$env:TPGA_CORS_ORIGINS = "http://127.0.0.1:$WebPort,http://localhost:$WebPort"
if (-not (Test-Path (Join-Path $web "node_modules"))) { npm --prefix $web ci | Out-Host }
if ($Dev) {
    $npmArgs = "run", "dev", "--", "--hostname", "127.0.0.1", "--port", "$WebPort"
} else {
    if (-not $NoBuild) { npm --prefix $web run build | Out-Host }
    $npmArgs = "run", "start", "--", "--hostname", "127.0.0.1", "--port", "$WebPort"
}
$ui = Start-Process -FilePath "npm.cmd" -PassThru -WindowStyle Hidden -WorkingDirectory $web -ArgumentList $npmArgs `
    -RedirectStandardOutput (Join-Path $logs "web.out.log") -RedirectStandardError (Join-Path $logs "web.err.log")
@{ api = $api.Id; web = $ui.Id; api_port = $ApiPort; web_port = $WebPort } | ConvertTo-Json | Set-Content $pidFile

$ok = $false
for ($i = 0; $i -lt 60; $i++) {
    try {
        $health = Invoke-RestMethod -Uri "http://127.0.0.1:$ApiPort/health" -TimeoutSec 2
        if ($health.status -eq "ok") { $ok = $true; break }
    } catch { Start-Sleep -Milliseconds 500 }
}
if (-not $ok) { throw "API did not answer /health; see $logs\api.err.log" }
Write-Host "API       http://127.0.0.1:$ApiPort  (/health ok, OpenAPI: /docs)"

$ok = $false
for ($i = 0; $i -lt 120; $i++) {
    try { Invoke-WebRequest -Uri "http://127.0.0.1:$WebPort" -UseBasicParsing -TimeoutSec 2 | Out-Null; $ok = $true; break }
    catch { Start-Sleep -Milliseconds 500 }
}
if (-not $ok) { throw "UI did not start; see $logs\web.err.log" }
Write-Host "Interface http://127.0.0.1:$WebPort"
Write-Host "Stop with: powershell -ExecutionPolicy Bypass -File scripts/dev.ps1 -Stop"
