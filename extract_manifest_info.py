import sys
import json
from lxml import etree
from pyaxmlparser import APK

apk_path = 'staging_apk/com.ticktick.task.apk'
apk = APK(apk_path)

print(f"Package: {apk.package}")
print(f"Version Name: {apk.version_name}")
print(f"Version Code: {apk.version_code}")
print(f"Min SDK: {apk.get_min_sdk_version()}")
print(f"Target SDK: {apk.get_target_sdk_version()}")

xml_elem = apk.get_android_manifest_xml()
if xml_elem is not None:
    pretty_xml = etree.tostring(xml_elem, pretty_print=True, encoding='utf-8').decode('utf-8')
    with open("TICKTICK_FUNCTIONAL_RESEARCH/evidence/manifest/AndroidManifest_pretty.xml", "w", encoding="utf-8") as f:
        f.write(pretty_xml)
    print("Saved AndroidManifest_pretty.xml (length:", len(pretty_xml), "bytes)")

activities = apk.get_activities()
services = apk.get_services()
receivers = apk.get_receivers()
providers = apk.get_providers()
permissions = apk.get_permissions()

overview_data = {
    "package": apk.package,
    "version_name": apk.version_name,
    "version_code": apk.version_code,
    "min_sdk": apk.get_min_sdk_version(),
    "target_sdk": apk.get_target_sdk_version(),
    "activities_count": len(activities),
    "services_count": len(services),
    "receivers_count": len(receivers),
    "providers_count": len(providers),
    "permissions_count": len(permissions),
    "activities": activities,
    "services": services,
    "receivers": receivers,
    "providers": providers,
    "permissions": permissions,
}

with open("TICKTICK_FUNCTIONAL_RESEARCH/evidence/manifest/manifest_summary.json", "w", encoding="utf-8") as f:
    json.dump(overview_data, f, indent=2)

print("Saved manifest_summary.json with counts:")
print(f"Activities: {len(activities)}")
print(f"Services: {len(services)}")
print(f"Receivers: {len(receivers)}")
print(f"Providers: {len(providers)}")
print(f"Permissions: {len(permissions)}")
