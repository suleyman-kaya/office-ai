import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)


relay_1 = 17
relay_2 = 27
relay_3 = 22
relay_4 = 26

def role_ac(relay):
        if(relay == "relay_1"): relay = relay_1
        elif(relay == "relay_2"): relay = relay_2
        elif(relay == "relay_3"): relay = relay_3
        elif(relay == "relay_4"): relay = relay_4
        else: pass
        GPIO.output(relay, GPIO.LOW)

def role_kapa(relay):
        if(relay == "relay_1"): relay = relay_1
        elif(relay == "relay_2"): relay = relay_2
        elif(relay == "relay_3"): relay = relay_3
        elif(relay == "relay_4"): relay = relay_4
        GPIO.output(relay, GPIO.HIGH)

def komut_kontrol(komut):
    try:
        komutlar = komut.split("|")
        komutlar = komutlar[1:]  # Komut numaralarını al, ilk elemanı atla.

        for komut_no in komutlar:
            komut_no = int(komut_no)
            if 1 <= komut_no <= 4:
                role_ac(f"relay_{komut_no}")
            elif 5 <= komut_no <= 8:
                role_kapa(f"relay_{komut_no - 4}")
            else:
                print(f"Geçersiz komut numarası: {komut_no}")
    except ValueError:
        print("Geçersiz komut numarası.")
    except Exception as e:
        print(f"Hata: {str(e)}")
