
import bleak



# OTHER MAIN #

import asyncio
from bleak import BleakScanner
from bleak import BleakClient


#async def main():
async def scan():
    devices = await BleakScanner.discover()
    for d in devices:
        print(d)

address = "FF:64:F3:A6:AB:7D"
MODEL_NBR_UUID = "00002a24-0000-1000-8000-00805f9b34fb"             # is this a standard ???
BATTERY_LEVEL_UUID = "0000180f-0000-1000-8000-00805f9b34fb"
async def connect_and_read_model(address):
    async with BleakClient(address) as client:
        model_number = await client.read_gatt_char(MODEL_NBR_UUID)
        print("Model Number: {0}".format("".join(map(chr, model_number))))

async def connect_and_read_battery(address):
    async with BleakClient(address) as client:
        # battery_level = await client.read_gatt_char(BATTERY_LEVEL_UUID)
        battery_level = await client.read_gatt_descriptor(9)
        print(battery_level)
        # print("Battery level: {0}".format("".join(map(chr, model_number))))

async def read_attribute(address, attr):
    async with BleakClient(address) as client:
        # battery_level = await client.read_gatt_char(BATTERY_LEVEL_UUID)
        battery_level = await client.read_gatt_descriptor(attr)
        print(battery_level)
        # print("Battery level: {0}".format("".join(map(chr, model_number))))

async def read_attributes(address):
    async with BleakClient(address) as client:
        services = await client.get_services()
        for service in services:
            print(service)

        for i in range(1,50):
            try:
                serdesc = await client.read_gatt_char(i)
            except Exception as e:
                print(e)
            else:
                print(serdesc.decode())

        # model_number = await client.read_gatt_char(MODEL_NBR_UUID)
        # print("Model Number: {0}".format("".join(map(chr, model_number))))

if __name__ == '__main__':



    # print("Before running scan")
    # asyncio.run(scan())


    for i in range(1,12):
        try:
            asyncio.run(read_attributes(address))
        except Exception as e:
            print(e)

    for i in range(1,12):
        try:
            asyncio.run(read_attribute("FF:64:F3:A6:AB:7D",i))
        except Exception as e:
            print(e)
    try:
        asyncio.run(connect_and_read_model(address))
    except Exception as e:
            print(e)

