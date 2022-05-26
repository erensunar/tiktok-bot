
from tracemalloc import stop
import winsound
import json
import time
import os
import pyautogui as py
class Settings():
    def __init__(self):
        json_file_path = "config.json"
        with open("config.json", "r") as f:
            self.data = json.load(f)
        self.menu()
        f.close()
        with open("config.json", "w") as f:
            json.dump(self.data, f)
        
        print(self.data)
    def sound(self):
        frequency = 2500  # Set Frequency To 2500 Hertz
        duration = 1000  # Set Duration To 1000 ms == 1 second
        winsound.Beep(frequency, duration)

    def menu(self):
        print("1- Kasa bilgilerini düzenle\n2-Konum ayarla")
        secim = input("Seçim yapınız (1/2): ")
        if secim == "1":
            self.setCoinandCollecter()
        elif secim == "2":
            self.setSmallCase()
        else:
            print("Hatalı seçim!")
            self.menu()
    # def setLiveButton(self):
    #     print("Lütfen canlı yayın bölümüne geçmek için bulunan butona tıklayınız..")
    #     print("Bip sesini duyduktan sonra bırakabilirsiniz.")
    #     input("Hazır olduğunuzda enter tuşuna basınız.")
    #     time.sleep(3)
    #     coordinat = py.position()
    #     self.data["smallCaseX"] = coordinat[0]
    #     self.data["smallCaseY"] = coordinat[1]
    #     self.sound()
    #     self.setSmallCase()
    def setSmallCase(self):
        print("Lütfen canlı yayındaki kasa simgesinin üstüne geliniz.")
        print("Bip sesini duyduktan sonra bırakabilirsiniz.")
        input("Hazır olduğunuzda enter tuşuna basınız.")
        time.sleep(3)
        coordinat = py.position()
        self.data["smallCaseX"] = coordinat[0]
        self.data["smallCaseY"] = coordinat[1]
        self.sound()
        self.setCaseArea()

    
    def setCaseArea(self):
        print("Lütfen canlı yayında bir kasaya tıklayınız, ardından açılan pencerede sol üst köşeyi gösteriniz.")
        print("Bip sesini duyduktan sonra bırakabilirsiniz.")
        input("Hazır olduğunuzda enter tuşuna basınız.")
        time.sleep(3)
        coordinat = py.position()
        self.data["SS-Top-LeftX"] = coordinat[0]
        self.data["SS-Top-LeftY"] = coordinat[1]
        self.sound()
        print("Şimdi sağ üst köşeyi gösteriniz.")
        print("Bip sesini duyduktan sonra bırakabilirsiniz.")
        input("Hazır olduğunuzda enter tuşuna basınız.")
        time.sleep(3)
        coordinat = py.position()
        self.data["SS-Top-RightX"] = coordinat[0]
        self.data["SS-Top-RightY"] = coordinat[1]
        self.sound()
        print("Şimdi sol alt köşeyi gösteriniz.")
        print("Bip sesini duyduktan sonra bırakabilirsiniz.")
        input("Hazır olduğunuzda enter tuşuna basınız.")
        time.sleep(3)
        coordinat = py.position()
        self.data["SS-Down-LeftX"] = coordinat[0]
        self.data["SS-Down-LeftY"] = coordinat[1]
        self.sound()
        print("Şimdi sağ alt köşeyi gösteriniz.")
        print("Bip sesini duyduktan sonra bırakabilirsiniz.")
        input("Hazır olduğunuzda enter tuşuna basınız.")
        time.sleep(3)
        coordinat = py.position()
        self.data["SS-Down-RightX"] = coordinat[0]
        self.data["SS-Down-RightY"] = coordinat[1]
        self.sound()
        self.setOpenButton()
        

    # def setCloseButton(self):
    #     print("Şimdi uygulamayı kapatmak için sağ üstten çarpıya basınız.")
    #     print("Açılan penceredeki kapat butonunun üstüne geliniz.")
    #     print("Bip sesini duyduktan sonra bırakabilirsiniz.")
    #     input("Hazır olduğunuzda enter tuşuna basınız.")
    #     time.sleep(3)
    #     coordinat = py.position()
    #     self.data["closeButtonX"] = coordinat[0]
    #     self.data["closeButtonY"] = coordinat[1]
    #     self.sound()

    
    def setOpenButton(self):
        print("Şimdi kasayı açmak için tıklanan butonu gösteriniz.")
        print("Bip sesini duyduktan sonra bırakabilirsiniz.")
        input("Hazır olduğunuzda enter tuşuna basınız.")
        time.sleep(3)
        coordinat = py.position()
        self.data["openButtonX"] = coordinat[0]
        self.data["openButtonY"] = coordinat[1]
        self.sound()
        # json_dump(self.data,"config.json")
        
    # def setWindowMode(self):
    #     print("Şimdi tam ekran yapmamız için pencereyi uzatın ve ortalayın.")
    #     print("Ve çift tıklayınca tam ekran olacağı şekilde bir konumda bekleyiniz..")
    #     print("Bip sesini duyduktan sonra bırakabilirsiniz.")
    #     input("Hazır olduğunuzda enter tuşuna basınız.")
    #     time.sleep(3)
    #     coordinat = py.position()
    #     self.data["windowModeX"] = coordinat[0]
    #     self.data["windowModeY"] = coordinat[1]
    #     self.sound()
    #     self.setLiveButton()

    def setCoinandCollecter(self):
        jeton = int(input("Kasada beklediğiniz minimum jeton sayısını giriniz: "))
        collecter = int(input("Kasadan beklediğin en fazla toplayıcı sayısını giriniz: "))
        workTime = int(input("Saniye cinsinden programın ne kadar çalışacağını giriniz: "))
        stopTime = int(input("Saniye cinsinden programın ne kadar bekleyeceğini giriniz: "))
        self.data["workTime"] = workTime
        self.data["stopTime"] = stopTime
        self.data["minJeton"] = jeton
        self.data["maxToplayan"] = collecter
        
    
Settings()