import ctypes,sys

```
通过修改注册表来更改壁纸, 接受一个命令行参数
具体代码找不到了,原理如下:
```

class Main:
    def __init__(self):
        path = 'D:\卢澳\Pictures\飞火壁纸库\FFWallPaper\custom\img\ef93148c2df9ca39b3a3ddbdb6171b22.jpg'
        ctypes.windll.user32.SystemParametersInfoW(20, 0, sys.argv[1], 0)

        input()


application = Main()