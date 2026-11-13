# Complete User Workflows

## 1. Overview

This document specifies the end-to-end user workflows of TickTick, tracing each trigger, user action, internal state transition, data mutations, background operations, and error branches. These workflows serve as the functional blueprint for an independent open-source recreation.

---

## 2. Workflow 1: End-to-End Task Lifecycle

```mermaid
stateDiagram-v2
    [*] --> Draft : Open Quick Add / FAB
    Draft --> Tokenized : Enter title with NLP ("Meeting tomorrow 3pm !1 #work")
    Tokenized --> SavedActive : Tap Save / Enter
    SavedActive --> InProgress : Start Pomodoro / Focus
    InProgress --> SavedActive : Session Completes / Pauses
    SavedActive --> Completed : Check off task / Right Swipe
    SavedActive --> WontDo : Long Swipe / Mark Won't Do
    Completed --> Archived : Archive completed tasks
    Completed --> Trash : Delete task
    SavedActive --> Trash : Delete task
    Trash --> Restored : Restore task within 30 days
    Restored --> SavedActive : Re-enters active list
    Trash --> [*] : Permanent Delete / 30-day Purge
```

### Detailed Execution Steps:
1. **Creation Trigger**: User taps the Floating Action Button (+) or uses the notification shade quick-add tile.
2. **Input Processing**: As text is typed, the local NLP tokenizer extracts dates, times, priority levels (`!1`, `!2`, `!3`), lists (`~ListName`), and tags (`#TagName`).
3. **Local Commit**:
   * Generates a new UUID `SID`.
   * Inserts row into `Tasks2` SQLite table with `STATUS = 0` (Active).
   * Writes initial record into `Tasks2_SYNCED_JSON` with `SYNC_STATUS = 1` (Pending Upload).
4. **Alarm Scheduling**: If a reminder timestamp is present, calls `AlarmManager.setExactAndAllowWhileIdle()` to schedule the notification via `ReminderReceiver`.
5. **Completion Transition**:
   * Tapping the checkbox triggers the completion animation.
   * `STATUS` updates to `2` (Completed); `COMPLETED_TIME` is set to current epoch milliseconds.
   * If part of a shared list, dispatches an activity notification to list collaborators.
6. **Undo Grace Period**: A bottom `Snackbar` appears for 3.5 seconds. Tapping "Undo" reverts `STATUS` to `0` and cancels deletion/completion flags.

---

## 3. Workflow 2: Recurring Task Recurrence Engine

```mermaid
sequenceDiagram
    participant User
    participant TaskEngine as Recurrence Engine
    participant DB as SQLite / GreenDAO
    participant AlarmMgr as AlarmManager

    User->>TaskEngine: Complete recurring task (Due: Today, RRULE: FREQ=DAILY)
    TaskEngine->>DB: Read task repeatFlag & repeatFrom
    alt Repeat from Due Date (repeatFrom == "0")
        TaskEngine->>TaskEngine: Calculate Next Due Date = Old Due Date + Interval
    else Repeat from Completion Date (repeatFrom == "1")
        TaskEngine->>TaskEngine: Calculate Next Due Date = Current Timestamp + Interval
    end
    
    alt Single Task Entity Re-use (TickTick default)
        TaskEngine->>DB: Record completed date in EX_DATE / History log
        TaskEngine->>DB: UPDATE Tasks2 SET DUE_DATE = nextDueDate, STATUS = 0
        TaskEngine->>AlarmMgr: Reschedule Alarm for nextDueDate
    else Spawn Next Occurrence
        TaskEngine->>DB: UPDATE current task SET STATUS = 2 (Completed)
        TaskEngine->>DB: INSERT INTO Tasks2 new task with nextDueDate
    end
    TaskEngine-->>User: Refresh UI to show task scheduled for next occurrence
```

