from machine import Pin, SPI
import time
from sx127x import SX127x

# Initialiser SPI og LoRa
spi = SPI(1, baudrate=10000000, polarity=0, phase=0, sck=Pin(5), mosi=Pin(27), miso=Pin(19))
lora = SX127x(spi=spi, pins={'ss': Pin(18), 'reset': Pin(14), 'dio_0': Pin(26)}, parameters={'frequency': 915E6})

# Modtag besked
def on_receive(lora, payload):
    print("Received message: {}".format(payload.decode()))

lora.on_receive(on_receive)
lora.receive()

while True:
    # Loop to keep the script running
    time.sleep(1)
