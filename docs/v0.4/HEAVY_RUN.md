# Running the v0.4 experiment on the laptop

Machine this was written for: **ASUS ROG Strix SCAR 18 (G835LX)**, Intel Core Ultra 9 275HX (8 performance
and 16 efficiency cores, 24 threads), 64 GB RAM, NVIDIA RTX 5090 Laptop GPU (not used), Windows 11 Pro.
Found with `Get-CimInstance Win32_ComputerSystem` and `Get-CimInstance Win32_Processor`.

The run loads all 24 threads for many hours (the expected time of every phase is in
`paper_artifacts_v2/pilot/PILOT.md`). Nothing in this file is done by the scripts: every setting below is
changed by you, and section "Restore" puts it back. The quality results do not depend on the speed of the
machine (the budget is counted in decoder calls); only the timing phase does.

## 1. Note the current settings (so they can be restored)

In PowerShell (normal user rights are enough):

```
powercfg /getactivescheme
powercfg /q SCHEME_CURRENT SUB_SLEEP > $env:USERPROFILE\Desktop\power-before.txt
powercfg /q SCHEME_CURRENT SUB_VIDEO >> $env:USERPROFILE\Desktop\power-before.txt
powercfg /q SCHEME_CURRENT SUB_BUTTONS >> $env:USERPROFILE\Desktop\power-before.txt
```

Also write down the Windows power mode (Settings → System → Power & battery → Power mode; in Russian
"Параметры → Система → Питание и батарея → Режим питания") and the Armoury Crate operating mode.

## 2. Power: no sleep, no hibernation, best performance

1. Plug in the laptop's own charger. On battery the processor slows down and the
   laptop may go to sleep.
2. Sleep and hibernation on AC off (screen may still switch off; that does not slow the run):
   ```
   powercfg /change standby-timeout-ac 0
   powercfg /change hibernate-timeout-ac 0
   powercfg /change monitor-timeout-ac 15
   ```
3. Closing the lid does nothing on AC (keep the lid open anyway, for cooling):
   ```
   powercfg /setacvalueindex SCHEME_CURRENT SUB_BUTTONS LIDACTION 0
   powercfg /setactive SCHEME_CURRENT
   ```
4. Windows power mode on AC: "Best performance" ("Максимальная производительность").
5. Armoury Crate → Operating mode: "Performance". "Turbo" is faster and louder; use it only if the laptop
   stands on a hard surface with free vents (step 4).
6. Battery: in Armoury Crate (or MyASUS) set battery charging to the balanced/80 % limit, so that the
   battery does not sit at 100 % and warm for days.

`tpga-exp doctor` checks items 1, 2 and 4.

## 3. Windows Update, Defender, other programs

1. Windows Update: Settings → Windows Update → "Pause updates" for 1 week ("Приостановить обновления").
   A restart for an update in the middle of the run stops it (the run can be resumed, see step 8, but
   the time is lost).
2. Microsoft Defender (optional, needs administrator rights, so you do it): Windows Security → Virus &
   threat protection → Manage settings → Exclusions → Add a folder `C:\dev\tp-ga\paper_artifacts_v2`.
   The run writes many small files there; the exclusion avoids scanning every one. Remove it afterwards.
3. Close the browser, IDEs that index files, Docker, games, and pause OneDrive / cloud sync.
4. Stop the web platform and anything else listening on ports 3000, 8000, 8010 (the other project on
   port 8000 too). Do not start the platform's dev server during the run; the progress is visible in the
   terminal (step 7).

## 4. Cooling

* A hard, flat surface; nothing in front of the side and rear vents; a cooling stand helps.
* Room temperature as low as practical; no direct sun.
* Under full load the processor runs hot and lowers its own clock when it reaches its temperature limit;
  a lower clock only makes the run longer and does not change the results of the quality phases.

## 5. Check

```
cd C:\dev\tp-ga
.venv\Scripts\activate
tpga-exp doctor --config experiments/paper-v2.yaml
```

doctor only reads; every "ВНИМАНИЕ" line says what to change. Run it again after the changes.

## 6. Start

In Windows Terminal (not inside an IDE, so that closing the IDE does not stop the run):

```
cd C:\dev\tp-ga
.venv\Scripts\activate
tpga-exp run --config experiments/paper-v2.yaml
```

The phases run in this order: reference, main, stagnation, legacy, factorial, timing. A single phase:
`--phase main` (repeatable). `--plain` prints one line per event instead of the live table (for a log file:
`tpga-exp run --config experiments/paper-v2.yaml --plain > run.log`).

## 7. While it runs

* The live table shows the phase, done/total runs, errors, the runs in progress per core and the estimated
  remaining time. The same state is written every few seconds to
  `paper_artifacts_v2/state/monitor.json`; logs go to `paper_artifacts_v2/logs/`.
* Do not run other heavy programs; light use (reading, a text editor) is fine but slows the run a little.
* The timing phase runs on the 8 performance cores only and measures time; during it the laptop should be
  idle.

## 8. Stopping and resuming

* **Ctrl+C once**: no new runs start; the runs in progress finish and are saved; then the program exits.
* **Ctrl+C twice**: the runs in progress are abandoned (they are not saved and will be repeated).
* **Resume**: the same command again. Finished runs are on disk and are skipped; the rest continue.
  After a power loss or a forced restart the same applies: at most the runs that were in progress are lost.
* Do not change `experiments/paper-v2.yaml`, `experiments/tuned-v2.yaml` or the Python packages between a
  stop and a resume (doctor compares the package versions with the run manifest).

## 9. After the run

```
tpga-exp report --config experiments/paper-v2.yaml
```

Tables go to `paper_artifacts_v2/tables`, figures to `paper_artifacts_v2/figures`.

## 10. Restore

1. Sleep, hibernation and screen timeouts: the values from `power-before.txt` (in minutes), for example
   `powercfg /change standby-timeout-ac 30`, `powercfg /change hibernate-timeout-ac 180`,
   `powercfg /change monitor-timeout-ac 10`.
2. Lid action on AC back to sleep: `powercfg /setacvalueindex SCHEME_CURRENT SUB_BUTTONS LIDACTION 1`
   and `powercfg /setactive SCHEME_CURRENT` (1 = sleep; use the value from `power-before.txt`).
3. Windows power mode and Armoury Crate mode back to what you noted.
4. Windows Update: "Resume updates".
5. Defender: remove the folder exclusion.
6. Battery charge limit: as you prefer.