### Edge Cases in Recurrence:
* **Skipping an Occurrence**: User selects "Skip this occurrence". The engine appends the skipped date to the task's `EX_DATE` string in ISO-8601 format and advances `DUE_DATE` without modifying task completion counters.
* **Editing a Recurring Task**: When modifying due date, priority, or title, a dialog prompts:
  1. *This occurrence only*: Clones current task, appends current date to parent's `EX_DATE`, and applies edits to the cloned standalone instance.
  2. *All future occurrences*: Updates the parent recurring task definition; updates `RRULE` starting from current date.
* **Chinese Lunar Calendar Recurrence**: For birthdays and lunar holidays, the engine maps Gregorian dates to the Chinese Lunar Calendar table, advancing recurrence based on lunar month and leap month cycles (`REPEAT_FLAG = "LUNAR"`).

---

## 4. Workflow 3: Habit Tracking & Streak Management

```mermaid
flowchart TD
    A[Open Habits Tab] --> B{Active Habits Exist?}
    B -- No --> C[Display Empty State & Habit Presets]
    C --> D[Select Preset e.g. Drink Water or Create Custom]
    D --> E[Configure Frequency, Daily Target & Reminders]
    E --> F[Save Habit to HABIT Table]
    
    B -- Yes --> G[Render Habit Matrix / Cards]
    G --> H[User Taps Check-in Circle]
    H --> I[Execute Animated Ring Fill & Flame Particle]
    I --> J[Insert/Update HABIT_RECORD & HABIT_CHECK_IN]
    J --> K[Recalculate Current Streak & Longest Streak]
    
    K --> L{Missed Yesterday?}
    L -- Yes --> M{Retroactive Check-in Allowed?}
    M -- Yes --> N[User opens Habit Calendar & logs missed day]
    N --> O[Streak Repaired & Recalculated]
    M -- No --> P[Current Streak resets to 1]
```

### Streak Computation Rules:
* **Daily Frequency**: Streak increments if a valid `HABIT_CHECK_IN` exists for consecutive days $T$ and $T-1$.
* **Specific Days of Week (e.g. Mon, Wed, Fri)**: The streak counter does not break on unselected days (Tue, Thu, Sat, Sun). The chain is evaluated strictly against scheduled active days.
* **Target Metric Habits**: For quantitative habits (e.g. 2000 ml water), partial check-ins record entries in `HABIT_CHECK_IN`. The habit is marked achieved for the day only when $\sum \text{value} \ge \text{targetValue}$.

---

## 5. Workflow 4: Focus & Pomodoro Cycle

```mermaid
sequenceDiagram
    participant User
    participant PomoUI as PomodoroActivity
    participant SoundSvc as AmbientSoundService
    participant Sensor as Accelerometer
    participant DB as GreenDAO (Pomodoro)

    User->>PomoUI: Select Task & Set Duration (e.g. 25 min)
    alt Manual Start
        User->>PomoUI: Tap "Start" Button
    else Flip to Focus
        User->>Sensor: Place phone facedown
        Sensor-->>PomoUI: Trigger SensorEvent (Z ~= -9.8 m/s²)
    end
    
    PomoUI->>SoundSvc: Play looping White Noise (e.g. Rain)
    PomoUI->>PomoUI: Start Foreground Countdown Timer
    
    alt User Switches App during Strict Mode
        PomoUI->>PomoUI: Intercept app change & show overlay alert
        PomoUI->>PomoUI: Increment interruption count
    end
    
    PomoUI->>PomoUI: Timer Reaches 00:00
    PomoUI->>SoundSvc: Stop Ambient Audio & Play Completion Chime
    PomoUI->>DB: INSERT INTO Pomodoro (START_TIME, END_TIME, DURATION, TASK_ID, STATUS=FINISHED)
    PomoUI->>User: Display PomoPopupActivity ("Focus Complete! Start 5 min Break?")
```

---

## 6. Workflow 5: Calendar Drag-to-Schedule

