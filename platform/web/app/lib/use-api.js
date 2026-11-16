"use client";

import { api } from "./api";
import { useAsync } from "./use-async";

/** GET a resource; returns { data, status: loading|ok|error|empty, error, reload }. */
export function useApi(path, { isEmpty } = {}) {
  return useAsync(path, () => api(path), isEmpty);
}
