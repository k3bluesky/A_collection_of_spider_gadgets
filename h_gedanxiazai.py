import requests
from bs4 import BeautifulSoup
import urllib.request
from lxml import html
import os
import tkinter as tk
def main():
    etree = html.etree
    now = os.getcwd()#定位当前目录
    path = now + "\下载歌单"
    if not os.path.exists(path):
        os.mkdir(path)
    headers = {
        'Referer': 'http://music.163.com/',
        'Host': 'music.163.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    }
    play_url = 'https://music.163.com/playlist?id=' + ID.get()
    s = requests.session()
    response = s.get(play_url, headers=headers).content
    s = BeautifulSoup(response, 'lxml')
    main = s.find('ul', {'class': 'f-hide'})
    print(main.find_all('a'))
    lists = []
    for music in main.find_all('a'):
        list = []
        musicUrl = 'http://music.163.com/song/media/outer/url' + music['href'][5:] + '.mp3'
        musicName = music.text
        list.append(musicName)
        list.append(musicUrl)
        lists.append(list)
    for i in lists:
        url = i[1]
        name = i[0]
        try:
            print('正在下载', name)
            text.insert('end',("正在下载", name,"\n"))
            urllib.request.urlretrieve(url, now + '/下载歌单/%s.mp3' % name)
            print('下载成功')
            text.insert('end',"下载成功\n")
        except:
            text.insert('end',"下载失败，请查看网络哦！")
    text.insert('end',"歌曲全部下载成功，请在根目录下的下载歌单中查找歌曲！\n")
            
root = tk.Toplevel()
root.title("网易云歌单歌曲批量下载")
root.geometry('720x500')
laber_0 = tk.Label(root,text = "请输入歌单ID：")
laber_1 = tk.Label(root,text = "歌单ID可在歌单链接的尾部获得，示例ID：4944138426，由于网站限制本程序只能抓取歌单前10首歌")
laber_2 = tk.Label(root,text = "由于技术限制，下载过程中界面未响应属正常现象，请耐心等待歌曲下载完毕")
laber_0.grid(row = 1, column = 0)
laber_1.grid(row = 2, column = 1)
laber_2.grid(row = 3, column = 1)
GetID = tk.Button(root, text='获取歌曲', width=10,height=2, command=main)
ID = tk.StringVar()
entryID = tk.Entry(root, textvariable = ID)
entryID.grid(row = 1,column = 1)
GetID.grid(row = 1,column = 2) 

text = tk.Text(root, height=30)
text.grid(row=4, column=0,columnspan = 4)
root.mainloop()
