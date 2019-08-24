import ctypes
import time

while True:
    GetWindowText = ctypes.windll.user32.GetWindowTextW
    GetWindowTextLength = ctypes.windll.user32.GetWindowTextLengthW
    GetForegroundWindow = ctypes.windll.user32.GetForegroundWindow
    length = GetWindowTextLength(GetForegroundWindow())
    buff = ctypes.create_unicode_buffer(length + 1)
    GetWindowText(GetForegroundWindow(), buff, length + 1)
    buff.value=buff.value.replace(" ","")
    if buff.value.strip():
        if "GoogleChrome" in buff.value:
            buff.value="GoogleChrome"
        if "MicrosoftVisualStudio" in buff.value:
            buff.value="VisualStudio"
        dict={}
        try:
            f=open("F:\Python Automation\RepliconTimeCalc.txt","r")
            for line in f:
                   (key, val) = line.split()
                   dict[key] = val
            if buff.value in dict.keys():     
                dict[buff.value] = int(dict[buff.value])+1
            else:
                dict[buff.value] = 1
            f.close()
        except FileNotFoundError:
            dict[buff.value] = 1
        f=open("F:\Python Automation\RepliconTimeCalc.txt","w+")
        for keys in dict.keys():
            f.write(keys+" "+str(dict[keys])+"\n")
        f.close()
    time.sleep(1)
