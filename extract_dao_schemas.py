import subprocess
import json
import os

daos = [
    ("ProjectDao", "com.ticktick.task.greendao.ProjectDao"),
    ("HabitDao", "com.ticktick.task.greendao.HabitDao"),
    ("HabitRecordDao", "com.ticktick.task.greendao.HabitRecordDao"),
    ("PomodoroDao", "com.ticktick.task.greendao.PomodoroDao"),
    ("ChecklistItemDao", "com.ticktick.task.greendao.ChecklistItemDao"),
    ("TagDao", "com.ticktick.task.greendao.TagDao"),
    ("ColumnDao", "com.ticktick.task.greendao.ColumnDao"),
    ("CommentDao", "com.ticktick.task.greendao.CommentDao"),
    ("AttachmentDao", "com.ticktick.task.greendao.AttachmentDao"),
    ("ReminderDao", "com.ticktick.task.greendao.ReminderDao"),
    ("MatrixProfileDao", "com.ticktick.task.greendao.MatrixProfileDao"),
    ("CalendarEventDao", "com.ticktick.task.greendao.CalendarEventDao"),
    ("CountdownDao", "com.ticktick.task.greendao.CountdownDao"),
    ("FavLocationDao", "com.ticktick.task.greendao.FavLocationDao"),
    ("FilterDao", "com.ticktick.task.greendao.FilterDao"),
]

env = os.environ.copy()
env['JAVA_HOME'] = r'D:\tick tick open source\TICKTICK_FUNCTIONAL_RESEARCH\tools\zulu17_jdk'
env['Path'] = r'D:\tick tick open source\TICKTICK_FUNCTIONAL_RESEARCH\tools\zulu17_jdk\bin;C:\Program Files\nodejs;C:\Users\Mahim\AppData\Roaming\npm;' + env.get('Path', '')
env['REA_JADX_MCP_JAR'] = r'D:\tick tick open source\TICKTICK_FUNCTIONAL_RESEARCH\tools\jadx-headless-mcp-0.7.1-all.jar'

rea_cmd = r'C:\Users\Mahim\AppData\Roaming\npm\rea.cmd'
apk_path = r'staging_apk\com.ticktick.task.apk'

results = {}

for name, fqcn in daos:
    print(f"Extracting {name}...")
    cmd = [rea_cmd, "inspect-android-method", apk_path, fqcn, "createTable", "--format", "json"]
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, env=env, timeout=40, shell=True)
        if proc.returncode == 0:
            data = json.loads(proc.stdout)
            src_text = data.get("normalized_result", {}).get("source", {}).get("text", "")
            results[name] = src_text
            print(f"Successfully extracted {name} ({len(src_text)} chars)")
        else:
            print(f"Failed {name}: {proc.stderr[:100]}")
    except Exception as e:
        print(f"Error {name}: {e}")

out_path = r"TICKTICK_FUNCTIONAL_RESEARCH\evidence\code_references\dao_create_tables.json"
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2)

print(f"Saved {len(results)} schemas to {out_path}")
