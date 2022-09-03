
from tkinter import *
from tkinter.ttk import *
from crawlerhelp import crawlerHelp
import tkinter.messagebox

class Win_l6ygs29y:
    def __init__(self):
        self.root = self.__win()
        self.tk_label_frame_l6ygtwq0 = Frame_l6ygtwq0(self.root)
        self.tk_label_frame_l6ygvqwt = Frame_l6ygvqwt(self.root)

    def __win(self):
        root = Tk()
        root.title("化学品信息爬取")
        # 设置大小 居中展示
        width = 600
        height = 500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(geometry)
        root.resizable(width=False, height=False)
        return root



class Frame_l6ygtwq0:
    def __init__(self,parent):
        self.root = self.__frame(parent)
        self.tk_button_l6yguw9x = self.__tk_button_l6yguw9x()
        self.tk_label_l6yh2pkw = self.__tk_label_l6yh2pkw()
        self.tk_input_l6yh32z2 = self.__tk_input_l6yh32z2()
        self.tk_button_l6yh4flz = self.__tk_button_l6yh4flz()
        self.tk_label_l6yh58z9 = self.__tk_label_l6yh58z9()
        self.tk_input_l6yh61o9 = self.__tk_input_l6yh61o9()
        self.tk_label_l6yh69ap = self.__tk_label_l6yh69ap()
        self.tk_input_l6yh77kh = self.__tk_input_l6yh77kh()
    def __frame(self,parent):
        frame = LabelFrame(parent,text="参数设置")
        frame.place(x=10, y=10, width=580, height=113)
        return frame

    def __tk_button_l6yguw9x(self):
        btn = Button(self.root, text="开始爬取")
        btn.place(x=450, y=40, width=95, height=38)
        return btn

    def __tk_label_l6yh2pkw(self):
        label = Label(self.root,text="本地外网IP：")
        label.place(x=10, y=10, width=94, height=24)
        return label

    def __tk_input_l6yh32z2(self):
        ipt = Entry(self.root)
        ipt.place(x=110, y=10, width=110, height=24)
        return ipt

    def __tk_button_l6yh4flz(self):
        btn = Button(self.root, text="测试",command=self.TestText)
        btn.place(x=240, y=10, width=50, height=24)
        return btn

    def __tk_label_l6yh58z9(self):
        label = Label(self.root,text="爬取起止页：")
        label.place(x=10, y=50, width=113, height=26)
        return label

    def __tk_input_l6yh61o9(self):
        ipt = Entry(self.root)
        ipt.place(x=110, y=50, width=68, height=24)
        return ipt

    def __tk_label_l6yh69ap(self):
        label = Label(self.root,text="至")
        label.place(x=190, y=50, width=30, height=24)
        return label

    def __tk_input_l6yh77kh(self):
        ipt = Entry(self.root)
        ipt.place(x=220, y=50, width=68, height=24)
        return ipt

    def validate_ip(ip_str,**kwargs):
        sep = ip_str.split('.')
        if len(sep) != 4:
            return False
        for i, x in enumerate(sep):
            try:
                int_x = int(x)
                if int_x < 0 or int_x > 255:
                    return False
            except ValueError as e:
                return False
        return True

    def TestText(self):
        localIP=self.tk_input_l6yh32z2.get()
        if localIP=="" or self.tk_input_l6yh32z2.get()==None:
            tkinter.messagebox.showerror("错误", "本地外网IP不能为空！")
            return
        result=self.validate_ip(localIP)
        if result ==False:
            tkinter.messagebox.showerror("错误", "IP地址不合法！")
            return
        print(self.tk_input_l6yh32z2.get())

class Frame_l6ygvqwt:
    def __init__(self,parent):
        self.root = self.__frame(parent)
        self.tk_text_l6ygw52x = self.__tk_text_l6ygw52x()
    def __frame(self,parent):
        frame = LabelFrame(parent,text="打印信息")
        frame.place(x=10,  y=130, width=580, height=345)
        return frame

    def __tk_text_l6ygw52x(self):
        text = Text(self.root)
        text.place(x=10, y=0, width=560, height=310)
        return text

def run():
    win = Win_l6ygs29y()
    # TODO 绑定点击事件或其他逻辑处理
    win.root.mainloop()



if __name__ == "__main__":
    run()

