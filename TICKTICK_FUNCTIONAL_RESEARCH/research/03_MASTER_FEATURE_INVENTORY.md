# TickTick Master Feature Inventory

**Project**: TickTick Functional Research  
**Document**: `research/03_MASTER_FEATURE_INVENTORY.md`  
**Evidence Standard**: [CODE-CONFIRMED], [RESOURCE-CONFIRMED], and [INFERRED]  
**Verification Standard**: VERIFIED, CODE_CONFIRMED, PARTIALLY_VERIFIED  

---

## 1. Domain A: Task Management (F001 – F035)

| ID | Feature Name | Classification / Description | Evidence Status | Verification |
| :--- | :--- | :--- | :--- | :--- |
| **F001** | Create Task | Quick and full task creation with title, description, and list assignment. | [CODE-CONFIRMED] | `CODE_CONFIRMED` |
| **F002** | Edit Task Title & Notes | Markdown-enabled rich description, URL detection, and title modification. | [CODE-CONFIRMED] | `CODE_CONFIRMED` |
| **F003** | Task Priority Levels | 4-level priority system: None (0), Low (1, Blue), Medium (3, Orange), High (5, Red). | [RESOURCE-CONFIRMED] | `VERIFIED` |
| **F004** | Complete Task | Toggle completion state; records `completedTime` and `completedUserId`. | [CODE-CONFIRMED] | `CODE_CONFIRMED` |
| **F005** | Reopen Task | Reopen completed task; clears completed timestamp, restores active status. | [CODE-CONFIRMED] | `CODE_CONFIRMED` |
| **F006** | "Won't Do" / Abandon Task | Mark task abandoned without deleting or completing (`task_wont_do`). | [RESOURCE-CONFIRMED] | `VERIFIED` |
| **F007** | Delete Task & Trash Bin | Soft-delete to Trash bin with 30-day restore capability before permanent purge. | [CODE-CONFIRMED] | `CODE_CONFIRMED` |
| **F008** | Task Duplication | Clone task deeply including checklist items, tags, and recurrence settings. | [CODE-CONFIRMED] | `CODE_CONFIRMED` |
| **F009** | Pin Task to Top | Pin important tasks to the top of list; records `pinnedTime` and `local_unpinned`. | [CODE-CONFIRMED] | `CODE_CONFIRMED` |
| **F010** | Flat Checklist Subtasks | Embedded checklist items (`checklist_item`) within a task body. | [CODE-CONFIRMED] | `CODE_CONFIRMED` |
| **F011** | Nested Hierarchical Subtasks | Multi-level subtasks backed by `PARENT_SID` and `CHILD_IDS` task hierarchy. | [CODE-CONFIRMED] | `CODE_CONFIRMED` |
| **F012** | Due Date & Due Time | Explicit epoch timestamp for task completion deadline (`DUE_DATE`). | [CODE-CONFIRMED] | `CODE_CONFIRMED` |
| **F013** | Start Date & Task Duration | Multi-day task scheduling spanning from `START_DATE` to `DUE_DATE`. | [CODE-CONFIRMED] | `CODE_CONFIRMED` |
| **F014** | All-Day Tasks | Tasks scheduled for a calendar date without a specific time (`isAllDay=1`). | [CODE-CONFIRMED] | `CODE_CONFIRMED` |
| **F015** | Floating Overdue Tasks | Automatic rollover of overdue tasks to today's date (`IS_FLOATING=1`). | [CODE-CONFIRMED] | `CODE_CONFIRMED` |
| **F016** | Recurring Tasks (Standard) | Daily, Weekday, Weekly, Monthly, Yearly recurrence via standard iCalendar RRULE. | [CODE-CONFIRMED] | `CODE_CONFIRMED` |
| **F017** | Custom Recurrence Intervals | "Every X days/weeks/months/years" with specific weekday selections. | [CODE-CONFIRMED] | `CODE_CONFIRMED` |
| **F018** | Recurrence from Completion Date | Calculate next due date relative to completion date rather than due date (`repeatFrom=1`). | [CODE-CONFIRMED] | `CODE_CONFIRMED` |
| **F019** | Ebbinghaus Forgetting Curve Recurrence | Memory review intervals based on spaced repetition (`repeat.ForgettingCurve`). | [CODE-CONFIRMED] | `CODE_CONFIRMED` |
| **F020** | Lunar Calendar Recurrence | Annual recurrence based on Chinese lunar calendar dates (`Yearly (on Lunar %1$s)`). | [RESOURCE-CONFIRMED] | `VERIFIED` |
| **F021** | Recurrence End Conditions | Recurrence termination by date or by total occurrences count. | [CODE-CONFIRMED] | `CODE_CONFIRMED` |
| **F022** | Recurrence Exceptions (`EXDATE`) | Skip specific single occurrences without breaking the overall series (`EX_DATE`). | [CODE-CONFIRMED] | `CODE_CONFIRMED` |
| **F023** | Manual Drag-and-Drop Sorting | Reorder tasks arbitrarily via `SORT_ORDER` within lists, sections, or dates. | [CODE-CONFIRMED] | `CODE_CONFIRMED` |
| **F024** | Automated Multi-attribute Sorting | Sort by Due Date, Title, Priority, Creation Time (Ascending / Descending). | [CODE-CONFIRMED] | `CODE_CONFIRMED` |
| **F025** | Task Grouping | Visual grouping by Date, Priority, List, Tag, or Assignee headers. | [CODE-CONFIRMED] | `CODE_CONFIRMED` |
| **F026** | Multi-Task Batch Selection | Select multiple tasks for bulk Move, Date change, Priority update, or Deletion. | [CODE-CONFIRMED] | `CODE_CONFIRMED` |
| **F027** | Custom Swipe Gestures | Configurable short/long swipe actions (Complete, Won't Do, Pin, Date, Priority, Move, Delete). | [RESOURCE-CONFIRMED] | `VERIFIED` |
| **F028** | Task Attachments (Photos/Files) | Attach camera captures, gallery images, PDFs, and generic files (`ATTACHMENT`). | [CODE-CONFIRMED] | `CODE_CONFIRMED` |
| **F029** | Voice Note Attachments | Audio recording attached directly to task payload via microphone permission. | [CODE-CONFIRMED] | `CODE_CONFIRMED` |
| **F030** | Task Comments & Activity Log | Collaborative threaded comment stream (`COMMENT`) with timestamps and user IDs. | [CODE-CONFIRMED] | `CODE_CONFIRMED` |
| **F031** | Task Progress Percentage | Track manual progress completion from 0% to 100% (`PROGRESS`). | [CODE-CONFIRMED] | `CODE_CONFIRMED` |
| **F032** | Task Type Switching | Convert task freely between Text Note, Checklist, and Rich Markdown task. | [CODE-CONFIRMED] | `CODE_CONFIRMED` |
| **F033** | Task Templates | Save configured tasks as reusable templates (`TaskTemplateDao`). | [CODE-CONFIRMED] | `CODE_CONFIRMED` |
| **F034** | Location-Based Geofence Task | Attach geographical coordinates to trigger reminder on arrive/leave. | [CODE-CONFIRMED] | `CODE_CONFIRMED` |
| **F035** | Task Time Zone Binding | Pin task deadlines to specific time zones independently of device clock. | [CODE-CONFIRMED] | `CODE_CONFIRMED` |

---

## 2. Domain B: Reminder & Notification System (F036 – F055)

| ID | Feature Name | Classification / Description | Evidence Status | Verification |
| :--- | :--- | :--- | :--- | :--- |
| **F036** | Single Exact Reminder | Precise alarm trigger at specified due time using `SCHEDULE_EXACT_ALARM`. | [CODE-CONFIRMED] | `CODE_CONFIRMED` |
| **F037** | Multiple Reminders per Task | Configure up to 5 discrete reminder triggers per task (e.g. 1 day before, 1 hour before, at time). | [CODE-CONFIRMED] | `CODE_CONFIRMED` |
| **F038** | Advance Early Reminders | Pre-set offsets (5m, 15m, 30m, 1h, 1d before due date). | [RESOURCE-CONFIRMED] | `VERIFIED` |
| **F039** | Subtask / Checklist Reminders | Independent reminder triggers attached to individual subtask items. | [CODE-CONFIRMED] | `CODE_CONFIRMED` |
| **F040** | Geofence Arrival/Departure Reminders | GPS location triggers (e.g. "Remind when arriving at Office"). | [CODE-CONFIRMED] | `CODE_CONFIRMED` |
| **F041** | "Annoying Alert" Persistent Alarms | High-priority repeating full-screen alarm ringing every few minutes until dismissed (Pro). | [RESOURCE-CONFIRMED] | `VERIFIED` |
| **F042** | Full-Screen Alarm Dialog | Pop-up overlay interrupting screen even on lock screen (`USE_FULL_SCREEN_INTENT`). | [CODE-CONFIRMED] | `CODE_CONFIRMED` |
| **F043** | Snooze Presets | Standard snooze intervals: 15 minutes, 1 hour, 3 hours, Tomorrow morning, Custom time. | [RESOURCE-CONFIRMED] | `VERIFIED` |
| **F044** | Interactive Notification Actions | Direct "Complete" and "Snooze" action buttons on system notification shade. | [CODE-CONFIRMED] | `CODE_CONFIRMED` |
| **F045** | Priority-Specific Ringtones | Distinct sound files assigned to High, Medium, and Low priority task reminders. | [RESOURCE-CONFIRMED] | `VERIFIED` |
| **F046** | Do Not Disturb (DND) Override | Ring audible alarms even when device is set to Do Not Disturb for urgent tasks. | [RESOURCE-CONFIRMED] | `VERIFIED` |
| **F047** | Daily Morning Summary Notification | Configurable daily agenda briefing notification delivered at morning wakeup time. | [RESOURCE-CONFIRMED] | `VERIFIED` |
| **F048** | Daily Evening Review Notification | Reminder to review uncompleted tasks and plan tomorrow's schedule. | [RESOURCE-CONFIRMED] | `VERIFIED` |
| **F049** | Persistent Status Bar Notification | Ongoing pinned notification showing today's task count and quick-add input. | [RESOURCE-CONFIRMED] | `VERIFIED` |
| **F050** | Task Completion Sound | Audio feedback upon checking off a task (Jingle, Drip, Knock, Spiral, None). | [RESOURCE-CONFIRMED] | `VERIFIED` |
| **F051** | Haptic Vibration Feedback | Vibration pulses on task completion, alarm ringing, and drag-and-drop. | [CODE-CONFIRMED] | `CODE_CONFIRMED` |
| **F052** | Device Reboot Alarms Rescheduling | `RECEIVE_BOOT_COMPLETED` broadcast receiver restores all alarms into `AlarmManager`. | [CODE-CONFIRMED] | `CODE_CONFIRMED` |
| **F053** | Time Zone Change Recalculation | Automatically recompute epoch alarm triggers when device timezone changes. | [CODE-CONFIRMED] | `CODE_CONFIRMED` |
| **F054** | External Calendar Alarm Sync | Forward reminders to system calendar notifications. | [RESOURCE-CONFIRMED] | `VERIFIED` |
| **F055** | Email Notification Reminders | Optional cloud delivery of reminder notifications to registered account email. | [RESOURCE-CONFIRMED] | `VERIFIED` |

---

## 3. Domain C: Calendar & Scheduling (F056 – F075)

| ID | Feature Name | Classification / Description | Evidence Status | Verification |
| :--- | :--- | :--- | :--- | :--- |
| **F056** | Calendar Day View | 24-hour vertical timeline showing task blocks and imported calendar events. | [CODE-CONFIRMED] | `CODE_CONFIRMED` |
| **F057** | Calendar 3-Day View | Compact 3-day multi-column scheduling grid. | [CODE-CONFIRMED] | `CODE_CONFIRMED` |
| **F058** | Calendar Week View | 7-day visual schedule grid with multi-day event banners across the top. | [CODE-CONFIRMED] | `CODE_CONFIRMED` |
| **F059** | Calendar Month View | Classic month grid with colored dots, badges, or title bars per scheduled item. | [CODE-CONFIRMED] | `CODE_CONFIRMED` |
| **F060** | Calendar Agenda / List View | Chronological continuous list of scheduled events grouped by date header. | [CODE-CONFIRMED] | `CODE_CONFIRMED` |
| **F061** | School / Course Timetable View | Weekly recurring class schedule grid with course details and classroom locations (Pro). | [CODE-CONFIRMED] | `CODE_CONFIRMED` |
| **F062** | Drag-and-Drop Scheduling | Drag unplaced tasks from an "Arrange Tasks" drawer directly onto calendar time slots. | [CODE-CONFIRMED] | `CODE_CONFIRMED` |
| **F063** | Task Duration Resizing | Drag bottom edge of task block on calendar timeline to extend or shrink duration. | [CODE-CONFIRMED] | `CODE_CONFIRMED` |
| **F064** | Direct Calendar Task Checkbox | Complete tasks directly from calendar blocks without opening task detail. | [RESOURCE-CONFIRMED] | `VERIFIED` |
| **F065** | System Calendar Two-Way Sync | Import and display events from Google Calendar, Samsung Calendar, Outlook. | [CODE-CONFIRMED] | `CODE_CONFIRMED` |
| **F066** | CalDAV / URL Calendar Subscriptions | Subscribe to external .ics calendar feeds (e.g., sports, holidays, work). | [CODE-CONFIRMED] | `CODE_CONFIRMED` |
| **F067** | Habit Overlay on Calendar | Display completed habit check-in logs as markers across the calendar view. | [RESOURCE-CONFIRMED] | `VERIFIED` |
| **F068** | Focus Record Overlay on Calendar | Display completed Pomodoro and Stopwatch focus sessions on the 24-hour timeline. | [RESOURCE-CONFIRMED] | `VERIFIED` |
| **F069** | Countdown Milestone Overlay | Display countdown milestone markers directly on calendar dates. | [RESOURCE-CONFIRMED] | `VERIFIED` |
| **F070** | Calendar Filtering by List / Tag | Toggle visibility of individual lists, tags, or calendar accounts. | [CODE-CONFIRMED] | `CODE_CONFIRMED` |
| **F071** | Calendar Color Coding | Color blocks by List Color, Tag Color, or Priority Color. | [RESOURCE-CONFIRMED] | `VERIFIED` |
| **F072** | Show/Hide Declined Events | Option to display or hide calendar invites that user declined. | [RESOURCE-CONFIRMED] | `VERIFIED` |
| **F073** | Secondary Time Zone Grid | Dual time zone ruler alongside the 24-hour calendar grid for international work. | [RESOURCE-CONFIRMED] | `VERIFIED` |
| **F074** | Start Day of Week Configuration | Choose Sunday, Monday, or Saturday as first day of the week. | [RESOURCE-CONFIRMED] | `VERIFIED` |
| **F075** | Week Number Display | Toggle display of ISO week numbers (e.g., W42) in calendar margins. | [RESOURCE-CONFIRMED] | `VERIFIED` |

---

## 4. Domain D: Habit Tracking (F076 – F095)

| ID | Feature Name | Classification / Description | Evidence Status | Verification |
| :--- | :--- | :--- | :--- | :--- |
| **F076** | Habit Creation | Define title, icon, color, encouragement quote, and tracking frequency. | [CODE-CONFIRMED] | `CODE_CONFIRMED` |
| **F077** | Boolean Check-in Habits | Simple binary completion habits (e.g., "Take vitamins", "Meditate"). | [CODE-CONFIRMED] | `CODE_CONFIRMED` |
| **F078** | Quantitative / Numeric Habits | Habits with numerical target and measurement unit (e.g. 2000 ml, 30 pages). | [CODE-CONFIRMED] | `CODE_CONFIRMED` |
| **F079** | Habit Time-of-Day Sections | Group habits by routine period: Morning, Afternoon, Evening, or Any Time. | [CODE-CONFIRMED] | `CODE_CONFIRMED` |
| **F080** | Custom Frequency Schedules | Daily, Specific Weekdays (e.g., Mon/Wed/Fri), or X times per week/month. | [CODE-CONFIRMED] | `CODE_CONFIRMED` |
| **F081** | Habit Daily Streaks | Calculate and display current consecutive days streak and all-time best streak. | [CODE-CONFIRMED] | `CODE_CONFIRMED` |
| **F082** | Habit Check-In Log & Journaling | Attach written reflection or journal entry to a daily habit check-in. | [RESOURCE-CONFIRMED] | `VERIFIED` |
| **F083** | Dedicated Habit Reminders | Multiple scheduled alarms per habit to prompt routine check-in. | [CODE-CONFIRMED] | `CODE_CONFIRMED` |
| **F084** | Habit Linked Focus Session | Launch a Pomodoro or Stopwatch session linked directly to a habit goal. | [RESOURCE-CONFIRMED] | `VERIFIED` |
| **F085** | Habit Monthly Heatmap | Color-coded grid visualization showing daily completion intensity across the month. | [CODE-CONFIRMED] | `CODE_CONFIRMED` |
| **F086** | Habit Archive / Pause | Freeze habit tracking without deleting historical streaks or stats (`FROZEN_HABIT_DATA`).| [CODE-CONFIRMED] | `CODE_CONFIRMED` |
| **F087** | Skip Habit Day | Mark a habit day explicitly skipped (e.g. sick day) to preserve streak continuity. | [CODE-CONFIRMED] | `CODE_CONFIRMED` |
| **F088** | Habit Show in "Today" View | Display pending habits alongside tasks on the Today dashboard. | [RESOURCE-CONFIRMED] | `VERIFIED` |
| **F089** | Habit Counter in App Badge | Include pending habits in the app icon uncompleted notification badge count. | [RESOURCE-CONFIRMED] | `VERIFIED` |
| **F090** | Habit Share Card | Generate graphical achievement card showing streak to share with peers. | [CODE-CONFIRMED] | `CODE_CONFIRMED` |

---

## 5. Domain E: Focus & Pomodoro System (F091 – F110)

| ID | Feature Name | Classification / Description | Evidence Status | Verification |
| :--- | :--- | :--- | :--- | :--- |
| **F091** | Pomodoro Work Timer | Countdown focus timer with standard 25-minute default interval (`PomodoroConfig`). | [CODE-CONFIRMED] | `CODE_CONFIRMED` |
| **F092** | Short & Long Breaks | Automatic transition to 5-minute short break and 15-minute long break every 4 cycles. | [CODE-CONFIRMED] | `CODE_CONFIRMED` |
| **F093** | Stopwatch Mode | Open-ended count-up timer for unconstrained focus tasks. | [CODE-CONFIRMED] | `CODE_CONFIRMED` |
| **F094** | Task-Linked Focus Session | Associate focus session with a specific task; records session under task history. | [CODE-CONFIRMED] | `CODE_CONFIRMED` |
| **F095** | Ambient White Noise Generator | Background soothing audio loops (Rain, Ocean, Cafe, Forest, White Noise, Campfire). | [CODE-CONFIRMED] | `CODE_CONFIRMED` |
| **F096** | Foreground Audio Service | Continuous audio playback of white noise via `FOREGROUND_SERVICE_MEDIA_PLAYBACK`. | [CODE-CONFIRMED] | `CODE_CONFIRMED` |
| **F097** | Strict Mode & App Whitelisting | Enforce lock-out preventing navigation outside TickTick during active focus session. | [RESOURCE-CONFIRMED] | `VERIFIED` |
| **F098** | Flip Phone to Start Focus | Hardware accelerometer trigger: start timer automatically by turning phone face down. | [RESOURCE-CONFIRMED] | `VERIFIED` |
| **F099** | OLED Anti-Burn-In Protection | Micro-shift digital clock coordinates periodically during full-screen desk clock. | [RESOURCE-CONFIRMED] | `VERIFIED` |
| **F100** | Floating Window Timer Ball | Picture-in-picture floating countdown overlay visible across other apps. | [RESOURCE-CONFIRMED] | `VERIFIED` |
| **F101** | Focus Interruption Tracking | Record and log reasons when a focus session is paused or terminated prematurely. | [CODE-CONFIRMED] | `CODE_CONFIRMED` |
| **F102** | Multi-Device Focus Auto-Sync | Synchronize active focus timer countdown across phone, desktop, and web in real-time (Pro). | [RESOURCE-CONFIRMED] | `VERIFIED` |
| **F103** | Daily & Weekly Focus Target | Set target focus hours (e.g. 4 hours/day) with progress indicators. | [CODE-CONFIRMED] | `CODE_CONFIRMED` |
| **F104** | Focus Distribution Analytics | Pie charts and bar graphs displaying focus time distribution by List and Tag. | [CODE-CONFIRMED] | `CODE_CONFIRMED` |
| **F105** | Virtual Study Room | Collaborative focus room displaying real-time avatars of other focused users. | [RESOURCE-CONFIRMED] | `VERIFIED` |

---

## 6. Domain F: Lists, Folders & Organization (F106 – F130)

| ID | Feature Name | Classification / Description | Evidence Status | Verification |
| :--- | :--- | :--- | :--- | :--- |
| **F106** | Custom Task Lists | Unlimited distinct task lists with title, custom color, and view modes. | [CODE-CONFIRMED] | `CODE_CONFIRMED` |
| **F107** | List Folders (`PROJECT_GROUP`) | Group multiple related lists into collapsible folder hierarchies. | [CODE-CONFIRMED] | `CODE_CONFIRMED` |
| **F108** | Kanban Board View | Horizontal columns (`COLUMN`) with card drag-and-drop between workflow stages. | [CODE-CONFIRMED] | `CODE_CONFIRMED` |
| **F109** | Timeline Gantt View | Horizontal multi-day task duration bars showing project dependencies. | [CODE-CONFIRMED] | `CODE_CONFIRMED` |
| **F110** | Smart Lists ("Today", "Next 7 Days") | Dynamic automated filters aggregating tasks matching temporal criteria. | [CODE-CONFIRMED] | `CODE_CONFIRMED` |
| **F111** | Smart List ("All", "Completed") | Master aggregate view of all active or historically completed tasks. | [CODE-CONFIRMED] | `CODE_CONFIRMED` |
| **F112** | Smart List ("Assigned to Me") | Filter showing collaborative tasks assigned to current user. | [CODE-CONFIRMED] | `CODE_CONFIRMED` |
| **F113** | Custom Smart Filters (`FILTER`) | User-defined smart lists with multi-condition rules (Date, Priority, List, Tag). | [CODE-CONFIRMED] | `CODE_CONFIRMED` |
| **F114** | Hierarchical Tags | Nested organizational tags (e.g. `#work/projectA`, `#finance/taxes`). | [CODE-CONFIRMED] | `CODE_CONFIRMED` |
| **F115** | Tag Colors | Assign distinct color palettes to tags for visual prioritization. | [CODE-CONFIRMED] | `CODE_CONFIRMED` |
| **F116** | Archive List | Archive completed lists to clean up sidebar while preserving historical data. | [CODE-CONFIRMED] | `CODE_CONFIRMED` |
| **F117** | List Custom Backgrounds | Set custom cover illustrations or gradient backdrops for individual lists. | [CODE-CONFIRMED] | `CODE_CONFIRMED` |
| **F118** | List Notification Muting | Mute alert sounds and popups for specific low-priority lists. | [CODE-CONFIRMED] | `CODE_CONFIRMED` |
| **F119** | Left Sidebar Navigation Customization | Pin, reorder, show, or hide specific smart lists, folders, and tabs. | [CODE-CONFIRMED] | `CODE_CONFIRMED` |
| **F120** | Bottom Navigation Bar Customization | Choose 3-5 tabs displayed in bottom navigation (Tasks, Calendar, Habits, Focus, Search). | [RESOURCE-CONFIRMED] | `VERIFIED` |

---

## 7. Domain G: Smart NLP & Machine Learning (F121 – F135)

| ID | Feature Name | Classification / Description | Evidence Status | Verification |
| :--- | :--- | :--- | :--- | :--- |
| **F121** | Natural Language Date Parsing | Automatically parse date/time from input (e.g., "Meeting tomorrow at 3pm"). | [RESOURCE-CONFIRMED] | `VERIFIED` |
| **F122** | NLP Recurrence Extraction | Parse recurrence keywords (e.g., "every Monday", "daily at 8am"). | [RESOURCE-CONFIRMED] | `VERIFIED` |
| **F123** | NLP Tag Parsing | Detect `#tag` syntax during input and convert to formal task tag. | [RESOURCE-CONFIRMED] | `VERIFIED` |
| **F124** | NLP Priority Parsing | Detect `!` or `!high` syntax to set priority level automatically. | [RESOURCE-CONFIRMED] | `VERIFIED` |
| **F125** | Smart Keyword Stripping | Automatically remove parsed date and tag keywords from task title upon save. | [RESOURCE-CONFIRMED] | `VERIFIED` |
| **F126** | Voice Task Creation | Speech-to-text task entry with automated entity extraction. | [CODE-CONFIRMED] | `CODE_CONFIRMED` |
| **F127** | Clipboard Task Detection | Detect copied text when app opens and suggest creating task. | [RESOURCE-CONFIRMED] | `VERIFIED` |
| **F128** | Smart URL Metadata Preview | Extract OpenGraph web page title, description, and favicon from links. | [RESOURCE-CONFIRMED] | `VERIFIED` |
| **F129** | Optical Character Recognition (OCR) | Extract text from photo attachments using on-device Google ML Kit. | [CODE-CONFIRMED] | `CODE_CONFIRMED` |
| **F130** | AI Assistant Task Breakdown | Use AI to suggest subtasks and breakdown large goals into actionable steps (Pro). | [RESOURCE-CONFIRMED] | `VERIFIED` |

---

## 8. Domain H: Team Collaboration (F131 – F145)

| ID | Feature Name | Classification / Description | Evidence Status | Verification |
| :--- | :--- | :--- | :--- | :--- |
| **F131** | Shared Lists | Share an entire task list with other registered TickTick accounts via email link. | [CODE-CONFIRMED] | `CODE_CONFIRMED` |
| **F132** | Task Assignment | Assign task responsibility to a specific collaborator (`ASSIGNEE`). | [CODE-CONFIRMED] | `CODE_CONFIRMED` |
| **F133** | Collaborator Role Permissions | Assign "Read Only", "Can Edit", or "Admin" privileges to list members. | [CODE-CONFIRMED] | `CODE_CONFIRMED` |
| **F134** | Collaborative Comments Stream | Threaded comments, attachment uploads, and mentions (`@username`) on tasks. | [CODE-CONFIRMED] | `CODE_CONFIRMED` |
| **F135** | Activity Log / Change Audit | Real-time audit log of who created, edited, completed, or deleted tasks. | [CODE-CONFIRMED] | `CODE_CONFIRMED` |
| **F136** | Team Spaces (`TEAM`, `TEAM_MEMBER`) | Organizational workspaces with centralized billing and directory. | [CODE-CONFIRMED] | `CODE_CONFIRMED` |

---

## 9. Domain I: Productivity Analytics & Tools (F146 – F160)

| ID | Feature Name | Classification / Description | Evidence Status | Verification |
| :--- | :--- | :--- | :--- | :--- |
| **F146** | Eisenhower Matrix 4-Quadrant View | Prioritize tasks into Urgency x Importance matrix (`MATRIX_PROFILE`). | [CODE-CONFIRMED] | `CODE_CONFIRMED` |
| **F147** | Custom Matrix Profiles | Create multiple matrix views with customized quadrant criteria (Pro). | [RESOURCE-CONFIRMED] | `VERIFIED` |
| **F148** | Productivity Achievement Score | Calculated karma / achievement score reflecting daily on-time completion rates. | [CODE-CONFIRMED] | `CODE_CONFIRMED` |
| **F149** | Productivity Levels & Badges | Gamified tier levels and unlockable achievement medals. | [CODE-CONFIRMED] | `CODE_CONFIRMED` |
| **F150** | Daily / Weekly Productivity Reports | Historical completion graphs, completion velocity, and on-time percentage. | [CODE-CONFIRMED] | `CODE_CONFIRMED` |
| **F151** | Annual Year-in-Review Report | Annual summary infographic of total tasks completed, focus hours, and top habits. | [CODE-CONFIRMED] | `CODE_CONFIRMED` |
| **F152** | Event Countdown Milestones | Countdown cards showing days remaining until events (`COUNTDOWN`). | [CODE-CONFIRMED] | `CODE_CONFIRMED` |

---

## 10. Domain J: Personalization & Themes (F161 – F175)

| ID | Feature Name | Classification / Description | Evidence Status | Verification |
| :--- | :--- | :--- | :--- | :--- |
| **F161** | Light / Dark / OLED Black Themes | Theme modes with pure black background for battery saving on OLED screens. | [RESOURCE-CONFIRMED] | `VERIFIED` |
| **F162** | Colorful Accent Palettes | Season, city, and color palette themes (e.g. Classic Blue, Morandi, Sakura, Forest). | [RESOURCE-CONFIRMED] | `VERIFIED` |
| **F163** | Dynamic Material You / Monet Theming | Adaptive theme color extraction matching Android system wallpaper colors. | [RESOURCE-CONFIRMED] | `VERIFIED` |
| **F164** | Custom App Launcher Icons | Select alternative launcher icons on device home screen. | [RESOURCE-CONFIRMED] | `VERIFIED` |
| **F165** | Multi-Language Support | 17 localized languages with independent in-app language override. | [RESOURCE-CONFIRMED] | `VERIFIED` |

---

## 11. Domain K: Data Management, Sync & Security (F176 – F195)

| ID | Feature Name | Classification / Description | Evidence Status | Verification |
| :--- | :--- | :--- | :--- | :--- |
| **F176** | Offline-First Data Persistence | 100% of tasks, lists, habits, and notes can be viewed, created, and edited offline. | [CODE-CONFIRMED] | `CODE_CONFIRMED` |
| **F177** | Bidirectional Cloud Sync | Delta synchronization syncing only modified entities using ETags and timestamps. | [CODE-CONFIRMED] | `CODE_CONFIRMED` |
| **F178** | Real-Time WebSocket Push Sync | Instant update delivery across active devices via WebSockets. | [CODE-CONFIRMED] | `CODE_CONFIRMED` |
| **F179** | Conflict Resolution (Last-Write-Wins) | Reconcile concurrent offline edits using modification timestamps and ETags. | [CODE-CONFIRMED] | `CODE_CONFIRMED` |
| **F180** | Manual Local Backup & Export | Export local backup archive (`.csv` / `.json` backup file). | [CODE-CONFIRMED] | `CODE_CONFIRMED` |
| **F181** | Third-Party Data Import | Import tasks from Todoist, Wunderlist, Any.do, GTasks, Microsoft To Do, CSV. | [RESOURCE-CONFIRMED] | `VERIFIED` |
| **F182** | Notion Database Sync | Two-way sync linking tasks to Notion database blocks (`notionBlock`). | [CODE-CONFIRMED] | `CODE_CONFIRMED` |
| **F183** | Pattern & Biometric App Lock | Protect entire app or specific private lists with PIN, Pattern, or Fingerprint. | [RESOURCE-CONFIRMED] | `VERIFIED` |
| **F184** | Wi-Fi Only Attachment Sync | Option to restrict image and file attachment downloads to Wi-Fi networks. | [RESOURCE-CONFIRMED] | `VERIFIED` |

---

## 12. Domain L: Widgets & Integrations (F196 – F215)

| ID | Feature Name | Classification / Description | Evidence Status | Verification |
| :--- | :--- | :--- | :--- | :--- |
| **F196** | Standard Task List Widget | Scrollable home screen widget showing tasks with interactive completion checkboxes. | [RESOURCE-CONFIRMED] | `VERIFIED` |
| **F197** | Calendar Month & Week Widget | Full month calendar grid or multi-column week schedule on home screen. | [RESOURCE-CONFIRMED] | `VERIFIED` |
| **F198** | Habit Grid & Progress Widget | Check in habits directly from home screen without opening app. | [RESOURCE-CONFIRMED] | `VERIFIED` |
| **F199** | Pomodoro / Focus Timer Widget | Start, pause, and view focus timer from home screen. | [RESOURCE-CONFIRMED] | `VERIFIED` |
| **F200** | Eisenhower Matrix Widget | 2x2 interactive quadrant grid widget on home screen. | [RESOURCE-CONFIRMED] | `VERIFIED` |
| **F201** | Quick Add Floating Button Widget | 1x1 shortcut icon or mini-bar for instant task voice/text entry. | [RESOURCE-CONFIRMED] | `VERIFIED` |
| **F202** | Assistive Quick Ball | Floating overlay ball on screen edge accessible inside any app. | [RESOURCE-CONFIRMED] | `VERIFIED` |
| **F203** | Huawei WearEngine Smartwatch Integration | Sync tasks and action alarms from Huawei smartwatch. | [CODE-CONFIRMED] | `CODE_CONFIRMED` |
| **F204** | Vivo Health Smartwatch Integration | Sync fitness and focus data with Vivo health ecosystem. | [CODE-CONFIRMED] | `CODE_CONFIRMED` |
| **F205** | IFTTT & Zapier Webhook Automation | Connect external webhooks to trigger task creation and completion notifications. | [RESOURCE-CONFIRMED] | `VERIFIED` |
| **F206** | Telegram Bot Task Integration | Send text or voice notes to TickTick Telegram bot to auto-create tasks. | [RESOURCE-CONFIRMED] | `VERIFIED` |
