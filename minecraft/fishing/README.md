# How to use

## Prerequisites
### On linux (only on x11 for now)
```
pip install pyautogui pytesseract pillow
sudo apt instal tesseract-ocr xdotool # On Debian/Ubuntu based systems
sudo pacman -Sy tesseract xdotool # On arch based systems
```
## On Windows
This script currently doesn't work on windows. The thing with pyautogui is that after (while ?) right clicking , it centers the cursor, meaning that in game you will be looking above or right at your feet, so the facing (fishing ?) direction will not be preserved.
To get tesseract, follow this link : https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-v5.3.0.20221214.exe

### TODO : Figure out how to make it work.

## How to run

-> Just download this script

-> Run something like :
```
python3 auto-fisher.py
```
