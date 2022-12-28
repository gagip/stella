pyinstaller -F main.py
pyinstaller -F --add-data="crawling_result.ui;./" result.py --hidden-import plyer.platforms.win.notification