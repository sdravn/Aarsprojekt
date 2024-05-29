from machine import Pin, I2C
import ssd1306
import framebuf
from time import sleep, ticks_ms

# Initialize I2C
i2c = I2C(scl=Pin(21), sda=Pin(22))  # Juster pins i henhold til din opsætning

oled = ssd1306.SSD1306_I2C(128, 64, i2c)
bitmap = bytearray(128 * 64 // 8)

pb1 = Pin(4, Pin.IN)
pb2 = Pin(0, Pin.IN)

# Scan for I2C devices
devices = i2c.scan()
if not devices:
    raise Exception("No I2C devices found")
else:
    for device in devices:
        print("I2C device found at address:", hex(device))

# Initialize SSD1306 display (adjust the address if needed)
try:
    oled = ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3C)
except ValueError as e:
    print(f"Error initializing display: {e}")
    raise e

# Load PBM files
def load_pbm(filename):
    with open(filename, 'rb') as f:
        f.readline()  # Magic number
        f.readline()  # Creator comment
        f.readline()  # Dimensions
        data = bytearray(f.read())
    return framebuf.FrameBuffer(data, 128, 64, framebuf.MONO_HLSB)

try:
    fbuf0 = load_pbm('tal/0.pbm')
    fbuf1 = load_pbm('tal/1.pbm')
    fbuf2 = load_pbm('tal/2.pbm')
    fbuf3 = load_pbm('tal/3.pbm')
    fbuf4 = load_pbm('tal/4.pbm')
    fbuf5 = load_pbm('tal/5.pbm')
    fbuf6 = load_pbm('tal/6.pbm')
    fbuf7 = load_pbm('tal/7.pbm')
    fbuf8 = load_pbm('tal/8.pbm')
    fbuf9 = load_pbm('tal/9.pbm')

    # Function to display images based on button state
    def update_display(button1_state, button2_state):
        oled.fill(0)  # Clear display
        if button1_state:
            oled.blit(fbuf1, 0, 0)
        if button2_state:
            oled.blit(fbuf9, 30, 0)
        if button2_state:
            oled.blit(fbuf2, 70, 0)
        oled.show()

    # Main loop to check button status
    while True:
        button1_state = pb1.value() == 0  # Assuming active low
        button2_state = pb2.value() == 0  # Assuming active low

        update_display(button1_state, button2_state)
        sleep(0.1)

except Exception as e:
    print(f"Error: {e}")
    raise e

