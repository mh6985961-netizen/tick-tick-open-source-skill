# Settings and Configuration Specifications

## 1. Overview of Configuration Architecture

TickTick's user settings are organized via standard Android `PreferenceFragmentCompat` screens backed by encrypted or private `SharedPreferences` and synchronized to the user's remote profile via the `UserPreference` network sync entity.

This document provides a comprehensive, field-by-field audit of all configuration screens, preference XML definitions, keys, types, default values, and their functional effects across the application.

---

## 2. Master Settings Catalog by Category

### 2.1 Root Settings (`preferences.xml`)
The top-level configuration screen accessed via the navigation drawer gear icon.

| Preference Key | Type | Default Value | Title / Label | Functional Behavior |
| :--- | :--- | :--- | :--- | :--- |
| `prefkey_account_settings` | `Preference` | — | Account & Profile | Launches `AccountInfoFragment`. Displays user email, avatar, nickname, Pro status expiration, and password/MFA options. |
| `prefkey_theme` | `Preference` | "Default Blue" | Appearance & Themes | Launches `CustomThemeActivity`. Controls app primary color, dark theme (Auto/Dark/Light/AMOLED Pure Black), and icon packs. |
| `prefkey_sound_and_notifications` | `Preference` | — | Sounds & Notifications | Launches `sound_reminder_and_notification_preferences.xml`. Configures ringtones, vibration patterns, and notification channels. |
| `prefkey_date_and_time` | `Preference` | — | Date & Time | Launches `date_and_time_preference.xml`. Configures date formats, 24-hour vs 12-hour clock, and time zone selection. |
| `prefkey_smart_recognition` | `Preference` | — | Smart Recognition | Launches `preference_smart_date_parse.xml`. Controls real-time NLP text parsing for dates, priorities, lists, and tags. |
| `prefkey_task_defaults` | `Preference` | — | Task Defaults | Launches `task_quick_add_preference.xml`. Sets default due date (None/Today), default reminder time, and default list. |
| `prefkey_habit_settings` | `Preference` | — | Habits | Launches `preference_habit_settings.xml`. Configures habit archiving, auto-backup, and section management. |
| `prefkey_pomodoro_settings` | `Preference` | — | Focus / Pomodoro | Launches `preference_pomodoro.xml`. Sets timer durations (work/break), strict mode, white noise volume, and flip-to-focus. |
| `prefkey_lock` | `Preference` | — | Security & App Lock | Launches `lock_preferences.xml`. Configures Pattern lock, PIN, Biometric/Fingerprint authentication, and auto-lock delay. |
| `prefkey_more_settings` | `Preference` | — | More Settings | Launches `more_settings_preferences.xml`. Language selection, swipe gestures, widget configuration, and experimental features. |

---

### 2.2 Smart Recognition & NLP (`preference_smart_date_parse.xml`)

| Preference Key | Type | Default Value | Functional Behavior in Code |
| :--- | :--- | :--- | :--- |
| `prefkey_smart_date_parse_enable` | `SwitchPreference` | `true` | Master toggle for natural language parsing. When disabled, dates entered in text are treated as literal strings. |
| `prefkey_smart_recognition_remove_text` | `SwitchPreference` | `true` | When enabled, recognized temporal phrases (e.g., "tomorrow at 5pm") are stripped from the task title upon saving. |
| `prefkey_smart_time_parse_enable` | `SwitchPreference` | `true` | Enables automatic parsing of time tokens (e.g., "15:00", "3pm", "noon", "midnight"). |
| `prefkey_smart_priority_parse_enable` | `SwitchPreference` | `true` | Enables exclamation mark priority parsing (`!1` for High, `!2` for Medium, `!3` for Low). |
| `prefkey_smart_project_parse_enable` | `SwitchPreference` | `true` | Enables tilde list assignment parsing (`~ListName`). |
| `prefkey_smart_tag_parse_enable` | `SwitchPreference` | `true` | Enables hashtag parsing (`#TagName`). |
| `prefkey_smart_parse_language` | `ListPreference` | "Auto" | Selects specific language NLP model (English, Chinese, French, German, Japanese, Spanish, Russian). |

---

### 2.3 Sounds, Reminders & Annoying Alerts (`advance_reminder_preferences.xml`, `sound_reminder_and_notification_preferences.xml`)

