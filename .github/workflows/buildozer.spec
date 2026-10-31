[app]

# (str) Title of your application
title = Habesha Live

# (str) Package name
package.name = habeshalive

# (str) Package domain (needed for android packaging)
package.domain = org.habeshalive

# (list) Source files to include (let it empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,json

# (list) Application requirements
requirements = python3,kivy

# (str) Supported orientations
orientation = portrait

# (list) Permissions
android.permissions = INTERNET

[buildozer]
# (int) Log level (0 = error, 1 = info, 2 = debug)
log_level = 2
