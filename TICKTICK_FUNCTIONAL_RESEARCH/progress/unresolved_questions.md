# Unresolved Questions & Runtime Investigation Items

This document tracks items that could not be verified exclusively through static APK analysis and that would benefit from dynamic runtime testing on a physical Android device or emulator.

---

## 1. Runtime Telemetry & Network Observations
1. **WebSocket Reconnection Jitter**:
   * *Status*: Static analysis confirmed WebSocket endpoint `wss://ms.ticktick.com/websocket` and 30-second ping interval.
   * *Runtime Question*: What is the exact client-side jitter and exponential backoff curve when the WebSocket server abruptly terminates connections during poor mobile handoffs?
2. **Dynamic A/B Testing (`pull.ticktick.com/android/config/abtest.json`)**:
   * *Status*: The client fetches remote configuration JSON on startup to toggle experimental feature flags.
   * *Runtime Question*: What active A/B experiments are currently served in production for new users vs. legacy accounts?

---

## 2. Audio & Visual Measurements
1. **Exact Decibel / Volume Multipliers on Ambient Audio**:
   * *Status*: Audio files extracted and documented.
   * *Runtime Question*: Does the app duck media audio from other applications (Spotify/YouTube) while white noise is playing, or mix streams using `AudioAttributes.FLAG_AUDIBILITY_ENFORCED`?
2. **Geofence Dwell Delay**:
   * *Status*: Geofencing client verified.
   * *Runtime Question*: What is the default `setNotificationResponsiveness` value in milliseconds set on the geofence requests to conserve battery?

---

## 3. Cloud AI Backend Latency
1. **AI Conversation Token Stream**:
   * *Status*: API `/api/v1/conversations` confirmed.
   * *Runtime Question*: Does the AI endpoint stream tokens via Server-Sent Events (SSE) or return complete JSON responses?
