"use client";

import { useEffect, useState } from "react";

/** Step through 0..total with play/pause at `speed` steps per second; a new `resetKey` restarts. */
export function useStepper(total, resetKey) {
  const [k, setK] = useState(0);
  const [playingRaw, setPlaying] = useState(false);
  const [speed, setSpeed] = useState(2);
  const [key, setKey] = useState(resetKey);
  if (key !== resetKey) {
    // derived reset during render (React's recommended alternative to an effect)
    setKey(resetKey);
    setK(0);
    setPlaying(false);
  }
  const playing = playingRaw && k < total;
  useEffect(() => {
    if (!playing) return undefined;
    const id = setTimeout(() => setK((v) => Math.min(total, v + 1)), 1000 / speed);
    return () => clearTimeout(id);
  }, [playing, k, total, speed]);
  return {
    k: Math.min(k, total),
    setK,
    playing,
    speed,
    setSpeed,
    toggle: () => {
      if (k >= total) setK(0);
      setPlaying(!playing);
    },
    next: () => setK((v) => Math.min(total, v + 1)),
    prev: () => setK((v) => Math.max(0, v - 1)),
    reset: () => {
      setPlaying(false);
      setK(0);
    },
  };
}
