# Screen Specification: SCR-FOC-001 - Pomodoro Dial & Focus Hub

### Screen ID
`SCR-FOC-001`

### Screen Name
Focus Hub & Pomodoro Dial (`PomodoroActivity`)

### Purpose
Implements the central productivity timer interface, supporting both countdown Pomodoros and open-ended stopwatches, task associations, ambient white noise playback, and distraction-free focus sessions.

### Entry Points
1. "Focus" tab on bottom navigation bar (`TabBar`).
2. Swipe action "Start Focus" on a task row in `SCR-TASK-001`.
3. "Start Focus" option in `SCR-TASK-002` (Task Detail).
4. Deep link: `ticktick://focus/start?duration=25`.

### Screen Contents
* **Top Mode Switcher**:
  * Segmented toggle button: **[ POMODORO ]** (Countdown) vs. **[ STOPWATCH ]** (Countup).
* **Central Interactive Dial Area**:
  * Circular progress ring with draggable rotary slider bead (`PomoDialView`).
  * Center Digital Timer display (e.g. `25:00`) in large monospace typography.
  * Associated Task Chip: Displays bound task title (e.g. "Draft Q3 Financials") with "X" unbind button. If unassociated, displays "Select a task to focus on".
* **Controls & Settings Row**:
  * **White Noise Button**: Displays active ambient audio track (e.g. "Rain", "Café", "None") with volume icon.
  * **Strict Mode Toggle**: Padlock icon showing Strict Mode status (On/Off).
  * **Fullscreen / Night Mode Button**: Moon icon to switch to OLED pure black digital clock mode.
* **Bottom Action Controls**:
  * Large Primary Start Button ("START" / "PAUSE" / "RESUME").
  * Secondary Stop / Give Up button (Square icon).

### Available Actions
1. Drag circular dial bead to adjust countdown minutes (5 to 180 minutes).
2. Tap Start to commence focus countdown.
3. Tap Pause to temporarily halt timer.
4. Tap Give Up / Stop to terminate session (prompts: "Abandon session or save partial focus?").
5. Tap White Noise to open `SCR-FOC-002` (`ChoosePomoSoundActivity`).
6. Turn phone facedown on a flat surface to trigger Flip-to-Focus accelerometer start.

### Interaction Behavior
* **Dial Physics**: Angular dragging snaps in increments of 5 minutes, emitting discrete tactile tick vibrations.
* **Running State**: Outer circular ring animates clockwise; digital countdown updates every second.
* **Completion Event**: When reaching `00:00`, rings alarm sound, vibrates device, logs entry in `Pomodoro` SQLite table, and launches `SCR-FOC-003` (`PomoPopupActivity`).

### Input Fields
* No text fields; duration input is managed via rotary dial drag.

### Navigation
* Tapping White Noise opens `SCR-FOC-002` (`ChoosePomoSoundActivity`).
* Tapping Focus History icon opens `FocusTimelineActivity`.
* Session completion navigates to `SCR-FOC-003` (`PomoPopupActivity`).

### Different States
* **Idle State**: Timer dial shows default duration (25:00); Start button enabled.
* **Running State**: Dial animating; "Pause" and "Stop" buttons visible; notification active in status bar.
* **Paused State**: Timer static; "Resume" and "Give Up" buttons visible.
* **Strict Mode Running**: Home and Back buttons intercepted; switching apps logs interruption warning.
* **OLED Night State**: Minimalist digital clock with random ±3px coordinate shift every 60s to prevent burn-in.

### Data Requirements
* Active `PomodoroConfig` (durations for work, short break, long break).
* Optional bound `Tasks2` row.

### Related Features
* Focus Timer (`F091`), Ambient Sounds (`F093`), Strict Mode (`F094`), Focus Analytics (`F096`).

### Subscription Restrictions
* Free tier includes 3 basic ambient sounds (Rain, White Noise, Waves).
* Pro tier unlocks full ambient library (15+ tracks) and auto-syncing of focus records across desktop/mobile.

### Evidence
* `com.ticktick.task.activity.PomodoroActivity`
* `res/layout/activity_pomodoro.xml`
* `com.ticktick.task.view.PomoDialView`

### Confidence
Confirmed `[CODE-CONFIRMED]`.

### Unknowns
* None; decompiled activity and custom dial views verified.
