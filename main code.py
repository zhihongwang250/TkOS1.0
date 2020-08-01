# -*coding:UTF-8*-
import sys
import tkinter as tk
from tkinter import Menu
from tkinter import messagebox as tkmessagebox
from tkinter import simpledialog
from tkinter import PhotoImage
from tkinter import Label
from pygame import mixer
import tkinter.font as tkFont
from tkinter import Button
import sys
import time
import random # 猜数字模块要用到
import webbrowser
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
# --------------
ran=0
m=0
a=0
b=0
ca=0
guo=0
close=0
# -------------
def guanyu():
    tkmessagebox.showinfo('关于TkOS','TkOS1.0  制作人：zhihongwang250，保留一切权利!')
def gameing():
    ran=random.randrange(15)
    for i in range(6):
        ans=simpledialog.askstring('猜数字游戏','请猜一个1到15的数字：')
        if ans==ran:
            tkmessagebox.showinfo('猜数字游戏','恭喜你，猜对了！游戏结束！')
            break
        else:
            tkmessagebox.showwarning('猜数字游戏','你猜错了，点击【确定】，再猜一次!')
            continue
    tkmessagebox.showinfo('猜数字游戏','数字是'+str(ran)+',加油！')
def game():
    kaishi=tkmessagebox.askyesno('猜数字游戏','确定要开始游戏吗？')
    if kaishi==True:
        gameing()
def nidedaan():
    pygame.mixer.init()
    pygame.mixer.music.load("你的答案.wav")
    pygame.mixer.music.play()
    ww=tkmessagebox.askyesno('播放音乐','正在播放【你的答案】，播放完后会自动退出播放程序,点击否停止播放')
    if ww==True:
        close=1
    else:
        close=0
        pygame.mixer.music.stop()
def xiashan():
    pygame.mixer.init()
    pygame.mixer.music.load("下山.wav")
    pygame.mixer.music.play()
    cc=tkmessagebox.askyesno('播放音乐','正在播放【下山】，播放完后会自动退出播放程序,点击否停止播放')
    if cc==True:
        pass
    else:
        pygame.mixer.music.stop()
def git():
    webbrowser.open('https://github.com/zhihongwang250/TkOS1.0')
def china():
    webbrowser.open('https://voice.baidu.com/act/newpneumonia/newpneumonia')
def us():
    webbrowser.open('https://voice.baidu.com/act/newpneumonia/newpneumonia?city=%E7%BE%8E%E5%9B%BD-%E7%BE%8E%E5%9B%BD')
def brazil():
    webbrowser.open('https://voice.baidu.com/act/newpneumonia/newpneumonia?city=%E5%B7%B4%E8%A5%BF-%E5%B7%B4%E8%A5%BF')
def india():
    webbrowser.open('https://voice.baidu.com/act/newpneumonia/newpneumonia?city=%E5%8D%B0%E5%BA%A6-%E5%8D%B0%E5%BA%A6')
def jisuanqi():
    while True:
        number = simpledialog.askstring('计算器','请输入数学表达式 (按ctrl+c结束): ')
        if not number:
            return
        try:
            tkmessagebox.showinfo('计算结果是：',eval(number)) # 计算数字 eval
            break
        except Exception:
            tkmessagebox.showerror('请注意！','表达式出现错误')
        finally:
            print('\n')
def closer():
    mixer.music.stop()
def liao():
    webbrowser.open('https://gitter.im/TkOS10/community')
# --------------
root = tk.Tk()
root.title("TkOS")
root.iconbitmap("tkos.ico")
menubar = Menu(root)
filemenu = tk.Menu(menubar, tearoff=0)
menubar.add_command(label='关于',command=guanyu)
root.config(menu=menubar)
menubar.add_command(label='猜数字游戏',command=game)
root.config(menu=menubar)
menubar.add_command(label='简易计算器',command=jisuanqi)
root.config(menu=menubar)
filemenu.add_separator()
menubar.add_cascade(label='播放音乐', menu=filemenu)
filemenu.add_command(label='你的答案', command=nidedaan)
filemenu.add_command(label='下山', command=xiashan)
root.config(menu=menubar)
bb = tk.Menu(menubar, tearoff=0)
bb.add_separator()
menubar.add_cascade(label='查看疫情', menu=bb)
bb.add_command(label='查看中国疫情', command=china)
bb.add_command(label='查看美国疫情', command=us)
bb.add_command(label='查看巴西疫情', command=brazil)
bb.add_command(label='查看印度疫情', command=india)
root.config(menu=menubar)
bb.add_separator()
root.config(menu=menubar)
root.geometry("400x200")
ft = tkFont.Font(family='等线', size=30, weight=tkFont.NORMAL)
theLabel = tk.Label(root, text='     用Tk,写OS！',font=ft)
theLabel.pack()
theButton = Button(text='打开项目的github界面', command=git)
theButton.pack()
button2=Button(text='关闭所有音乐',command=closer)
button2.pack()
button3=Button(text='去到聊天区',command=liao)
button3.pack()
root.mainloop()