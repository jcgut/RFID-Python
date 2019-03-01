from keyboard_alike import reader



ser = reader.Reader(0xffff, 0x0035, 84, 16, should_reset=False)
ser.initialize()
data = ser.read().strip()
ser.disconnect()

print data
