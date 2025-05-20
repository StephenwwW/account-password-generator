# Account & Password Generator 帳號密碼產生器

## 專案簡介 | Project Introduction

本專案是一個圖形化帳號、密碼與日文姓名產生器，支援自訂密碼規則、隨機ID與日文姓名（漢字、假名、羅馬拼音）。
This project is a GUI tool for generating random accounts, passwords, and Japanese names (Kanji, Kana, Romaji), with customizable password rules.

## 功能特色 | Features
- 隨機產生密碼（可自訂長度、範圍）
- 隨機產生ID
- 隨機產生日文姓名（同時顯示漢字、假名、羅馬拼音三種對應格式）
- 介面與註解皆為繁體中文，方便維護

## 安裝方式 | Installation
1. 下載本專案原始碼
2. 安裝 Python 3.x
3. 安裝必要套件（tkinter 通常隨 Python 內建）
   ```bash
   pip install -r requirements.txt
   ```

## 執行方式 | Usage
```bash
python src/main.py
```

## 檔案結構 | File Structure
```
account-password-generator/
├── README.md
├── LICENSE
├── .gitignore
├── requirements.txt
├── images/
│   └── screenshot.png
└── src/
    ├── main.py
    └── japanese_names.py
```

## License
MIT 
