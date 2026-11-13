import os
import zipfile
import shutil

tools_dir = os.path.abspath('TICKTICK_FUNCTIONAL_RESEARCH/tools')
zip_path = os.path.join(tools_dir, 'zulu17_jdk.zip')
jdk_target = os.path.join(tools_dir, 'zulu17_jdk')

if os.path.exists(zip_path) and os.path.getsize(zip_path) > 100_000_000:
    print('Extracting zulu17_jdk.zip...')
    with zipfile.ZipFile(zip_path, 'r') as z:
        z.extractall(tools_dir)
    for item in os.listdir(tools_dir):
        if item.startswith('zulu17.') and '-jdk' in item:
            source = os.path.join(tools_dir, item)
            if os.path.exists(jdk_target):
                shutil.rmtree(jdk_target)
            os.rename(source, jdk_target)
            print(f'Moved {source} to {jdk_target}')
            break
    print('Zulu 17 JDK successfully installed to:', jdk_target)
    # Check for javac and java
    javac = os.path.join(jdk_target, 'bin', 'javac.exe')
    print('javac exists:', os.path.exists(javac))
else:
    print('Zip not ready or not downloaded yet')
