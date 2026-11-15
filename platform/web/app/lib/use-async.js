"use client";

import { useCallback, useEffect, useEffectEvent, useState } from "react";

/**
 * Run `loader` whenever `key` changes (null: do nothing). The state of the last finished load is
 * stored with its key, so "loading" is derived during render instead of being set in an effect.
 * Returns { data, status: idle|loading|ok|empty|error, error, reload }.
 */
export function useAsync(key, loader, isEmpty) {
  const [state, setState] = useState({ key: null });
  const [tick, setTick] = useState(0);
  const full = key == null ? null : `${key}#${tick}`;
  const load = useEffectEvent(() => loader());
  const empty = useEffectEvent((data) => Boolean(isEmpty?.(data)));
  useEffect(() => {
    if (full == null) return undefined;
    let alive = true;
    load().then(
      (data) => alive && setState({ key: full, status: empty(data) ? "empty" : "ok", data, error: null }),
      (error) => alive && error?.name !== "AbortError" && setState({ key: full, status: "error", data: null, error }),
    );
    return () => {
      alive = false;
    };
  }, [full]);
  const reload = useCallback(() => setTick((v) => v + 1), []);
  if (full == null) return { data: null, status: "idle", error: null, reload };
  if (state.key !== full) return { data: state.data ?? null, status: "loading", error: null, reload };
  return { data: state.data, status: state.status, error: state.error, reload };
}
