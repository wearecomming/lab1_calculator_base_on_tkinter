import tkinter as tk  #引用tkinter库以进行GUI编辑
import unicodeit
import numpy as np
import math
window = tk.Tk()
window.title("Calculator")

#居中显示#
sw = window.winfo_screenwidth()  #宽度
sh = window.winfo_screenheight()
ww = 500
wh = 500
x = (sw-ww) / 2
y = (sh-wh) / 2
window.geometry("%dx%d+%d+%d" %(ww,wh,x,y)) 


window.attributes("-alpha", 0.9)
window["background"] = "black"
#设定window的背景，颜色，透明度

font1=("黑体",25)
font2 = ("黑体", 15)
font3=("黑体",20)
#定义两个之后会用到的字体格式，一个为结果行字体font1，一个为按键字体font2

res_all = tk.StringVar()#总结果
res_all.set("")
res_back= tk.StringVar()#隐藏计算式
res_back.set("")
#创建变量res，使得最后结果行能够随着按键的输入而变化

label = tk.Label(window, textvariable=res_all, height=2,font=font1,fg="white", bg="black", width=27, justify=tk.LEFT, anchor=tk.SE).grid(row=1, column=1, columnspan=5)
#总结果行

button_2nd = tk.Button(window, text="2nd", width=5, font=font2, fg="white",relief=tk.FLAT, bg="grey")
button_pai = tk.Button(window, text="π", width=5, font=font2, fg="white",relief=tk.FLAT, bg="grey")
button_e = tk.Button(window, text="e", width=5, font=font2, fg="white",relief=tk.FLAT, bg="grey")
button_C = tk.Button(window, text="C", width=5, font=font2, fg="white",relief=tk.FLAT, bg="grey")
button_back = tk.Button(window, text="⬅", width=5, font=font2, fg="white",relief=tk.FLAT, bg="grey")
button_2nd.grid(row=2, column=1, padx=3, pady=2)
button_pai.grid(row=2, column=2, padx=3, pady=2)
button_e.grid(row=2, column=3, padx=3, pady=2)
button_C.grid(row=2, column=4, padx=3, pady=2)
button_back.grid(row=2, column=5, padx=3, pady=2)

button_sin = tk.Button(window, text="sin", width=5, font=font2, fg="white",relief=tk.FLAT, bg="grey")
button_lc = tk.Button(window, text="(", width=5, font=font2, fg="white",relief=tk.FLAT, bg="grey")
button_rc = tk.Button(window, text=")", width=5, font=font2, fg="white",relief=tk.FLAT, bg="grey")
button_pow = tk.Button(window, text=unicodeit.replace("x^y"), width=5, font=font2, fg="white",relief=tk.FLAT, bg="grey")
button_div = tk.Button(window, text="÷", width=5, font=font2, fg="white",relief=tk.FLAT, bg="grey")
button_sin.grid(row=3, column=1, padx=3, pady=2)
button_lc.grid(row=3, column=2, padx=3, pady=2)
button_rc.grid(row=3, column=3, padx=3, pady=2)
button_pow.grid(row=3, column=4, padx=3, pady=2)
button_div.grid(row=3, column=5, padx=3, pady=2)



button_cos = tk.Button(window, text="cos", width=5, font=font2, fg="white",relief=tk.FLAT, bg="grey")
button_7 = tk.Button(window, text="7", width=5, font=font2, fg="white",relief=tk.FLAT, bg="grey")
button_8 = tk.Button(window, text="8", width=5, font=font2, fg="white",relief=tk.FLAT, bg="grey")
button_9 = tk.Button(window, text="9", width=5, font=font2, fg="white",relief=tk.FLAT, bg="grey")
button_mul = tk.Button(window, text="×", width=5, font=font2, fg="white",relief=tk.FLAT, bg="grey")
button_cos.grid(row=4, column=1, padx=3, pady=2)
button_7.grid(row=4, column=2, padx=3, pady=2)
button_8.grid(row=4, column=3, padx=3, pady=2)
button_9.grid(row=4, column=4, padx=3, pady=2)
button_mul.grid(row=4, column=5, padx=3, pady=2)



