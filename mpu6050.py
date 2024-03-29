from imu import MPU6050
import time
from machine import Pin, I2C
#raspberry pi pico üzerindeki bağlantı pinleri aşağıdadır
i2c = I2C(1, sda=Pin(18), scl=Pin(19), freq=400000) #pin seçimi yapma ve i2c portu seçme
imu = MPU6050(i2c)

while True:
    #ani ivmeyi yazdırır
    #Kullanmak için aşağıdaki yorum satırını kaldırın
    #print('Gx=',imu.gyro.x,"",'Gy=',imu.gyro.y,"",'Gz=',imu.gyro.z,"")
    
    #koordinat değişimini yazdırır
    print('Gx=',round(imu.accel.x,2),"",'Gy=',round(imu.accel.y,2),"",'Gz=',imu.accel.z,"")
    print(type(round(imu.accel.x,2)))
    
    time.sleep(0.3)
