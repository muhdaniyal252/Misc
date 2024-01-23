def device_names_system(devicenames):
    devices = []
    objects = {}

    for devicename in devicenames:
        if devicename not in devices:
            devices.append(devicename)
            objects[devicename] = 0
        else:
            num = objects[devicename]
            num += 1
            devices.append(devicename + str(num))
            objects[devicename] = num

    return devices
