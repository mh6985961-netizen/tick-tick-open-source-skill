# Premium Features and Restrictions

## 1. Subscription Architecture & Gating Model

TickTick operates a **Freemium** business model. The application codebase (`com.ticktick.task`) enforces feature limits through centralized user entitlement checks, primarily evaluated via `UserProfile.isPro()`, `isProUser()`, and feature-specific capability flags.

When an unentitled user attempts to access a restricted capability, the application intercepts the action and displays `GetProActivity` or `ProFeaturesActivity`.

```mermaid
flowchart TD
    UserAction[User triggers feature e.g. Add 2nd Reminder / Open Week Calendar] --> CheckPro{UserProfile.isPro() == true?}
    
    CheckPro -- Yes --> ExecuteFeature[Execute Feature Immediately]
    
    CheckPro -- No --> CheckLimit{Within Free Tier Quota?}
    CheckLimit -- Yes --> ExecuteFeature
    CheckLimit -- No --> Intercept[Show Upgrade Prompt: GetProActivity]
    
    Intercept --> UserChoice{User Action}
    UserChoice -- Subscribe --> GooglePlay[Google Play Billing Flow]
    GooglePlay --> ReceiptVerify[Verify Receipt: /api/v2/subscribe/verify/google]
    ReceiptVerify --> Unlock[Set isPro = true & Refresh UI]
    UserChoice -- Dismiss --> AbortAction[Cancel Operation & Retain Free State]
```

---

## 2. Quantitative Free vs. Pro Tier Comparison Matrix

The following table summarizes the verified functional restrictions and quantitative caps between Free and Pro tiers discovered in the decompiled bytecode and resource strings:

| Feature Dimension | Free Tier Limitation | Premium / Pro Entitlement | Evidence Source |
| :--- | :--- | :--- | :--- |
| **User Lists (Projects)** | Maximum 9 active lists | Up to 299 active lists | `[CODE-CONFIRMED]` `ProjectLimitHelper` |
| **Tasks per List** | Maximum 99 tasks per list | Up to 999 tasks per list | `[CODE-CONFIRMED]` `TaskCountValidator` |
| **Checklist Items / Subtasks**| Maximum 19 checklist items | Up to 199 checklist items per task | `[CODE-CONFIRMED]` `CheckListLimitHelper` |
| **Reminders per Task** | **1 Reminder** per task | Up to **5 Reminders** per task | `[CODE-CONFIRMED]` `ReminderLimitHelper` |
| **Subtask Alarms** | Not supported (parent alarm only)| **Individual Reminders** on subtasks | `[CODE-CONFIRMED]` `ChecklistItemReminder` |
| **Habit Tracking** | Maximum 5 active habits | **Unlimited** active habits | `[CODE-CONFIRMED]` `HabitCountLimit` |
| **Calendar Multi-Views** | Agenda view only / Limited Day view | **Full Multi-View**: Month, Week, Day, 3-Day, Agenda | `[CODE-CONFIRMED]` `CalendarViewActivity` |
| **External Calendar Sync** | Read-only basic integration | **Two-Way Sync** + URL `.ics` WebCal Subscriptions | `[CODE-CONFIRMED]` `CalendarManagerActivity` |
| **Eisenhower Matrix** | 1 default profile with fixed rules | **Custom Profiles** + Custom Quadrant Rule Filter Editor | `[CODE-CONFIRMED]` `MatrixConditionEditActivity` |
| **Annoying Alert** | Not supported | **Supported**: Continuous repeating persistent alarms | `[CODE-CONFIRMED]` `preference_annoying_alert.xml` |
| **Ambient Focus Sounds** | 3 basic white noise sounds | **Full Sound Library** (15+ ambient tracks) | `[CODE-CONFIRMED]` `ChoosePomoSoundActivity` |
| **Custom Smart Lists** | Pre-set smart lists only (Today, 7 Days) | **Custom Filter Engine** (Multi-condition Boolean rules) | `[CODE-CONFIRMED]` `SmartListRuleEditActivity` |
| **Task Activity History** | Not available | **Full Revision Log** of task edits and collaborator actions | `[CODE-CONFIRMED]` `TaskActivitiesWebViewActivity` |
| **Attachment Uploads** | 1 attachment/task, max 10MB/day | Up to 99 attachments/task, max 50MB/day | `[CODE-CONFIRMED]` `handleAttachmentAddCountLimit` |
| **Appearance & Themes** | Basic primary color presets | **Full Theme Store**, City Themes, Custom Hex Color Picker | `[CODE-CONFIRMED]` `CustomThemeActivity` |
| **Course Timetable** | 1 basic timetable | Multiple schedules, campus import, odd/even week cycles | `[CODE-CONFIRMED]` `CourseDetailActivity` |

---

## 3. Pro Code Evaluation & Interception Architecture

### 3.1 Entitlement Check Pattern
In decompiled bytecode, feature gates consistently query a singleton user configuration cache:

```java
// Typical Pro verification pattern in com.ticktick.task
public boolean canAddReminder(Task task) {
    int reminderCount = task.getReminderCount();
    boolean isPro = UserConfigCache.getInstance().getUserProfile().isPro();
    if (isPro) {
        return reminderCount < 5;
    } else {
        return reminderCount < 1;
    }
}
```

### 3.2 Pro Gating Interceptor (`GetProActivity`)
When an unentitled action is intercepted:
1. An event is logged to analytics (`EventReport: "pro_click_entry", source: "reminder_limit"`).
2. An Intent launches `com.ticktick.task.activity.account.GetProActivity`.
3. The intent passes `EXTRA_SOURCE_FEATURE` (e.g. `FEATURE_CALENDAR`, `FEATURE_MATRIX`, `FEATURE_ATTACHMENT`).
4. `GetProActivity` highlights the specific capability that triggered the paywall, displaying a tailored benefit pitch.

---

## 4. Subscription Lifecycle & Expiration Behavior

### 4.1 Pro Expiration (`ProExpiredActivity6130`)
When a user's subscription expires or fails to renew:
* **Zero Data Destruction**: The application strictly preserves all existing data. If a user created 25 lists and 100 habits while on Pro, none are deleted.
* **Graceful Degradation to Read-Only / Cap**:
  * Existing lists and habits remain fully visible and usable.
  * Creating a *new* list or *new* habit is blocked until the active count drops below the Free threshold (e.g. fewer than 5 habits).
  * Calendar views revert to the default view; attempting to select the Week or Month tab prompts the renewal dialog.
* **Expiration Notice Banner**: A non-intrusive warning card appears at the top of the Settings screen: *"Your Pro subscription has expired. Renew today to maintain full access."*
