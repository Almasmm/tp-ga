// Calls to the local FastAPI back end through the /api rewrite of next.config.mjs.

export class ApiError extends Error {
  constructor(message, status) {
    super(message);
    this.status = status;
  }
}

function detail(data) {
  if (typeof data?.detail === "string") return data.detail;
  if (Array.isArray(data?.detail)) return data.detail.map((d) => d.msg).join("; ");
  return null;
}

export async function api(path, { method = "GET", body, signal } = {}) {
  let response;
  try {
    response = await fetch("/api" + path, {
      method,
      signal,
      headers: body ? { "Content-Type": "application/json" } : undefined,
      body: body ? JSON.stringify(body) : undefined,
    });
  } catch (error) {
    if (error.name === "AbortError") throw error;
    throw new ApiError("offline", 0);
  }
  if (response.status === 204) return null;
  const data = await response.json().catch(() => null);
  if (!response.ok) throw new ApiError(detail(data) ?? `HTTP ${response.status}`, response.status);
  return data;
}

export async function apiText(path) {
  const response = await fetch("/api" + path).catch(() => null);
  if (!response) throw new ApiError("offline", 0);
  if (!response.ok) throw new ApiError(`HTTP ${response.status}`, response.status);
  return response.text();
}

/** Subscribe to the SSE stream of a job; returns a function that closes it. */
export function subscribe(jobId, handlers) {
  const source = new EventSource(`/api/jobs/${jobId}/events`);
  for (const type of ["started", "method_started", "progress", "method_done", "done", "error", "cancelled"]) {
    source.addEventListener(type, (event) => {
      const data = JSON.parse(event.data);
      handlers[type]?.(data);
      if (type === "done" || type === "error" || type === "cancelled") source.close();
    });
  }
  source.onerror = () => {
    if (source.readyState === EventSource.CLOSED) handlers.closed?.();
  };
  return () => source.close();
}

export function downloadBlob(name, content, type) {
  const url = URL.createObjectURL(new Blob([content], { type }));
  const a = document.createElement("a");
  a.href = url;
  a.download = name;
  document.body.appendChild(a);
  a.click();
  a.remove();
  setTimeout(() => URL.revokeObjectURL(url), 1000);
}