| Preference Key | Type | Default Value | Functional Behavior in Code |
| :--- | :--- | :--- | :--- |
| `prefkey_reminder_sound` | `RingtonePreference` | "ticktick_bell.ogg" | Custom ringtone played on notification arrival. |
| `prefkey_vibration` | `SwitchPreference` | `true` | Toggles device vibrator motor for alerts (`long[] {0, 250, 200, 250}`). |
| `prefkey_annoying_alert` | `SwitchPreference` | `false` | **Pro Feature: Annoying Alert**. When enabled, missed reminders ring continuously or repeat every 2 minutes until explicitly snoozed or dismissed. |
| `prefkey_annoying_alert_interval` | `ListPreference` | "2 min" | Interval options: 1 min, 2 min, 5 min, 10 min. |
| `prefkey_reminder_dnd_override` | `SwitchPreference` | `false` | Requests `ACCESS_NOTIFICATION_POLICY` to bypass system Do Not Disturb (DND) for high-priority task alarms. |
| `prefkey_daily_reminder_morning` | `SwitchPreference` | `true` | Daily Agenda summary notification delivered at configured morning time (default: 08:30). |
| `prefkey_daily_reminder_evening` | `SwitchPreference` | `false` | Evening recap notification delivered at configured time (default: 20:00). |
| `prefkey_status_bar_sticky` | `SwitchPreference` | `false` | Keeps an ongoing, non-dismissible notification in the Android status bar displaying Today's remaining tasks. |

---

### 2.4 Focus & Pomodoro Settings (`preference_pomodoro.xml`, `preference_pomodoro_focus.xml`)

| Preference Key | Type | Default Value | Functional Behavior in Code |
| :--- | :--- | :--- | :--- |
| `prefkey_pomodoro_duration` | `ListPreference` | "25" | Focus duration in minutes (options: 5 to 180 min; default: 25 min). |
| `prefkey_short_break_duration` | `ListPreference` | "5" | Short break duration in minutes (options: 1 to 30 min; default: 5 min). |
| `prefkey_long_break_duration` | `ListPreference` | "15" | Long break duration in minutes (options: 5 to 60 min; default: 15 min). |
| `prefkey_long_break_frequency` | `ListPreference` | "4" | Number of completed Pomodoro sessions before triggering a long break. |
| `prefkey_pomo_auto_start_break` | `SwitchPreference` | `false` | Automatically starts the break countdown immediately when a focus session ends. |
| `prefkey_pomo_auto_start_next` | `SwitchPreference` | `false` | Automatically starts the next focus session when a break countdown ends. |
| `prefkey_strict_mode` | `SwitchPreference` | `false` | Prevents leaving the app during an active focus session; locks the screen to the timer dial. |
| `prefkey_strict_mode_whitelist` | `Preference` | — | Configures allowed apps during Strict Mode (e.g., Dictionary, Calculator). |
| `prefkey_flip_to_focus` | `SwitchPreference` | `true` | Enables accelerometer detection: turning the phone facedown starts the focus timer. |
| `prefkey_oled_anti_burn_in` | `SwitchPreference` | `true` | Jitters digital clock pixels every 60s in fullscreen night focus mode. |
| `prefkey_ambient_white_noise` | `ListPreference` | "Rain" | Default background audio track for focus sessions. |
| `prefkey_ambient_volume` | `SeekBarPreference` | 80 | Volume percentage for ambient background audio playback. |

---

### 2.5 Habit Settings (`preference_habit_settings.xml`)

| Preference Key | Type | Default Value | Functional Behavior in Code |
| :--- | :--- | :--- | :--- |
| `prefkey_habit_show_in_today` | `SwitchPreference` | `true` | Embeds daily scheduled habits into the "Today" task list view. |
| `prefkey_habit_auto_archive` | `SwitchPreference` | `false` | Automatically archives habits with zero check-ins over a 30-day period. |
| `prefkey_habit_sound` | `SwitchPreference` | `true` | Plays celebratory chime (`habit_complete.ogg`) upon check-in completion. |
| `prefkey_habit_haptic` | `SwitchPreference` | `true` | Emits tactile vibration upon completing a daily habit target. |
| `prefkey_habit_section_order` | `Preference` | — | Launches section manager allowing reordering of habit categories (Morning/Afternoon/Evening). |

