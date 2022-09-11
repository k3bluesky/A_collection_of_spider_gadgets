import tkinter as tk

root = tk.Toplevel()
root.title("功能实现")


laber_0 = tk.Label(root,text = "菜单：[作者：杨瑞冬]")
laber_1 = tk.Label(root,text = "淘宝商品查询：[作者：杨瑞冬]")
laber_2 = tk.Label(root,text = "京东商品查询：[作者：杨瑞冬]")
laber_3 = tk.Label(root,text = "豆瓣电影排行榜：[作者：李俊杰 GUI制作：杨瑞冬]")
laber_4 = tk.Label(root,text = "豆瓣电影评分查询：[作者：杨瑞冬]")
laber_5 = tk.Label(root,text = "搜狗图片批量下载：[作者：谭翔宇 GUI制作：杨瑞冬]")
laber_6 = tk.Label(root,text = "网易云歌单信息抓取：[作者：王琪 GUI制作：杨瑞冬]")
laber_7 = tk.Label(root,text = "天气查询：[作者：杨宇鹏 GUI制作：杨瑞冬]")
laber_8 = tk.Label(root,text = "网易云歌单歌曲批量下载：[作者：郑敬聪 GUI制作：杨瑞冬]")
laber_9 = tk.Label(root,text = "根目录文件名为简写拼音，序号为菜单顺序")
laber_0.grid(row = 0, column = 2)
laber_1.grid(row = 1, column = 2)
laber_2.grid(row = 2, column = 2)
laber_3.grid(row = 3, column = 2)
laber_4.grid(row = 4, column = 2)
laber_5.grid(row = 5, column = 2)
laber_6.grid(row = 6, column = 2)
laber_7.grid(row = 7, column = 2)
laber_8.grid(row = 8, column = 2)
laber_9.grid(row = 9, column = 2)

root.mainloop()
