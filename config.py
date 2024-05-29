# config.py

device_config = {
    'miso': 19,   # GPIO 19
    'mosi': 27,   # GPIO 27
    'ss': 18,     # GPIO 18
    'sck': 5,     # GPIO 5
    'dio_0': 26,  # GPIO 26
    'reset': 14,  # GPIO 14
    'led': 2,     # GPIO 2 (kan justeres hvis nødvendigt)
}

app_config = {
    'loop': 200,
    'sleep': 100,
}

lora_parameters = {
    'frequency': 868E6,  # Juster frekvensen hvis nødvendigt
    'tx_power_level': 2,
    'signal_bandwidth': 125E3,
    'spreading_factor': 8,
    'coding_rate': 5,
    'preamble_length': 8,
    'implicit_header': False,
    'sync_word': 0x12,
    'enable_CRC': False,
    'invert_IQ': False,
}

wifi_config = {
    'ssid': 'KEA_Starlink',
    'password': 'KeaStarlink2023'
}
