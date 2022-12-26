pyinstaller -F main.py
pyinstaller -w -F --add-data="crawling_result.ui;./" result.py