```mermaid
sequenceDiagram
    participant User
    participant CalView as CalendarViewActivity
    participant Tray as Unscheduled Tasks Drawer
    participant Grid as 24-Hour Timeline Grid
    participant DB as SQLite Tasks2

    User->>CalView: Open Calendar (Day or Week View)
    CalView->>Tray: Query tasks WHERE DUE_DATE IS NULL OR ALL_DAY = 1
    User->>Tray: Tap & Hold task chip
    Tray-->>User: Lift card (Elevation 6dp, slight rotation)
    User->>Grid: Drag chip onto 14:00 time slot
    Grid-->>User: Highlight snap block (14:00 - 14:30)
    User->>Grid: Release drag
    Grid->>DB: UPDATE Tasks2 SET START_TIME = 14:00, DUE_DATE = 14:30, ALL_DAY = 0
    Grid-->>User: Animate card snapping into calendar timeline
    User->>Grid: Drag bottom resize handle downwards to 15:30
    Grid->>DB: UPDATE Tasks2 SET DUE_DATE = 15:30 (Duration = 90 min)
```

---

## 7. Workflow 6: Shared List Collaboration

```mermaid
sequenceDiagram
    participant Owner as List Owner
    participant Server as TickTick Cloud API
    participant Member as Collaborator
    participant DB as Local Database

    Owner->>Server: POST /api/v2/project/{id}/share (Generate Invite Link / QR)
    Server-->>Owner: Return invite link ("ticktick.com/invite/...")
    Owner->>Member: Send invite link via messaging app
    Member->>Server: POST /api/v2/project/join (Accept Invite)
    Server->>Server: Add Member to PROJECT_MEMBER (ROLE = MEMBER)
    Server-->>Member: Return Project data & tasks
    Member->>DB: Sync shared project & tasks locally
    
    Member->>DB: Assign Task to Owner & Post Comment
    Member->>Server: POST /api/v2/batch (Task update + Comment)
    Server->>Owner: Push WebSocket Notification ("Member assigned you a task")
    Owner->>DB: Auto-sync update & render badge on Notification Center
```

---

## 8. Workflow 7: Offline-to-Online Synchronization & Conflict Resolution

```mermaid
sequenceDiagram
    participant Client as TickTick Client (Offline)
    participant LocalDB as SQLite (GreenDAO)
    participant SyncMgr as SyncManager
    participant Server as TickTick REST API

    Note over Client: User edits task while disconnected
    Client->>LocalDB: UPDATE Tasks2 SET TITLE = "Updated Offline", ETAG = oldEtag
    Client->>LocalDB: INSERT INTO Tasks2_SYNCED_JSON (CHANGE_TYPE = UPDATE, SYNC_STATUS = 1)
    
    Note over Client: Device regains Internet connectivity
    SyncMgr->>SyncMgr: NetworkCallback.onAvailable() fired
    SyncMgr->>LocalDB: Query all rows WHERE SYNC_STATUS = 1
    SyncMgr->>Server: POST /api/v2/batch/check (Upload dirty entities + Checkpoint ID)
    
    alt No Conflict (Server ETag matches client oldEtag)
        Server->>Server: Apply update to master database
        Server-->>SyncMgr: 200 OK (New Checkpoint ID, New ETag)
        SyncMgr->>LocalDB: UPDATE Tasks2 SET ETAG = newEtag; DELETE FROM Tasks2_SYNCED_JSON
    else Conflict Detected (Server ETag modified by another client)
        Server-->>SyncMgr: 409 Conflict / Return Server Version
        alt Last-Write-Wins (LWW) Strategy
            SyncMgr->>SyncMgr: Compare client updateTime vs server updateTime
            SyncMgr->>LocalDB: Overwrite with latest timestamp version
        else Three-Way Merge (for Checklists / Notes)
            SyncMgr->>SyncMgr: Merge checklist items by item SID
            SyncMgr->>LocalDB: Save merged state & upload reconciled record
        end
    end
```
