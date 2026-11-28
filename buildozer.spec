[app]

# Шаг 1. Указываем название приложения, отображаемое на устройстве.
title = Секретная лаборатория

# Шаг 2. Указываем техническое имя приложения (без пробелов).
package.name = secretlab

# Шаг 3. Указываем домен разработчика.
package.domain = org.student

# Шаг 4. Указываем папку, в которой находятся файлы проекта.
source.dir = .

# Шаг 5. Перечисляем типы файлов, которые необходимо включить в APK.
source.include_exts = py,png,jpg,jpeg,kv,atlas,json,db,sqlite

# Шаг 6. Указываем версию приложения.
version = 0.1

# Шаг 7. Перечисляем необходимые библиотеки и компоненты
requirements = python3,kivy,sqlite3

# Шаг 8. Дополнительно: Указываем путь к иконке приложения.
icon.filename = %(source.dir)s/icon.png

orientation = portrait
fullscreen = 0

android.archs = arm64-v8a
android.accept_sdk_license = True

p4a.branch = develop
android.api = 36
android.ndk = 29

[buildozer]

log_level = 2
warn_on_root = 1