button_tan = tk.Button(window, text="tan", width=5, font=font2, fg="white",relief=tk.FLAT, bg="grey")
button_4 = tk.Button(window, text="4", width=5, font=font2, fg="white",relief=tk.FLAT, bg="grey")
button_5 = tk.Button(window, text="5", width=5, font=font2, fg="white",relief=tk.FLAT, bg="grey")
button_6 = tk.Button(window, text="6", width=5, font=font2, fg="white",relief=tk.FLAT, bg="grey")
button_dec = tk.Button(window, text="-", width=5, font=font2, fg="white",relief=tk.FLAT, bg="grey")
button_tan.grid(row=5, column=1, padx=3, pady=2)
button_4.grid(row=5, column=2, padx=3, pady=2)
button_5.grid(row=5, column=3, padx=3, pady=2)
button_6.grid(row=5, column=4, padx=3, pady=2)
button_dec.grid(row=5, column=5, padx=3, pady=2)


button_sec = tk.Button(window, text="sec", width=5, font=font2, fg="white",relief=tk.FLAT, bg="grey")
button_1 = tk.Button(window, text="1", width=5, font=font2, fg="white",relief=tk.FLAT, bg="grey")
button_2 = tk.Button(window, text="2", width=5, font=font2, fg="white",relief=tk.FLAT, bg="grey")
button_3 = tk.Button(window, text="3", width=5, font=font2, fg="white",relief=tk.FLAT, bg="grey")
button_plu = tk.Button(window, text="+", width=5, font=font2, fg="white",relief=tk.FLAT, bg="grey")
button_sec.grid(row=6, column=1, padx=3, pady=2)
button_1.grid(row=6, column=2, padx=3, pady=2)
button_2.grid(row=6, column=3, padx=3, pady=2)
button_3.grid(row=6, column=4, padx=3, pady=2)
button_plu.grid(row=6, column=5, padx=3, pady=2)


button_cot = tk.Button(window, text="cot", width=5, font=font2, fg="white",relief=tk.FLAT, bg="grey")
button_np = tk.Button(window, text="n!", width=5, font=font2, fg="white",relief=tk.FLAT, bg="grey")
button_0 = tk.Button(window, text="0", width=5, font=font2, fg="white",relief=tk.FLAT, bg="grey")
button_dot = tk.Button(window, text=".", width=5, font=font2, fg="white",relief=tk.FLAT, bg="grey")
button_equ = tk.Button(window, text="=", width=5, font=font2, fg="white",relief=tk.FLAT, bg="grey")
button_cot.grid(row=7, column=1, padx=3, pady=2)
button_np.grid(row=7, column=2, padx=3, pady=2)
button_0.grid(row=7, column=3, padx=3, pady=2)
button_dot.grid(row=7, column=4, padx=3, pady=2)
button_equ.grid(row=7, column=5, padx=3, pady=2)


state=0
def change_power():
    global state
    if state==0:
        button_2nd.config(fg='white',bg='blue')
        button_sin.config(text=unicodeit.replace("sin^{-1}"))
        button_cos.config(text=unicodeit.replace("cos^{-1}"))
        button_tan.config(text=unicodeit.replace("tan^{-1}"))
        button_sec.config(text=unicodeit.replace("sec^{-1}"))
        button_cot.config(text=unicodeit.replace("cot^{-1}"))
        state=1
    else:
        button_2nd.config(fg='white',bg='grey')
        button_sin.config(text="sin")
        button_cos.config(text="cos")
        button_tan.config(text="tan")
        button_sec.config(text="sec")
        button_cot.config(text="cot")
        state=0


clack=0
def buttonclick(x1,x2):
    global clack
    if clack==1:
        res_back.set("")
        res_all.set("")
        clack=0
    b=res_all.get()
    if len(b)>=25:return
    c=res_back.get()
    res_back.set(c+x2)
    res_all.set(b+x1)

def clear():
    res_back.set("")
    res_all.set("")

def back():
    global clack
    if clack==1:
        res_back.set("")
        res_all.set("")
        clack=0
    b=res_all.get()
    if len(b)>=25:return
    c=res_back.get()
    res_back.set(c[0:-1])
    res_all.set(b[0:-1])
    
