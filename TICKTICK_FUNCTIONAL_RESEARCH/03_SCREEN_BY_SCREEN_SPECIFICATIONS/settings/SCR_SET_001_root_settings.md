# Screen Specification: SCR-SET-001 - Root Settings Menu

### Screen ID
`SCR-SET-001`

### Screen Name
Root Settings Menu (`SettingActivity`)

### Purpose
Provides top-level organization and entry points for all application preferences, account details, customization options, and system integrations.

### Entry Points
1. Tapping the Gear icon at the bottom of `NavDrawerFragment`.
2. Overflow menu on certain main screens.

### Screen Contents
* **Top Navigation Bar**:
  * Back navigation arrow.
  * Title: "Settings".
* **Preference Categories & Rows (`preferences.xml`)**:
  * **Account Section**:
    * Avatar, User Nickname, Email address, and Pro status badge ("PRO" or "Free").
  * **General Section**:
    * Appearance & Themes (Current theme name).
    * Sounds & Notifications (Ringtone and channel shortcuts).
    * Date & Time (Date format and 24-hr toggle).
    * Smart Recognition (NLP parsing toggles).
    * Task Defaults (Default due date and list).
    * Habits (Section order and reminder times).
    * Focus / Pomodoro (Timer durations and white noise).
  * **Security & Privacy Section**:
    * App Lock (Pattern / PIN / Biometric status).
    * Privacy Settings (Analytics and telemetry toggles).
  * **Data Management Section**:
    * Backup & Import (Todoist, MS To-Do, CSV export, local `.bak`).
  * **About Section**:
    * Version string (`8.3.0.1`), What's New changelog, Help & FAQ, Terms of Service.

### Available Actions
1. Tap any category item to open its sub-preference screen.
2. Tap Account card to open `AccountInfoFragment`.
3. Tap "Log Out" at bottom of screen to invalidate tokens and return to `LoginMainActivity`.

### Navigation
* Leads to specific preference activities cataloged in `07_SETTINGS_AND_CONFIGURATION.md`.

### Data Requirements
* Active `UserPreference` and `UserProfile` caches.

### Evidence
* `com.ticktick.task.activity.preference.SettingActivity`
* `res/xml/preferences.xml`

### Confidence
Confirmed `[CODE-CONFIRMED]`.
