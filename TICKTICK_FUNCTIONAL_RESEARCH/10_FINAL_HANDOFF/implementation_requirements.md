# Implementation Requirements & Technical Standards

## 1. Architectural Constraints for Independent Build

To guarantee production quality and platform independence, any AI agent or engineering team developing the alternative application must adhere to the following technical standards:

1. **Clean-Room Development**: Do not copy decompiled Java/Smali source code or proprietary assets. Recreate behavior based strictly on functional specifications, table schemas, and interaction flows.
2. **Local-First Data Storage**:
   * All queries must hit local SQLite storage with indexes on `(PROJECT_ID, STATUS, DELETED)` and `(DUE_DATE, STATUS)`.
   * UI operations must complete synchronously in under 16ms to maintain 60/120fps refresh rates.
3. **Data Schema Conformance**:
   * Adhere to the entity models defined in [`evidence/code_references/schema.sql`](file:///d:/tick%20tick%20open%20source/TICKTICK_FUNCTIONAL_RESEARCH/evidence/code_references/schema.sql).
4. **RFC 5545 Recurrence Compliance**:
   * Recurrence rules must parse and generate valid iCalendar `RRULE` strings.
5. **Exact Timing & Alarm Precision**:
   * Must utilize platform exact alarm APIs with wake-lock acquisition to guarantee delivery during deep sleep/Doze mode.

---

## 2. Technology Stack Recommendations

| Layer | Recommended Technologies | Rationale |
| :--- | :--- | :--- |
| **Cross-Platform UI** | Flutter, React Native, Rust (Slint/Iced), Kotlin Multiplatform | Provides 60fps native rendering, cross-platform compilation (Android, iOS, Desktop, Web). |
| **Local Database** | SQLite with SQLDelight, Drift, or Room | Zero-latency local reads/writes, transactional ACID guarantees. |
| **State Management** | BLoC, Riverpod, Redux, or Elm Architecture | Deterministic unidirectional data flow with predictable state transitions. |
| **Date & Time Engine** | Joda-Time / Java Time / Chrono (Rust) | Robust handling of time zones, leap years, and RFC-5545 recurrence. |
| **Audio Engine** | Just_audio, OpenAL, or native MediaPlayer | Low-latency seamless looping of ambient white noise audio files. |

---

## 3. Performance & Resource Benchmarks

* **Cold Startup Time**: < 800ms from process launch to interactive task list.
* **Scroll Performance**: Stable 60fps / 120fps with zero frame drops during flings on lists containing 1,000+ items.
* **Database Query Latency**: Under 5ms for standard active list queries (`WHERE STATUS = 0`).
* **Memory Footprint**: Under 120MB resident memory during active background Pomodoro playback.
