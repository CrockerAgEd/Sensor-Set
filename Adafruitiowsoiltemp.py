"""
'temp_humidity.py'
==================================
Example of sending analog sensor
values to an Adafruit IO feed.
Author(s): Brent Rubell
Tutorial Link: Tutorial Link: https://learn.adafruit.com/adafruit-io-basics-temperature-and-humidity
Dependencies:
    - Adafruit IO Python Client
        (https://github.com/adafruit/io-client-python)
    - Adafruit_Python_DHT
        (https://github.com/adafruit/Adafruit_Python_DHT)
"""

#temp probe setup
import os
import glob
import time

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'

time.sleep(0)

device_folder1 = glob.glob(base_dir + '28-01131f69*')[0]
device_file1 = device_folder1 + '/w1_slave'

device_folder2 = glob.glob(base_dir + '28-01131f98*')[0]
device_file2 = device_folder2 + '/w1_slave'

device_folder3 = glob.glob(base_dir + '28-021317d8*')[0]
device_file3 = device_folder3 + '/w1_slave'

device_folder4 = glob.glob(base_dir + '28-021317db*')[0]
device_file4 = device_folder4 + '/w1_slave'


# import adafruit dht library.
import Adafruit_DHT

# import Adafruit IO REST client.
from Adafruit_IO import Client, Feed

# Delay in-between sensor readings, in seconds.
DHT_READ_TIMEOUT = 5

# Pin connected to DHT22 data pin
DHT_DATA_PIN = 20

# Set to your Adafruit IO key.
# Remember, your key is a secret,
# so make sure not to publish it when you publish this code!
ADAFRUIT_IO_KEY = 'c907dc9fee4f4a978b830c2e126345b6'

# Set to your Adafruit IO username.
# (go to https://accounts.adafruit.com to find your username).
ADAFRUIT_IO_USERNAME = 'Mschroer'

# Create an instance of the REST client.
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

# Set up Adafruit IO Feeds.
temperature_feed = aio.feeds('temp')
humidity_feed = aio.feeds('humidity')

# Set up DHT11 Sensor.
dht11_sensor = Adafruit_DHT.DHT11

#read temp probes
def read_temp_raw1():
    f1 = open(device_file1, 'r')
    lines1 = f1.readlines()
    f1.close()
    return lines1

def read_temp_raw2():
    f2 = open(device_file2, 'r')
    lines2 = f2.readlines()
    f2.close()
    return lines2

def read_temp_raw3():
    f3 = open(device_file3, 'r')
    lines3 = f3.readlines()
    f3.close()
    return lines3

def read_temp_raw4():
    f4 = open(device_file4, 'r')
    lines4 = f4.readlines()
    f4.close()
    return lines4

def read_temp1():
    lines1 = read_temp_raw1()
    while lines1[0].strip()[-3:] != 'YES':
        time1.sleep(0.2)
        lines1 = read_temp_raw1()
    equals_pos1 = lines1[1].find('t=')
    if equals_pos1 != -1:
        temp_string1 = lines1[1][equals_pos1+2:]
        temp_c1 = float(temp_string1) / 1000.0
        temp_f1 = temp_c1 * 9.0 / 5.0 + 32.0
        return temp_f1
    
def read_temp2():
    lines2 = read_temp_raw2()
    while lines2[0].strip()[-3:] != 'YES':
        time2.sleep(0.2)
        lines2 = read_temp_raw2()
    equals_pos2 = lines2[1].find('t=')
    if equals_pos2 != -1:
        temp_string2 = lines2[1][equals_pos2+2:]
        temp_c2 = float(temp_string2) / 1000.0
        temp_f2 = temp_c2 * 9.0 / 5.0 + 32.0
        return temp_f2

def read_temp3():
    lines3 = read_temp_raw3()
    while lines3[0].strip()[-3:] != 'YES':
        time3.sleep(0.2)
        lines3 = read_temp_raw3()
    equals_pos3 = lines3[1].find('t=')
    if equals_pos3 != -1:
        temp_string3 = lines3[1][equals_pos3+2:]
        temp_c3 = float(temp_string3) / 1000.0
        temp_f3 = temp_c3 * 9.0 / 5.0 + 32.0
        return temp_f3

def read_temp4():
    lines4 = read_temp_raw4()
    while lines4[0].strip()[-3:] != 'YES':
        time4.sleep(0.2)
        lines4 = read_temp_raw4()
    equals_pos4 = lines4[1].find('t=')
    if equals_pos4 != -1:
        temp_string4 = lines4[1][equals_pos4+2:]
        temp_c4 = float(temp_string4) / 1000.0
        temp_f4 = temp_c4 * 9.0 / 5.0 + 32.0
        return temp_f4

while True:
    humidity, temperature = Adafruit_DHT.read_retry(dht11_sensor, DHT_DATA_PIN)
    if humidity is not None and temperature is not None:
        print("dhttemp = ",temperature*1.8+32,"dhthumidity = ",humidity, "probe1 =",(read_temp1()),"probe2 =",(read_temp2()),"probe3 =",(read_temp4()),"probe4 =",(read_temp4()),)
        # Send humidity and temperature feeds to Adafruit IO
    
        temperature = '%.2f'%((temperature)*1.8+32)
        humidity = '%.2f'%(humidity)


        aio.send(temperature_feed.key, str(temperature))
        aio.send(humidity_feed.key, str(humidity))
        aio.send(aio.feeds('soil-1-temp').key, str(read_temp1()))
        aio.send(aio.feeds('soil-2-temp').key, str(read_temp2()))
        aio.send(aio.feeds('soil-3-temp').key, str(read_temp3()))
        aio.send(aio.feeds('soil-4-temp').key, str(read_temp4()))
        time.sleep(0)
        
    else:
        print('Failed to get DHT11 Reading, trying again in ', DHT_READ_TIMEOUT, 'seconds')
    # Timeout to avoid flooding Adafruit IO
    time.sleep(DHT_READ_TIMEOUT)