def buttonclick_tr(x):
    global clack
    if clack==1:
        res_back.set("")
        res_all.set("")
        clack=0
    ans1=""
    ans2=""
    b=res_all.get()
    if len(b)>=25:return
    c=res_back.get()
    global state
    if state==0:
        if x==1:
            ans1=ans1+'sin('
            ans2=ans2+'np.sin(np.pi/180*'
        if x==2:
            ans1=ans1+'cos('
            ans2=ans2+'np.cos(np.pi/180*'
        if x==3:
            ans1=ans1+'tan('
            ans2=ans2+'np.tan(np.pi/180*'           
        if x==4:
            ans1=ans1+'sec('
            ans2=ans2+'np.sec(np.pi/180*'
        if x==5:
            ans1=ans1+'cot('
            ans2=ans2+'np.cot(np.pi/180*'
    else:
        if x==1:
            ans1=ans1+unicodeit.replace("sin^{-1}(")
            ans2=ans2+'180/np.pi*np.arcsin('
        if x==2:
            ans1=ans1+unicodeit.replace("cos^{-1}(")
            ans2=ans2+'180/np.pi*np.arccos('
        if x==3:
            ans1=ans1+unicodeit.replace("tan^{-1}(")
            ans2=ans2+'180/np.pi*np.arctan('           
        if x==4:
            ans1=ans1+unicodeit.replace("sec^{-1}(")
            ans2=ans2+'180/np.pi*np.arcsec('
        if x==5:
            ans1=ans1+unicodeit.replace("cot^{-1}(")
            ans2=ans2+'180/np.pi*np.arccot('
    res_back.set(c+ans2)
    res_all.set(b+ans1)
    
def buttonclick_fac():
    global clack
    if clack==1:
        res_back.set("")
        res_all.set("")
        clack=0
    b=res_all.get()
    if len(b)>=25:return
    c=res_back.get()
    res_all.set(b+'!')
    i=len(b)-1
    now=""
    while i>=0 and b[i]<='9' and b[i]>='0':
        now=b[i]+now
        i=i-1
    res_back.set(c[0:i]+"math.factorial("+now+")")
    

def eqa():
    global clack
    b=res_all.get()
    c=res_back.get()
    try:
        ans = eval(c) 
        x=str(ans)
        if len(x)>25:x=x[0:25]
        res_all.set(x)
        res_back.set(x)
    except (ZeroDivisionError): 
        res_all.set(str('Error: 除零错误'))
    except NameError:
        res_all.set(str('Error: 请加上括号'))
    except SyntaxError:
        res_all.set(str('Error: 语法错误，请正确输入'))
    clack=1
    
button_2nd.config(command=lambda: change_power())
button_pai.config(command=lambda: buttonclick("π","np.pi"))
button_e.config(command=lambda: buttonclick("e","np.exp(1)"))
button_C.config(command=lambda: clear())
button_back.config(command=lambda: back())
button_sin.config(command=lambda: buttonclick_tr(1))
button_lc.config(command=lambda: buttonclick("(","("))
button_rc.config(command=lambda: buttonclick(")",")"))
button_pow.config(command=lambda: buttonclick("^","**"))
button_div.config(command=lambda: buttonclick("÷","/"))
button_cos.config(command=lambda: buttonclick_tr(2))
button_7.config(command=lambda: buttonclick("7","7"))
button_8.config(command=lambda: buttonclick("8","8"))
button_9.config(command=lambda: buttonclick("9","9"))
button_mul.config(command=lambda: buttonclick("×","*"))
button_tan.config(command=lambda: buttonclick_tr(3))
button_4.config(command=lambda: buttonclick("4","4"))
button_5.config(command=lambda: buttonclick("5","5"))
button_6.config(command=lambda: buttonclick("6","6"))
button_dec.config(command=lambda: buttonclick("-","-"))
button_sec.config(command=lambda: buttonclick_tr(4))
button_3.config(command=lambda: buttonclick("3","3"))
button_2.config(command=lambda: buttonclick("2","2"))
button_1.config(command=lambda: buttonclick("1","1"))
button_plu.config(command=lambda: buttonclick("+","+"))
button_sec.config(command=lambda: buttonclick_tr(5))
button_np.config(command=lambda: buttonclick_fac())
button_0.config(command=lambda: buttonclick("0","0"))
button_dot.config(command=lambda: buttonclick(".","."))
button_equ.config(command=lambda: eqa())

window.mainloop()