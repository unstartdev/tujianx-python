# -*- coding: UTF-8 -*-
import get
#user_agent = "tujianx-python/0x38"
piclink = ""
picid = ""
pathfnish = ""
catelist = ['杂烩', '二次元', '电脑壁纸']
catestr = "0.杂烩\n1.二次元\n2.电脑壁纸"
actlist = ['today']
print("0. 今日图片")
selectactup = int(input('Enter you want to see:'))
if selectactup == 0:
    print(catestr)
    selectcateup = int(input('Enter you want to see:'))
    get.getpicinfo(catelist[selectcateup], actlist[selectactup])
    selopen = input('要打开它吗？(Y/N)')
    if selopen == 'Y':
        get.getpicfile(piclink, picid)
        from PIL import Image
        img = Image.open(pathfnish)
        img.show()
    elif selopen == "N":
        selsave = input('单独保存它？(Y/N)')
        if selsave == "Y":
            get.getpicfile(piclink, picid)
            print(pathfnish)
        elif selsave == "N":
            import restartmodule
            selquit = input('退出或返回主菜单(Q/R)')
            if selquit == "Q":
                restartmodule.stop_program()
            elif selquit == "R":
                restartmodule.restart_program()
