import time
from machine import Pin, SPI
from micropython_rfm9x import RFM9x

# Konfigurer SPI og pins
RESET = Pin(14, Pin.OUT)
CS = Pin(5, Pin.OUT)
spi = SPI(2, baudrate=1000000, polarity=0, phase=0, bits=8, firstbit=SPI.MSB, sck=Pin(18), mosi=Pin(23), miso=Pin(19))

RADIO_FREQ_MHZ = 858.0

# Initialiser RFM95 LoRa-modul
rfm9x = RFM9x(spi, CS, RESET, RADIO_FREQ_MHZ)

# Juster sendeeffekten (i dB). Standard er 13 dB, men høj effekt radios som RFM95 kan gå op til 23 dB.
rfm9x.tx_power = 23

def send_lora_data(message):
    rfm9x.send(bytes(message, 'utf-8'))
    print("Sendt:", message)

# Hovedloop
while True:
    send_lora_data("Hej fra senderen!")
    time.sleep(2)
