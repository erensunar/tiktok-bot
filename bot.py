


import pyautogui as py
from win32api import GetSystemMetrics
from datetime import datetime
import datetime
import mss

import os
import mss.tools
import threading
from PIL import Image
from pytesseract import pytesseract
import json


class App():
    def __init__(self):

       
        f = open("config.json")
        data = json.load(f)
        self.smallCaseX = data["smallCaseX"] #Küçük kasanın koordinatları
        self.smallCaseY = data["smallCaseY"]
        self.ss_Top_LeftX = data["SS-Top-LeftX"]
        self.ss_Top_LeftY = data["SS-Top-LeftY"]
        self.ss_Top_RightX = data["SS-Top-RightX"]
        self.ss_Top_RightY = data["SS-Top-RightY"]
        self.ss_Down_LeftX = data["SS-Down-LeftX"]
        self.ss_Down_LeftY = data["SS-Down-LeftY"]
        self.ss_Down_RightX = data["SS-Down-RightX"]
        self.ss_Down_RightY = data["SS-Down-RightY"]
        self.canCollect = data["maxToplayan"]
        self.coinValue = data["minJeton"]
        self.openButtonX = data["openButtonX"]
        self.openButtonY = data["openButtonY"]

        self.workTime = data["workTime"]
        self.stopTime = data["stopTime"]
        self.work = True

        self.lastCurrentTime = self.currentTime(day=False)
        # time.sleep(3)
        self.workThread = threading.Thread(target = self.workControl, args=(self.workTime,self.stopTime))
        self.start()
        # self.restart()
        

    

    def start(self):
        print("Program başlıyor..")
        for i in range(1,4):
            time.sleep(1)
            print(i)
        self.strategy()
    def workControl(self,runTime, stopTime):
        while True:
            for i in range(runTime):
                time.sleep(1)
            print("Program beklemeye geçiyor..")
            self.work = False

            for i in range(stopTime):
                time.sleep(1)
            print("Program çalışmaya devam ediyor..")
            self.work = True
            self.lastCurrentTime = self.currentTime(day = False)
            self.strategy()
        

    def getRemainingSeconds(self,remainingTime):
        try:    
            x = time.strptime(remainingTime.split(',')[0],'%M:%S')
            seconds= datetime.timedelta(minutes=x.tm_min,seconds=x.tm_sec).total_seconds()
            return int(seconds)
        except:
            self.strategy()
        
    # def getFullScreen(self):
    #     time.sleep(20)
    #     py.click(self.windowModeX,self.windowModeY)
    #     py.click(self.windowModeX,self.windowModeY)
    #     self.goLiveArea()

    def getScreenCenter(self):

        centerX =  GetSystemMetrics(0) / 2
        centerY = GetSystemMetrics(1) / 2
        return centerX,centerY
  

    def slideUp(self):
        centerX, centerY = self.getScreenCenter()
        py.moveTo(centerX,centerY+100)
        time.sleep(0.5)
        py.dragTo(centerX, centerY-550,duration=0.5)

    # slideUp(centerX, centerY)
    def clickCenter(self,x = 0, y= 0):
        centerX, centerY = self.getScreenCenter()
        py.click(centerX+x,centerY+y)

    def clickCase(self):
        time.sleep(2)
        py.click(self.smallCaseX,self.smallCaseY)



    # def lastCurrentTime(self):

    #     with open("log.txt", "r") as f:
    #         logs = str(f.readlines())
    #         logs = logs.split("\\n")
    #         lastCurrentTime = logs[-2].split(" ")[2])
            
    
    def restartControl(self):
        
        currentTime = datetime.datetime.now().strftime("%H:%M:%S")
        FMT = '%H:%M:%S'
        tdelta = str(datetime.datetime.strptime(currentTime, FMT) - datetime.datetime.strptime(self.lastCurrentTime, FMT))
        x = time.strptime(tdelta.split(',')[0],'%H:%M:%S')
        seconds= datetime.timedelta(minutes=x.tm_min,seconds=x.tm_sec).total_seconds()  
        return int(seconds)


    def controlCase(self):
        print("Kasa kontrol ediliyor..")
        time.sleep(3)
        try:
            if None == py.locateCenterOnScreen("control.png"):
            # if None == py.locateCenterOnScreen("follow.png") and py.locateCenterOnScreen("follow2.png") == None:
                print("Kasa bulunamadı")
                return 0
            else:
                print("Kasa bulundu.")
                return 1
        except:
            self.help()
            self.strategy()

    def currentTime(self,day=True):
        if day:
            return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        else:
            return datetime.datetime.now().strftime("%H:%M:%S")
    def deleteImage(self,caseImageName):
        os.remove(caseImageName)
    def saveLog(self,log):
        print("Kasa bilgileri yazdırılıyor.")
        currentTime =  self.currentTime(day=True)
        self.lastCurrentTime = self.currentTime(day=False)

        yazilacak = currentTime + log
        with open('log.txt', 'a') as f:
            f.write(yazilacak)
            f.write('\n')
        f.close()
    def imageToText(self,imagePath):
        print("Görüntü işleniyor")
        path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        img = Image.open(imagePath)
        pytesseract.tesseract_cmd = path_to_tesseract
        text = pytesseract.image_to_string(img)   
        text = text[:-1].split()
        print(text)
        try:
            coinValue = int(text[1])
            canCollect = int(text[text.index("kisi") - 1] )#Kişiden önce yazan yer toplayıcı sayısı
            remainingTime = text[-1]
            print(coinValue)
            print(canCollect)
            print(remainingTime)
            # self.deleteImage(imagePath)
            return (coinValue, canCollect, remainingTime)
        except:
            self.strategy()
        

    def help(self):
        self.clickCenter(+75,-400)
        self.clickCenter(+75,-400)
        self.clickCenter(+75,-400)
        self.clickCenter(+75,-400)
        time.sleep(0.5)
        self.slideUp()

    # def start(self):
        
        
    #     os.system(r'""C:\Program Files\BlueStacks_nxt\HD-Player.exe" --instance Nougat32 --hidden --cmd launchAppWithBsx --package "com.zhiliaoapp.musically""')

            
        

    

    # def stop(self):
    #     os.system("taskkill /Im HD-Player.exe" )
    #     time.sleep(3)
    #     py.click(self.closeButtonX, self.closeButtonY)

    # def restart(self):
    #     self.saveLog("Restart atılıyor.")
    #     self.stop()
        
    #     time.sleep(10)
    #     self.getFullScreen()
    
    # def goLiveArea(self):
        
    #     py.click(self.liveButtonX, self.liveButtonY)
    #     time.sleep(10)
    #     self.strategy()

    
    
    def stopWatch(self,remainingSeconds):
        for i in range(remainingSeconds+4,0,-1):
            print("Kalan süre:" + str(i))
            time.sleep(1)
        self.click = False
        self.strategy()
        
        
    def openCase(self):

        self.click = True
        x = self.openButtonX
        y = self.openButtonY
        while self.click:
            py.click(x,y)
        time.sleep(1)


    def takeCasePhoto(self):
        print("Ekran görüntüsü çekiliyor")
        top = self.ss_Top_LeftY #yukarı boşluk
        left = self.ss_Top_LeftX #s
        width = self.ss_Top_RightX - self.ss_Top_LeftX
        height = self.ss_Down_LeftY - self.ss_Top_LeftY
        with mss.mss() as sct:
            monitor = {"top": top, "left": left, "width":width, "height":height}
            output = "sandik.png".format(**monitor)
            sct_img = sct.grab(monitor)
            mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)

    # def takeViewersPhoto(self):
    #     time.sleep(3)
    #     with mss.mss() as sct:
    #         monitor = {"top":  47, "left":1160, "width":40, "height":20}
    #         output = "izleyici.png".format(**monitor)
    #         sct_img = sct.grab(monitor)
    #         mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
    #         print(output)



    def strategy(self):
        
        while self.work:
            
            self.clickCase()
            # if self.restartControl() >self.restartTime:
            #     self.restart()

            if self.controlCase() == 1:
                self.takeCasePhoto()
                coinValue, canCollect, remainingTime = self.imageToText("sandik.png")
                if remainingTime == "Ac": #Sandığın süresi bitip açamadığımız zaman pencereyi kapatıp kaydırıyor.
                    self.help()
                elif ":" in remainingTime:

                    log =" " +  str(coinValue) + " Adet jetona sahip bir kasa bulundu. " + str(canCollect) + " kişi toplayabilir. "
                    self.saveLog(log)
                    remainingSeconds = self.getRemainingSeconds(remainingTime)
                    if coinValue > self.coinValue and canCollect >= self.canCollect :
                        print("Uygun Kasa Bulundu!")
                        t1 = threading.Thread(target=self.openCase)
                        t2 = threading.Thread(target=self.stopWatch, args = (remainingSeconds ,))
                        t1.start()
                        t2.start()
                        break
                    else:
                        self.help()
                else:
                    self.help()

                
                
                
            else:
                self.help()
                time.sleep(5)
            
import time
App()