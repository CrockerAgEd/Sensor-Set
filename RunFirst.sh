cd ..
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install build-essential python-dev
git clone https://github.com/adafruit/Adafruit_Python_DHT.git
cd Adafruit_Python_DHT
sudo apt-get install build-essential python-dev
sudo python setup.py install
sudo python3 setup.py install
cd ..
cd Adafruit_Python_DHT
cd examples
python AdafruitDHT.py 11 20
