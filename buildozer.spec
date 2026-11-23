[app]

title = Секретная лаборатория
package.name = secretlab
package.domain = org.student

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,json,db,sqlite

version = 0.1

requirements = python3,kivy,sqlite3

orientation = portrait
fullscreen = 0

icon.filename = %(source.dir)s/icon.png
android.archs = arm64-v8a
android.accept_sdk_license = True

p4a.branch = develop
android.api = 36
android.ndk = 29

[buildozer]

log_level = 2
warn_on_root = 1
