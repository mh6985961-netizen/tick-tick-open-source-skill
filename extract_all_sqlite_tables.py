import zipfile
import re
import json

dex_files = ['classes.dex', 'classes2.dex', 'classes3.dex']
apk_path = 'staging_apk/com.ticktick.task.apk'

tables = {}

# Match '"TableName" ("_id" INTEGER PRIMARY KEY...'
pattern = re.compile(rb'\"([a-zA-Z0-9_]+)\"\s*\(\"(_id|ID|id)\" INTEGER PRIMARY KEY.+?\);', re.DOTALL)

with zipfile.ZipFile(apk_path, 'r') as z:
    for dex_name in dex_files:
        data = z.read(dex_name)
        matches = pattern.findall(data)
        for tbl_bytes, pkey_bytes in matches:
            pass

        # Also search for all table definitions that contain ("_id" INTEGER PRIMARY KEY
        pos = 0
        while True:
            idx = data.find(b'INTEGER PRIMARY KEY', pos)
            if idx == -1:
                break
            # Look backwards for table name
            start = max(0, idx - 150)
            chunk = data[start:idx+1500]
            # Look for "TableName" ("col" INTEGER PRIMARY KEY ... );
            m = re.search(rb'\"([a-zA-Z0-9_]+)\"\s*\(\"([^\"]+)\"\s+INTEGER PRIMARY KEY.+?\);', chunk, re.DOTALL)
            if m:
                tbl_name = m.group(1).decode('utf-8', errors='ignore')
                full_stmt = m.group(0).decode('utf-8', errors='ignore')
                clean_stmt = re.sub(r'[\r\n\t]+', ' ', full_stmt)
                clean_stmt = clean_stmt.replace('\\"', '"').strip()
                sql = f"CREATE TABLE IF NOT EXISTS {clean_stmt}"
                if tbl_name not in tables or len(sql) > len(tables[tbl_name]):
                    tables[tbl_name] = sql
            pos = idx + 20

print(f"Discovered {len(tables)} SQLite table schemas:")
for t in sorted(tables.keys()):
    print(f" - {t}")

out_path = 'TICKTICK_FUNCTIONAL_RESEARCH/evidence/code_references/all_sqlite_tables.json'
with open(out_path, 'w', encoding='utf-8') as f:
    json.dump(tables, f, indent=2)

sql_out = 'TICKTICK_FUNCTIONAL_RESEARCH/evidence/code_references/schema.sql'
with open(sql_out, 'w', encoding='utf-8') as f:
    for t in sorted(tables.keys()):
        f.write(f"-- ============================================================================\n")
        f.write(f"-- Table: {t}\n")
        f.write(f"-- ============================================================================\n")
        f.write(f"{tables[t]}\n\n")

print(f"Saved {len(tables)} schemas to {sql_out}")
