import os
import glob
import time

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'

device_folder1 = glob.glob(base_dir + '28*')[0]
device_file1 = device_folder1 + '/w1_slave'

device_folder2 = glob.glob(base_dir + '28*')[0]
device_file2 = device_folder2 + '/w1_slave'

device_folder3 = glob.glob(base_dir + '28*')[0]
device_file3 = device_folder3 + '/w1_slave'

device_folder4 = glob.glob(base_dir + '28*')[0]
device_file4 = device_folder4 + '/w1_slave'

def read_temp_raw():
    f1 = open(device_file1, 'r')
    lines1 = f1.readlines()
    f1.close()
    return lines

def read_temp_raw():
    f2 = open(device_file2, 'r')
    lines2 = f2.readlines()
    f2.close()
    return lines

def read_temp_raw():
    f3 = open(device_file3, 'r')
    lines3 = f3.readlines()
    f3.close()
    return lines

def read_temp_raw():
    f4 = open(device_file4, 'r')
    lines4 = f4.readlines()
    f4.close()
    return lines

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
        return temp_c1, temp_f1

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
        return temp_c2, temp_f2

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
        return temp_c3, temp_f3

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
        return temp_c4, temp_f4
	
	
	
while True:
	print("sensor 1"read_temp1()"sensor 2"read_temp2()"sensor 3"read_temp3()"sensor 4"read_temp4())	
	time.sleep(1)
