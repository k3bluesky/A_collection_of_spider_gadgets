import tkinter as tk

def taobao():
       import a_taobao
       
def jingdong():
       import b_jingdong

def douban():
       import c_douban_top250

def zuozhe():
       import writer

def douban_pingfen():
       import d_douban_pingfen

def gongneng():
       import gongneng

def picture():
       import e_sogou_picture

def weather():
       import f_tianqichaxun

def gedanzhuaqu():
       import g_gedanxinxi

def gedanxiazai():
       import h_gedanxiazai

root = tk.Tk()
root.title("爬虫功能菜单")
root.geometry('550x500')
frmlt_0 = tk.Frame(root,width=500, height=10)
label_1 = tk.Label(root,text = "欢迎使用爬虫工具综合菜单",width=20, height=7)
Button_1 = tk.Button(root,text = " 淘宝商品查询 ",width=20, height=1, command = taobao)
Button_2 = tk.Button(root,text = " 京东商品查询 ",width=20, height=1, command = jingdong)
Button_3 = tk.Button(root,text = "豆瓣电影排行榜",width=20, height=1, command = douban)
Button_4 = tk.Button(root,text = "豆瓣电影评分查询",width=20, height=1, command = douban_pingfen)
Button_5 = tk.Button(root,text = "搜狗图片批量下载",width=20, height=1, command = picture)
Button_6 = tk.Button(root,text = " 天气预报 ",width=20, height=1, command = weather)
Button_7 = tk.Button(root,text = " 网易云音乐推荐歌单获取 ",width=20, height=1, command = gedanzhuaqu)
Button_8 = tk.Button(root,text = " 网易云音乐歌单下载 ",width=20, height=1, command = gedanxiazai)
writer = tk.Button(root,text = "作者信息", command = zuozhe)
tips = tk.Button(root,text = "功能实现", command = gongneng)
frmlt_0.grid(row=0, column=1,padx=1,pady=3,columnspan = 3)
label_1.grid(row = 0, column = 1,columnspan = 3)
Button_1.grid(row = 1, column = 2)
Button_2.grid(row = 2, column = 2)
Button_3.grid(row = 3, column = 2)
Button_4.grid(row = 4, column = 2)
Button_5.grid(row = 5, column = 2)
Button_6.grid(row = 6, column = 2)
Button_7.grid(row = 7, column = 2)
Button_8.grid(row = 8, column = 2)
writer.grid(row = 9, column = 2)
tips.grid(row = 10, column = 2)

root.mainloop()

