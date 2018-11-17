import numpy as np


def decode_position(data):
    result = np.zeros(data.shape, dtype=object)
    length = data.shape[0]
    for i in range(length):
        position = data[i]
        if position == 0:
            result[i] = "CB"
        elif position == 1:
            result[i] = "LCB"
        elif position == 2:
            result[i] = "RCB"
        elif position == 3:
            result[i] = "LB"
        elif position == 4:
            result[i] = "RB"
        elif position == 5:
            result[i] = "LWB"
        elif position == 6:
            result[i] = "RWB"
        elif position == 7:
            result[i] = "CDM"
        elif position == 8:
            result[i] = "LDM"
        elif position == 9:
            result[i] = "RDM"
        elif position == 10:
            result[i] = "CM"
        elif position == 11:
            result[i] = "LCM"
        elif position == 12:
            result[i] = "RCM"
        elif position == 13:
            result[i] = "CAM"
        elif position == 14:
            result[i] = "LAM"
        elif position == 15:
            result[i] = "RAM"
        elif position == 16:
            result[i] = "LM"
        elif position ==17:
            result[i] = "RM"
        elif position == 18:
            result[i] = "LW"
        elif position == 19:
            result[i] = "RW"
        elif position == 20:
            result[i] = "RW"
        elif position == 21:
            result[i] = "LF"
        elif position == 22:
            result[i] = "RF"
        elif position == 23:
            result[i] = "LS"
        elif position == 24:
            result[i] = "RS"
        elif position == 25:
            result[i] = "ST"
    return result


def encode_position(data):
    result = np.zeros(data.shape)
    length = data.shape[0]
    for i in range(length):
        position = data[i]
        if position == "CB":
            result[i] = 0
        elif position == "LCB":
            result[i] = 1
        elif position == "RCB":
            result[i] = 2
        elif position == "LB":
            result[i] = 3
        elif position == "RB":
            result[i] = 4
        elif position == "LWB":
            result[i] = 5
        elif position == "RWB":
            result[i] = 6
        elif position == "CDM":
            result[i] = 7
        elif position == "LDM":
            result[i] = 8
        elif position == "RDM":
            result[i] = 9
        elif position == "CM":
            result[i] = 10
        elif position == "LCM":
            result[i] = 11
        elif position == "RCM":
            result[i] = 12
        elif position == "CAM":
            result[i] = 13
        elif position == "LAM":
            result[i] = 14
        elif position == "RAM":
            result[i] = 15
        elif position == "LM":
            result[i] = 16
        elif position == "RM":
            result[i] = 17
        elif position == "LW":
            result[i] = 18
        elif position == "RW":
            result[i] = 19
        elif position == "RW":
            result[i] = 20
        elif position == "LF":
            result[i] = 21
        elif position == "RF":
            result[i] = 22
        elif position == "LS":
            result[i] = 23
        elif position == "RS":
            result[i] = 24
        elif position == "ST":
            result[i] = 25
    return result
