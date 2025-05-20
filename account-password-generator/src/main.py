# -*- coding: utf-8 -*-
"""
主程式：Account & Password Generator
功能：
1. 隨機產生密碼（可自訂長度、範圍）
2. 隨機產生ID
3. 隨機產生日文姓名（支援漢字、假名、羅馬拼音三種顯示方式）
"""

import tkinter as tk
import random
import string
from japanese_names import surnames, given_names

# 密碼生成函數
def generate_password(length, use_lowercase, use_uppercase, use_digits, use_special_chars):
    characters = ""
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation
    if not characters:
        return "請選擇至少一個選項"
    return ''.join(random.choice(characters) for _ in range(length))

# 隨機ID生成函數
def generate_id(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

# 日文姓名生成函數（只根據漢字長度過濾，三種格式對應顯示）
def generate_japanese_name_with_all_styles(target_length):
    candidates = []
    for surname in surnames:
        for given in given_names:
            kanji = f"{surname['kanji']}{given['kanji']}"
            if len(kanji) == target_length:
                kana = f"{surname['kana']} {given['kana']}"
                romaji = f"{surname['romaji']} {given['romaji']}"
                candidates.append((kanji, kana, romaji))
    if candidates:
        return random.choice(candidates)
    else:
        return None

# 更新顯示的密碼、ID或日文姓名
def generate_items():
    length = item_length.get()
    item_list.delete(0, tk.END)
    if item_type.get() == "密碼":
        use_lowercase = lowercase_var.get()
        use_uppercase = uppercase_var.get()
        use_digits = digits_var.get()
        use_special_chars = special_chars_var.get()
        for _ in range(10):
            password = generate_password(length, use_lowercase, use_uppercase, use_digits, use_special_chars)
            item_list.insert(tk.END, password)
    elif item_type.get() == "ID":
        for _ in range(10):
            random_id = generate_id(length)
            item_list.insert(tk.END, random_id)
    elif item_type.get() == "日文姓名":
        # 先取得所有可用組合
        all_candidates = []
        for surname in surnames:
            for given in given_names:
                kanji = f"{surname['kanji']}{given['kanji']}"
                if len(kanji) == length:
                    kana = f"{surname['kana']} {given['kana']}"
                    romaji = f"{surname['romaji']} {given['romaji']}"
                    all_candidates.append((surname['kanji'], kanji, kana, romaji))
        # 優先選取不同姓氏
        random.shuffle(all_candidates)
        used_surnames = set()
        results = []
        for surname_kanji, kanji, kana, romaji in all_candidates:
            if surname_kanji not in used_surnames:
                results.append((kanji, kana, romaji))
                used_surnames.add(surname_kanji)
            if len(results) >= 10:
                break
        # 若不足10組，再補齊
        if len(results) < 10:
            for surname_kanji, kanji, kana, romaji in all_candidates:
                if len(results) >= 10:
                    break
                if (kanji, kana, romaji) not in results:
                    results.append((kanji, kana, romaji))
        # 顯示結果
        if results:
            for kanji, kana, romaji in results:
                item_list.insert(tk.END, f"{kanji}　{kana}　{romaji}")
        else:
            for _ in range(10):
                item_list.insert(tk.END, "無法產生符合長度的姓名")

# 鎖定/解鎖範圍選擇框與日文姓名選項
def lock_unlock_options(*args):
    if item_type.get() == "ID":
        lowercase_checkbox.config(state=tk.DISABLED)
        uppercase_checkbox.config(state=tk.DISABLED)
        digits_checkbox.config(state=tk.DISABLED)
        special_chars_checkbox.config(state=tk.DISABLED)
    elif item_type.get() == "密碼":
        lowercase_checkbox.config(state=tk.NORMAL)
        uppercase_checkbox.config(state=tk.NORMAL)
        digits_checkbox.config(state=tk.NORMAL)
        special_chars_checkbox.config(state=tk.NORMAL)
    elif item_type.get() == "日文姓名":
        lowercase_checkbox.config(state=tk.DISABLED)
        uppercase_checkbox.config(state=tk.DISABLED)
        digits_checkbox.config(state=tk.DISABLED)
        special_chars_checkbox.config(state=tk.DISABLED)

# 設定主視窗
root = tk.Tk()
root.title("Account & Password Generator")

# 密碼/ID/姓名長度調整
item_length = tk.IntVar(value=8)
length_slider = tk.Scale(root, from_=3, to_=12, orient="horizontal", variable=item_length, label="長度")
length_slider.pack(pady=10)

# 顯示當前設定的長度
length_label = tk.Label(root, text="當前長度: 8")
length_label.pack()

def update_length_label(val):
    length_label.config(text=f"當前長度: {val}")
length_slider.config(command=update_length_label)

# 範圍選擇框（僅適用於密碼）
options_frame = tk.Frame(root)
options_frame.pack(pady=10)
lowercase_var = tk.BooleanVar(value=True)
uppercase_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
special_chars_var = tk.BooleanVar(value=True)
lowercase_checkbox = tk.Checkbutton(options_frame, text="小寫字母 (a~z)", variable=lowercase_var)
uppercase_checkbox = tk.Checkbutton(options_frame, text="大寫字母 (A~Z)", variable=uppercase_var)
digits_checkbox = tk.Checkbutton(options_frame, text="數字 (0~9)", variable=digits_var)
special_chars_checkbox = tk.Checkbutton(options_frame, text="特殊符號", variable=special_chars_var)
lowercase_checkbox.grid(row=0, column=0, padx=5)
uppercase_checkbox.grid(row=0, column=1, padx=5)
digits_checkbox.grid(row=1, column=0, padx=5)
special_chars_checkbox.grid(row=1, column=1, padx=5)

# 顯示密碼/ID/日文姓名選擇框
item_type = tk.StringVar(value="密碼")
item_type.trace_add("write", lock_unlock_options)
item_type_frame = tk.Frame(root)
item_type_frame.pack(pady=10)
password_radio = tk.Radiobutton(item_type_frame, text="密碼", variable=item_type, value="密碼")
id_radio = tk.Radiobutton(item_type_frame, text="ID", variable=item_type, value="ID")
jpname_radio = tk.Radiobutton(item_type_frame, text="日文姓名", variable=item_type, value="日文姓名")
password_radio.pack(side="left")
id_radio.pack(side="left")
jpname_radio.pack(side="left")

# 顯示密碼/ID/姓名列表
item_list = tk.Listbox(root, height=10, width=40)
item_list.pack(pady=10)

# 生成按鈕
generate_button = tk.Button(root, text="隨機生成", command=generate_items)
generate_button.pack(pady=10)

# 右鍵複製功能
def copy_item(event):
    try:
        selected_item = item_list.get(item_list.curselection())
        root.clipboard_clear()
        root.clipboard_append(selected_item)
        root.update()
    except:
        pass
item_list.bind("<Button-3>", copy_item)

# 啟動GUI介面
root.mainloop() 
