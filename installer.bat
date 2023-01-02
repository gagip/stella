pyinstaller -F --paths=./src ./src/main.py

pyinstaller -F --paths=./src ^
--add-data="./src/crawling_result.ui;./" ^
./src/result.py ^
--hidden-import plyer.platforms.win.notification

pyinstaller -F --paths=./src ./src/fashionplus.py