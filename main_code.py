# -*coding:UTF-8*-
import sys
import tkinter as tk
from tkinter import Tk
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
def jingcai():
    huida=['2/8/6','2/6/8','6/2/8','6/8/2','8/6/2','8/2/6']
    def kaishi():
        score=0
        one=simpledialog.askstring('请听题！得分'+str(score),'什么最重要？')
        if one=='wifi':
            tkmessagebox.showinfo('哈哈哈哈！','恭喜你，答对了！我相信，你肯定是网上办公过！')
            score=score=1
        else:
            tkmessagebox.showerror('哈哈哈哈！','hahahha~答错了，没有WiFi你如何下载这个程序？')
            score=score+0
        twotwo=simpledialog.askstring('请听题！得分'+str(score),'孔子是著名的？')
        if twotwo=='老人家':
            tkmessagebox.showinfo('哈哈哈哈！','恭喜你，答对了！甭管什么家，老人家就对了！')
            score=score+1
        else:
            tkmessagebox.showerror('哈哈哈哈！','hahahaha~答错了，甭管什么家，老人家就对了！')
            score=score+0
        three=simpledialog.askstring('请听题！得分'+str(score),'一个人前面看有3根头发，后面看有2根头发，他jiu jing有多少根头发？（有坑）（请回答数字）')
        if three=='0':
            tkmessagebox.showinfo('哈哈哈哈！','恭喜你，答对了！jiujing，都揪浄了，没头发了！')
            score=score+1
        else:
            tkmessagebox.showerror('哈哈哈哈！','hahahaha~答错了，jiujing，都揪浄了，没头发了！')
            score=score+0
        four=simpledialog.askstring('请听题！得分'+str(score),'苹果手机为什么要叫苹果手机？')
        if four=='因为乔布斯喜欢吃苹果':
            tkmessagebox.showinfo('哈哈哈哈！','恭喜你，答对了！乔布斯喜不喜欢吃苹果我不知道，但他们家肯定有喜欢吃苹果的！')
            score=score+1
        else:
            tkmessagebox.showerror('哈哈哈哈！','hahahaha~答错了，乔布斯喜不喜欢吃苹果我不知道，但他们家肯定有喜欢吃苹果的！')
            score=score+0
        five=simpledialog.askstring('卡脖子问题！得分'+str(score),'填空：三个臭皮匠，___________。')
        if four=='臭味都一样':
            tkmessagebox.showinfo('哈哈哈哈！','恭喜你，答对了！他们都是一个皮革厂出来的！')
            score=score+1
        else:
            tkmessagebox.showerror('哈哈哈哈！','hahahaha~答错了，他们都是一个皮革厂出来的！')
            score=score+0
        six=simpledialog.askstring('请听题！得分'+str(score),'一加一等于几？（有多个答案，回答时请以以下方式回答：你好/你好（回答数字））')
        if six in huida:
            tkmessagebox.showinfo('哈哈哈哈！','恭喜你，答对了！不信拿手指头数啊！')
            score=score+1
        else:
            tkmessagebox.showerror('哈哈哈哈！','hahahaha~答错了，不信拿手指头数啊！')
            score=score+0
        tkmessagebox.showinfo('颁奖','答错了？没奖励！答对了？也没奖励！哈哈哈哈哈，没有办法我就是这么强大！')
    jingcai=Tk()
    jingcai.title("有奖竞猜（共计六题，满分6分）")
    jingcai.geometry("100x100")
    jingcailable=Label(jingcai,text='点它开始有奖竞猜↓')
    jingcailable.pack()
    jingcaibutton=Button(jingcai,text='点我~',command=kaishi)
    jingcaibutton.pack()
    jingcai.mainloop()
def guanyu():
    tkmessagebox.showinfo('关于TkOS','TkOS1.0\n制作人：zhihongwang250，\n保留一切权利!')
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
    else:
        return
def nidedaan():
    mixer.init()
    mixer.music.load("你的答案.wav")
    mixer.music.play()
    ww=tkmessagebox.askyesno('播放音乐','正在播放【你的答案】，播放完后会自动退出播放程序,点击否停止播放')
    if ww==True:
        close=1
    else:
        close=0
        mixer.music.stop()
def xiashan():
    mixer.init()
    mixer.music.load("下山.wav")
    mixer.music.play()
    cc=tkmessagebox.askyesno('播放音乐','正在播放【下山】，播放完后会自动退出播放程序,点击否停止播放')
    if cc==True:
        pass
    else:
        mixer.music.stop()
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
def one():
    tkmessagebox.showinfo('版本记录：1.0.0','可以听歌曲\n一个猜数字游戏\n计算器\n可以通过打开网页的方式查看疫情')
def two():
    tkmessagebox.showinfo('版本记录1.0.2',
    '修复一些bug\n听歌曲功能更人性化\n可打开项目的github界面\n美观了一些界面\n计算器更人性化\n可检测是否为Python2\n'+
    '搭配一个聊天区（网址https://gitter.im/TkOS10/community）')
def this():
    tkmessagebox.showinfo('版本记录1.0.6（当前版本）','新增一些小游戏\n可显示版本记录\n修改了一些计算器的代码，使其更完善')
# --------------
root = tk.Tk()
root.title("TkOS")
root.iconbitmap("tkos.ico")
menubar = Menu(root)
filemenu = tk.Menu(menubar, tearoff=0)
menubar.add_command(label='关于',command=guanyu)
root.config(menu=menubar)
mm = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='小游戏',menu=mm)
mm.add_command(label='猜数字',command=game)
mm.add_command(label='有奖竞猜小游戏',command=jingcai)
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
root.geometry("600x300")
ft = tkFont.Font(family='等线', size=30, weight=tkFont.NORMAL)
theLabel = tk.Label(root, text='     用Tk,写OS！',font=ft)
theLabel.pack()
theLabel5 = tk.Label(root, text='     TkOS1.0 1.0.6')
theLabel5.pack()
theButton = Button(text='打开项目的github界面', command=git)
theButton.pack()
theLabel4 = tk.Label(root, text='     看看作者的全部作品↑')
theLabel4.pack()
button2=Button(text='关闭所有音乐',command=closer)
button2.pack()
theLabel3 = tk.Label(root, text='     仅在播放音乐时有效')
theLabel3.pack()
button3=Button(text='去到聊天区',command=liao)
button3.pack()
theLabel2 = tk.Label(root, text='     发现了bug？现在报告↑')
theLabel2.pack()
root.config(menu=menubar)
aa = tk.Menu(menubar, tearoff=0)
aa.add_separator()
menubar.add_cascade(label='查看版本记录', menu=aa)
aa.add_command(label='查看1.0.0版本记录', command=one)
aa.add_command(label='查看1.0.2版本记录', command=two)
aa.add_command(label='查看这个版本的介绍', command=this)
root.config(menu=menubar)
aa.add_separator()
root.mainloop()