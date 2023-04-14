import os
import zipfile
import sys

def scanner(input_path):
    path = input_path + '/'
    mods = [name for name in os.listdir(path)
        if name.endswith('.jar') or name.endswith('.jar.disabled')]

    mcreator_mods = []
    for mod in mods:
        is_mcreator = False
        zfile = zipfile.ZipFile(path + mod, 'r')
        try:
            infolist = zfile.infolist()
            for zipinfo in infolist:
                filename = zipinfo.filename
                if "mcreator" in filename and not is_mcreator:
                    is_mcreator = True
                    mcreator_mods.append(mod)
        except Exception:
            return f"Failed to read mod {mod} in path\n{path}"

    if (not mcreator_mods):
        return "No MCreator mods were found!"

    newline = '\n'
    return f"MCreator mods were found!\n{newline.join(mcreator_mods)}"
