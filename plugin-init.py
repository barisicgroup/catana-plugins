# Python script for the initialization of new Catana plugin file (.catplg).
# Call this script without arguments to see the available options.

import json
import sys
from datetime import datetime

now = datetime.now()
ext = ".catplg"
defaultPluginName = "catana_plugin_" + now.strftime("%Y%m%d_%H%M%S")
defaultDescription = "Plugin for Catana web application"
defaultAuthor = "plugin-init script"

def get_plugin_file_structure(name, desc, author):
    return {
        # Plugin name
        # The name must be lowercase, single-word (i.e., no spaces), and may contain hyphens and underscores.
        "name": name if len(name) > 0 else defaultPluginName,
        # Plugin description
        "description": desc if len(desc) > 0 else defaultDescription,
        # Plugin version
        "version": "1.0.0",
        # Name of the plugin's author
        "author": author if len(author) > 0 else defaultAuthor,
        # URL template for retrieving files of this plugin.
        # ---
        # Released plugins (and their scripts) are expected to be located at some server (e.g., Catana's plugin repository).
        # This property describes how path for individual files will be retrieved.
        # Substring {name} will be replaced with the name of the plugin (defined in "name" field).
        # Substring {file} will be replaced with the name of the script file (defined in "scripts" field).
        # or a plugin file ("name".catplg).
        "thisUrlTemplate": "https://raw.githubusercontent.com/barisicgroup/catana-plugins/main/{name}/{file}",
        # URL template for retrieving addresses of dependencies.
        # If empty, "thisUrlTemplate" is used.
        "depsUrlTemplate": "",
        # References to scripts included in this plugin (in the form of "name.extension")
        "scripts": [],
        # Name of the script to be automatically executed when the plugin is loaded.
        # This script should be included also in the "scripts" field.
        "initScript": "",
        # Names of plugins on which this plugin depends (in the form of "name" without extension)
        "dependencies": []
    }

argv = sys.argv
argc = len(sys.argv)

print("Usage: python3 plugin-init.py plugin_name [\"plugin_description\"] [\"plugin_author\"]")
print("Arguments in [] are optional.")

if argc < 2 or (argc == 2 and argv[1] == "help"):
    exit(0)

print("===")

fileData = get_plugin_file_structure(argv[1], argv[2] if argc > 2 else "", argv[3] if argc > 3 else "")
jsonData = json.dumps(fileData, indent=4)
fileName = argv[1] + ext

file = open(fileName, "w")
file.write(jsonData)
file.close()

print("File created: " + fileName)