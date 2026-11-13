# Feature Specification: F001 - Task Creation

## 1. Feature Identification
* **Feature ID**: `F001`
* **Feature Name**: Task Creation (Quick Add & Full Detail)
* **Domain**: Task Management
* **Evidence Standard**: `[CODE-CONFIRMED]` via REA JADX / `Task2Dao` / `QuickAddBottomSheet`

---

## 2. Functional Description
Allows the user to create new actionable tasks via a single-tap Quick Add modal or an expanded Task Detail form. Supports real-time NLP token parsing, priority assignment, due date/time scheduling, project list allocation, tag labeling, subtask checklist embedding, and multimedia attachments.

---

## 3. Entry Points & User Invocations
1. Floating Action Button (+) on `TaskListFragment`.
2. Notification shade Quick Add tile / Ongoing notification action.
3. System text selection context menu (`ACTION_PROCESS_TEXT` via `ProcessTextActivity`).
4. Android Home Screen App Shortcut (`shortcut_add_task`).
5. Deep Link URI: `ticktick://task/add?title=...`.

---

## 4. Input Fields & Validation Rules
| Field | Type | Required | Default Value | Validation & Boundary Rules |
| :--- | :--- | :--- | :--- | :--- |
| `title` | Text / String | Yes | `""` | Maximum 1,024 characters. Whitespace trimmed. |
| `content` | Text / Markdown | No | `""` | Maximum 32,768 characters. Supports GFM Markdown. |
| `dueDate` | DateTime | No | `null` (or Today if pref enabled) | ISO-8601 UTC timestamp. |
| `priority` | Integer | No | `0` (None) | Enum: `0` = None, `1` = Low, `3` = Medium, `5` = High. |
| `projectId` | String (UUID) | Yes | `"inbox"` | Must exist in `PROJECT` table. |
| `tags` | Array of Strings | No | `[]` | Each tag alphanumeric + underscore; max 32 chars. |
| `allDay` | Boolean | No | `true` (if no time specified) | `1` if all-day event; `0` if specific time block. |

---

## 5. Screen Components & Controls
* **Input Field**: Auto-expanding `EditText` with `imeOptions="actionDone"`.
* **NLP Pill Container**: Horizontal flexbox rendering parsed date, priority, list, and tag pills.
* **Toolbar Controls**:
  * Date Picker button (Calendar icon).
  * Priority button (Flag icon).
  * Project Picker chip (List title with color dot).
  * Tag Picker button (# icon).
  * Voice Input button (Mic icon).
  * Save / Submit button (Checkmark / Paper airplane icon).

---

## 6. Micro-Interactions & State Transitions
1. Tapping FAB summons `QuickAddBottomSheet` from bottom of screen with 250ms slide-up animation.
2. Soft keyboard opens automatically with cursor focused in Title field.
3. As characters are typed, tokenizer detects keywords and creates dynamic interactive chip spans.
4. Tapping a chip span opens its corresponding selector dialog (e.g. tapping "Tomorrow 3pm" chip opens Date/Time picker).
5. Pressing keyboard "Done" or tapping Submit:
   * Triggers short click haptic feedback.
   * Inserts row into SQLite `Tasks2`.
   * Enqueues dirty row in `Tasks2_SYNCED_JSON`.
   * Clears text input and remains open if continuous add mode is active, or dismisses sheet.

---

## 7. Data Persistence & Database Mutations
```sql
INSERT INTO TASKS2 (
    SID, TITLE, CONTENT, DUE_DATE, PRIORITY, PROJECT_ID, 
    STATUS, ALL_DAY, CREATED_TIME, MODIFIED_TIME, PIN, SORT_ORDER
) VALUES (
    'd3b07384-d113-4e44-8822-123456789abc',
    'Submit Financial Audit Report',
    'Ensure Q3 numbers reconcile with bank statement',
    1715011200000,
    5,
    'proj_work_uuid',
    0,
    0,
    1714980000000,
    1714980000000,
    0,
    1000
);

INSERT INTO TASKS2_SYNCED_JSON (
    SID, JSON_CONTENT, CHANGE_TYPE, SYNC_STATUS, TIMESTAMP
) VALUES (
    'd3b07384-d113-4e44-8822-123456789abc',
    '{"title":"Submit Financial Audit Report",...}',
    1,
    1,
    1714980000000
);
```

---

## 8. Background & Notification Processing
* If `dueDate` contains an explicit reminder offset:
  * Inserts reminder row into `TASK_REMINDER`.
  * Computes `triggerTime = dueDate - reminderOffset`.
  * Invokes `AlarmManager.setExactAndAllowWhileIdle(RTC_WAKEUP, triggerTime, pendingIntent)`.

---

## 9. Error States & Edge Cases
* **Empty Title**: Tapping save with empty title shakes input box and displays toast: *"Please enter a task name"*.
* **Database Full / Disk Error**: Displays `Snackbar` with error message; caches in-memory draft so input is never lost.
* **Network Offline**: Task is saved locally without network delay; sync status remains pending until network restores.

---

## 10. Verification & Test Criteria
1. Verify Quick Add opens with soft keyboard in < 150ms.
2. Verify typing "Buy Milk tomorrow at 5pm !high #groceries" produces parsed date (Tomorrow 17:00), priority (High), and tag (`groceries`).
3. Verify newly created task appears immediately at the top of the Task List.
4. Verify alarm fires accurately at scheduled due date/time even if device is in Doze mode.
