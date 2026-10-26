[app]
source.dir = .
version = 0.1
android.accept_sdk_license = True
# (str) Title of your application
title = Mësojmë Alfabetin

# (str) Package name
package.name = alfabeti

# (str) Package domain (needed for android packaging)
package.domain = org.alfabeti

# (list) Source files to include (let it include python files and assets)
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
# Specify python modules your app uses (e.g., kivy, etc.)
requirements = python3,kivy,cython
android.api = 33
android.minapi = 21
requirements = python3,kivy,cython
# (str) Supported orientations
orientation = portrait

# (list) Permissions
android.permissions = INTERNET

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2
