from machine import Pin, SPI
import time
from micropython_rfm9x import *





#Lora
lora_next_time = 0
lora_interval = 5                  # send lora Data hver X sekund
###########################################################################################################################3
#ESP32 Example
RESET = Pin(14, Pin.OUT)
#spi = SPI(2, baudrate=1000000, polarity=0, phase=0, bits=8, firstbit=0, sck=Pin(5), mosi=Pin(18), miso=Pin(19))
CS = Pin(5, Pin.OUT)
#RESET = Pin(22, Pin.OUT)
spi = SPI(2, baudrate=10000, polarity=0, phase=0, bits=8, firstbit=0, sck=Pin(18), mosi=Pin(23), miso=Pin(19))

RADIO_FREQ_MHZ = 858.0
# Initialze RFM radio
rfm9x = RFM9x(spi, CS, RESET, RADIO_FREQ_MHZ)

# Note that the radio is configured in LoRa mode so you can't control sync
# word, encryption, frequency deviation, or other settings!

# You can however adjust the transmit power (in dB).  The default is 13 dB but
# high power radios like the RFM95 can go up to 23 dB:
rfm9x.tx_power = 23
# time.sleep(1)  #

def data():
    soil.read()
    sensor.measure()
    m = (max_moisture-soil.read())*100/(max_moisture-min_moisture)
    moisture = '{:.1f} %'.format(m)
    sensor_value_temp = sensor.temperature()
    sensor_value_hum = sensor.humidity()
    bat_pct = get_battery_percentage()
    values = [sensor_value_temp, sensor_value_hum, m, bat_pct]
    m = int(m + 0.5)
    return f"{sensor_value_temp},{sensor_value_hum},{m},{bat_pct}"

packet = data()
data = f"{packet}"
################################# Main
# Send a packet.  Note you can only send a packet up to 252 bytes in length.
# This is a limitation of the radio packet size, so if you need to send larger
# amounts of data you will need to break it into smaller send calls.  Each send
# call will wait for the previous one to finish before continuing.
while True:
    ##### Lora Sender
    if time.ticks_diff(time.ticks_ms(), lora_next_time) > 0 and pumpe_is_on != 1:
        rfm9x = RFM9x(spi, CS, RESET, RADIO_FREQ_MHZ)
        rfm9x.send(bytes(data, "utf-8"))
        lora_next_time = time.ticks_ms() + lora_interval* 1000
