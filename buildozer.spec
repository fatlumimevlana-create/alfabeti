[app]

# (str) Title of your application
title = Mësojmë Alfabetin

# (str) Package name
package.name = alfabeti

# (str) Package domain (needed for android packaging)
package.domain = org.alfabeti

# (str) Source directory where the app lives
source.dir = .

# (list) Source files to include (let it include python files and assets)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning
version = 0.1

# (list) Application requirements
# Specify python modules your app uses (e.g., kivy, etc.)
requirements = python3,kivy,

# (str) Supported orientations
orientation = portrait

# (list) Permissions
android.permissions = INTERNET

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android SDK license agreement ('True' to accept)
android.accept_sdk_license = True

# (list) Architectures to build for
android.archs = arm64-v8a

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2
