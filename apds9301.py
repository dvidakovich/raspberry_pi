import smbus

# Module variables
i2c_ch = 1
bus = None

# APDS-9301 address on the I2C bus
apds9301_addr = 0x39

# Register addresses
apds9301_control_reg = 0x80
apds9301_timing_reg = 0x81
apds9301_data0low_reg = 0x8C
apds9301_data1low_reg = 0x8E

# Initialize communications and turn on the APDS-9301
def init():

    global bus

    # Initialize I2C (SMBus)
    bus = smbus.SMBus(i2c_ch)

    # Read the CONTROL register (1 byte)
    val = bus.read_i2c_block_data(apds9301_addr, apds9301_control_reg, 1)

    # Set POWER to on in the CONTROL register
    val[0] = val[0] & 0b11111100
    val[0] = val[0] | 0b11

    # Enable the APDS-9301 by writing back to CONTROL register
    bus.write_i2c_block_data(apds9301_addr, apds9301_control_reg, val)

# Read light data from sensor and calculate lux
def read_lux():

    global bus

    # Read channel 0 light value and combine 2 bytes into 1 number
    val = bus.read_i2c_block_data(apds9301_addr, apds9301_data0low_reg, 2)
    ch0 = (val[1] << 8) | val[0]

    # Read channel 1 light value and combine 2 bytes into 1 number
    val = bus.read_i2c_block_data(apds9301_addr, apds9301_data1low_reg, 2)
    ch1 = (val[1] << 8) | val[0]

    # Make sure we don't divide by 0
    if ch0 == 0.0:
        return 0.0

    # Calculate ratio of ch1 and ch0
    ratio = ch1 / ch0

    # Assume we are using the default 13.7 ms integration time on the sensor
    # So, scale raw light values by 1/0.034 as per the datasheet
    ch0 *= 1 / 0.034
    ch1 *= 1 / 0.034

    # Assume we are using the default low gain setting
    # So, scale raw light values by 16 as per the datasheet
    ch0 *= 16;
    ch1 *= 16;

    # Calculate lux based on the ratio as per the datasheet
    if ratio <= 0.5:
        return (0.0304 * ch0) - ((0.062 * ch0) * ((ch1/ch0) ** 1.4))
    elif ratio <= 0.61:
        return (0.0224 * ch0) - (0.031 * ch1)
    elif ratio <= 0.8:
        return (0.0128 * ch0) - (0.0153 * ch1)
    elif ratio <= 1.3:
        return (0.00146 * ch0) - (0.00112*ch1)
    else:
        return 0.0
