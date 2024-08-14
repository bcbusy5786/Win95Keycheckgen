import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import threading
import time
import sys

# 用于在GUI中显示日志的函数
def log_output(text):
    output_window.configure(state='normal')  # 允许编辑
    output_window.insert(tk.END, text + '\n')
    output_window.configure(state='disabled')  # 禁止编辑
    output_window.see(tk.END)  # 自动滚动到日志窗口底部

# 定义计时器到期后的操作
def on_timeout():
    root.destroy()
    sys.exit()

# 检查密钥的函数
def check_key():
    CDKEY = entry.get()
    LENKEY = len(CDKEY)

    if LENKEY == 23:
        YEAR = CDKEY[0:3]
        DAY = CDKEY[3:5]
        SEVENKEY = CDKEY[10:17]
        try:
            int(YEAR)
            int(DAY)
            int(SEVENKEY)
        except ValueError:
            log_output("Error 2: 格式错误（无法将输入的密钥转换为可计算类型）")
            log_output('')
            return
        if int(YEAR) < 367:
            Year = True
        else:
            Year = False
        if int(DAY) >= 95 or int(DAY) <= 3:
            Day = True
        else:
            Day = False
        if int(SEVENKEY[0:1]) == 0:
            sevenkey1 = True
        else:
            sevenkey1 = False
        a = int(SEVENKEY[1:2])
        b = int(SEVENKEY[2:3])
        c = int(SEVENKEY[3:4])
        d = int(SEVENKEY[4:5])
        e = int(SEVENKEY[5:6])
        f = int(SEVENKEY[6:7])
        if (a+b+c+d+e+f) % 7 == 0:
            Sevenkey = True
        else:
            Sevenkey = False
        Jieguo = Year and Day and sevenkey1 and Sevenkey
    elif LENKEY == 11:
        THREE = CDKEY[0:3]
        SEVEN = CDKEY[4:12]
        try:
            int(THREE)
            int(SEVEN)
        except ValueError:
            log_output("Error 2: 格式错误（无法将输入的密钥转换为可计算类型）")
            log_output('')
            return
        if THREE not in {"333", "444", "555", "666", "777", "888", "999"}:
            Three = True
        else:
            Three = False
        a = int(SEVEN[1:2])
        b = int(SEVEN[2:3])
        c = int(SEVEN[3:4])
        d = int(SEVEN[4:5])
        e = int(SEVEN[5:6])
        f = int(SEVEN[6:7])
        g = int(SEVEN[0:1])
        if (a+b+c+d+e+f+g) % 7 == 0:
            Sevenkey = True
        else:
            Sevenkey = False
        Jieguo = Three and Sevenkey
    else:
        log_output('Error 1: 格式错误（密钥长度无效）')
        log_output('')
        return

    KEY = 'OSR(OEM)' if LENKEY == 23 else 'RTM'

    if Jieguo:
        log_output('检测的密钥： {}'.format(CDKEY))
        log_output('恭喜你，该密钥有效！')
        log_output('该密钥适用于 {}'.format(KEY))
        log_output('')
    else:
        log_output('检测的密钥： {}'.format(CDKEY))
        log_output('很抱歉，该密钥无效！')



# 创建主窗口
root = tk.Tk()
root.title("Key Checker with Log")

# 创建一个输入框供用户输入密钥
entry_label = tk.Label(root, text="请输入要检测的Windows 95密钥：")
entry_label.pack()

entry = tk.Entry(root, width=50)
entry.pack()

# 创建一个按钮，用户点击后会触发密钥检测
check_button = tk.Button(root, text="检查密钥", command=check_key)
check_button.pack()

# 创建一个滚动文本框用于显示日志输出
output_window = ScrolledText(root, width=70, height=15)
output_window.pack(fill=tk.BOTH, expand=True)

# 运行主事件循环
root.mainloop()