---

### 2.6 Calendar View Options (`preference_calendar_view_options.xml`)

| Preference Key | Type | Default Value | Functional Behavior in Code |
| :--- | :--- | :--- | :--- |
| `prefkey_calendar_start_of_week` | `ListPreference` | "1" (Monday) | First day of the week in calendar grids: Monday (`1`), Sunday (`0`), or Saturday (`6`). |
| `prefkey_calendar_default_view` | `ListPreference` | "Month" | Default view on opening Calendar tab: "Month", "Week", "Day", "3-Day", or "Agenda". |
| `prefkey_calendar_show_completed` | `SwitchPreference` | `true` | Toggles rendering of completed tasks in past calendar date blocks. |
| `prefkey_calendar_show_lunar` | `SwitchPreference` | `false` | Displays Chinese Lunar calendar dates beneath Gregorian numbers. |
| `prefkey_calendar_show_week_numbers`| `SwitchPreference` | `false` | Displays ISO-8601 week numbers along the left margin of the month grid. |
| `prefkey_calendar_visible_hours_start`| `ListPreference` | "08:00" | Starting hour boundary for vertical Day and Week view grids. |
| `prefkey_calendar_visible_hours_end` | `ListPreference` | "22:00" | Ending hour boundary for vertical Day and Week view grids. |

---

### 2.7 App Lock & Security (`lock_preferences.xml`)

| Preference Key | Type | Default Value | Functional Behavior in Code |
| :--- | :--- | :--- | :--- |
| `prefkey_task_pattern_lock_enable` | `SwitchPreference` | `false` | Enables password protection for launching the application. |
| `prefkey_lock_type` | `ListPreference` | "Pattern" | Protection mechanism: "Pattern" (3x3 grid) or "PIN" (4-digit numeric code). |
| `prefkey_biometric_enable` | `SwitchPreference` | `true` | Enables Android `BiometricPrompt` (Fingerprint / Face Unlock) to unlock without entering pattern/PIN. |
| `prefkey_lock_delay` | `ListPreference` | "0" (Immediately) | Auto-lock timeout after app transitions to background: Immediately, 1 min, 5 min, 15 min. |
| `prefkey_stealth_mode` | `SwitchPreference` | `false` | Masks pattern trace line on the 3x3 grid so observers cannot see the drawn pattern. |

---

### 2.8 AI Assistant & Smart Features (`preferences_ai_feature.xml`)

| Preference Key | Type | Default Value | Functional Behavior in Code |
| :--- | :--- | :--- | :--- |
| `prefkey_ai_assistant_enable` | `SwitchPreference` | `true` | Enables AI breakdown suggestions and task generation inside Task Detail view. |
| `prefkey_ai_subtask_generation` | `SwitchPreference` | `true` | Displays "Break Down with AI" button in task checklists; queries remote AI endpoint (`/api/v1/conversations`). |
| `prefkey_ai_daily_summary` | `SwitchPreference` | `false` | Generates automated morning executive summaries of scheduled tasks and meetings. |
| `prefkey_ai_tone_of_voice` | `ListPreference` | "Concise" | Sets personality of AI suggestions: "Concise", "Detailed", "Motivational". |

---

### 2.9 Data Import, Export & Backup (`data_import_preferences.xml`)

| Preference Key | Type | Default Value | Functional Behavior in Code |
| :--- | :--- | :--- | :--- |
| `prefkey_import_todoist` | `Preference` | — | OAuth / CSV import bridge for migrating tasks, projects, and tags from Todoist. |
| `prefkey_import_wunderlist` | `Preference` | — | Legacy import tool for Wunderlist zip backup archives. |
| `prefkey_import_ms_todo` | `Preference` | — | Microsoft Graph API OAuth bridge for importing Microsoft To-Do lists. |
| `prefkey_export_csv` | `Preference` | — | Exports all active and completed tasks into an open `.csv` spreadsheet archive. |
| `prefkey_local_backup` | `Preference` | — | Creates a full local SQLite dump archive (`.bak`) in device storage. |
| `prefkey_auto_backup` | `SwitchPreference` | `true` | Automatically generates weekly backup snapshots retained in device storage. |
