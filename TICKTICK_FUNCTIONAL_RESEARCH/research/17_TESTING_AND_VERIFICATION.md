# Testing and Verification Strategy

## 1. Quality Assurance Philosophy

To ensure that an independent open-source recreation achieves production-grade stability, reliability, and precision equal to TickTick, the application must be verified against rigorous test suites. This document specifies the comprehensive testing strategy, automated test matrices, and verification protocols.

---

## 2. Core Unit Test Matrices

### 2.1 Recurrence Engine Test Matrix
The recurrence calculator must be verified against deterministic temporal boundary cases:

| Test Case ID | Initial Due Date | Recurrence Rule (`RRULE`) | `repeatFrom` | Completion Date | Expected Next Due Date | Rationale |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `TC-REC-01` | `2026-05-01` | `FREQ=DAILY;INTERVAL=1` | `0` (Due) | `2026-05-01` | `2026-05-02` | Standard consecutive daily repeat. |
| `TC-REC-02` | `2026-05-01` | `FREQ=DAILY;INTERVAL=1` | `0` (Due) | `2026-05-10` (Overdue)| `2026-05-02` | Repeat from due date preserves original schedule regardless of late completion. |
| `TC-REC-03` | `2026-05-01` | `FREQ=DAILY;INTERVAL=1` | `1` (Done) | `2026-05-10` (Overdue)| `2026-05-11` | Repeat from completion date shifts next occurrence relative to execution date. |
| `TC-REC-04` | `2024-02-29` | `FREQ=YEARLY;INTERVAL=1` | `0` (Due) | `2024-02-29` | `2025-02-28` | Leap day yearly repeat clamps to Feb 28 in non-leap year. |
| `TC-REC-05` | `2026-01-31` | `FREQ=MONTHLY;INTERVAL=1`| `0` (Due) | `2026-01-31` | `2026-02-28` | 31st monthly repeat clamps to last day of February. |
| `TC-REC-06` | `2026-05-01` | `FREQ=WEEKLY;BYDAY=MO,WE,FR`| `0` (Due) | `2026-05-01` (Fri) | `2026-05-04` (Mon) | Advances to next specified weekday in chain. |

---

### 2.2 Natural Language Processing (NLP) Test Matrix
The local tokenizer must parse temporal phrases, priorities, and organizational tokens accurately:

| Test Case ID | Raw Input String | Parsed Title Output | Extracted Due Date / Time | Priority | Tags / Lists |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `TC-NLP-01` | `"Meeting with team tomorrow at 3pm"` | `"Meeting with team"` | Tomorrow at 15:00:00 | None (`0`) | None |
| `TC-NLP-02` | `"Pay rent on May 1st !1 #finance"` | `"Pay rent"` | Next May 1st, 09:00:00 | High (`5`) | Tag: `finance` |
| `TC-NLP-03` | `"Doctor visit next monday 10:30am ~Health"`| `"Doctor visit"`| Next Monday, 10:30:00 | None (`0`) | List: `Health` |
| `TC-NLP-04` | `"Buy groceries tonight !2"` | `"Buy groceries"` | Today at 20:00:00 | Medium (`3`)| None |
| `TC-NLP-05` | `"Review report in 3 days !low"` | `"Review report"` | `now() + 3 days` | Low (`1`) | None |

---

### 2.3 Habit Streak Calculation Test Matrix
The streak engine must handle diverse weekly schedules and gaps:

| Test Case ID | Scheduled Days | Check-In History (Dates) | Evaluation Date | Expected Streak | Rationale |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `TC-HAB-01` | Daily (All 7 days) | Mon, Tue, Wed, Thu, Fri | Friday | **5 Days** | Perfect daily streak. |
| `TC-HAB-02` | Daily (All 7 days) | Mon, Tue, [Missed Wed], Thu, Fri | Friday | **2 Days** | Missing Wednesday resets streak on Thursday. |
| `TC-HAB-03` | Mon, Wed, Fri only | Mon, Wed, Fri | Friday | **3 Days** | Tue and Thu are not scheduled; streak is unbroken. |
| `TC-HAB-04` | Daily (All 7 days) | Mon, Tue, Wed, Thu | Friday (Not checked in yet) | **4 Days** | If today is in progress, streak preserves yesterday's total until day ends. |

---

## 3. Integration & Database Test Protocols

### 3.1 Local SQLite ACID & Foreign Key Verification
* **Cascade Deletion**:
  1. Insert a `PROJECT` row with `SID = "proj_test"`.
  2. Insert 10 `Tasks2` rows associated with `"proj_test"`.
  3. Delete `"proj_test"`.
  4. Verify all 10 child `Tasks2` rows are either deleted or their `PROJECT_ID` is set to `"inbox"` / `DELETED = 1`.
* **Shadow Queue Integrity**:
  1. Execute batch creation of 50 tasks while simulated offline.
  2. Verify exactly 50 rows exist in `Tasks2_SYNCED_JSON` with `SYNC_STATUS = 1`.
  3. Reconnect network; execute sync.
  4. Verify `Tasks2_SYNCED_JSON` is empty (`count == 0`) and `Tasks2` contains updated `ETAG` values.

---

## 4. Hardware & Platform Verification Protocols

### 4.1 Doze Mode Alarm Verification Protocol
1. Schedule a task reminder for $T+10\text{ minutes}$.
2. Disconnect USB charging; turn off device screen.
3. Force device into deep Doze mode via ADB command:
   `adb shell dumpsys deviceidle force-idle`
4. Wait 10 minutes.
5. **Pass Criteria**: Device screen wakes up, ringtone plays, and heads-up banner is rendered at exact scheduled second.

### 4.2 Accelerometer Flip-to-Focus Protocol
1. Launch Pomodoro screen.
2. Place device flat facedown on desk surface.
3. **Pass Criteria**: Device emits a 100ms haptic confirmation and starts the countdown timer without manual button taps.
4. Pick up phone and face screen up; verify countdown timer is visibly running.
