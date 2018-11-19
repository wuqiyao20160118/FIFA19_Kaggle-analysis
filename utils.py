import numpy as np
import pandas as pd


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


def change_bodyShape(x):
    if str(x) == "Lean":
        return 60
    elif str(x) == "Normal":
        return 80
    elif str(x) == "Stocky":
        return 90
    else:
        return x

    
def convert_value(v):
    if('M' in str(v)):
        return float(v[1:-1]) * 1e6
    elif('K' in str(v)):
        return float(v[1:-1]) * 1e3  
    elif('€0' in str(v)):
        return float(v[1:])
    else:
        return v

    
def fix_value(x):
    # evaluate sum
    if('+' in str(x).strip()):
        calc = x.split('+')
        return int(calc[0]) + int(calc[1])
    # evaluate subtraction
    elif('-' in str(x).strip()):
        calc = x.split('-')
        return int(calc[0]) + int(calc[1])
    # convert to integer if string contains a valid number
    elif str(x).strip().isdigit():
        return int(x)
    # return as it is, for example null values
    else:
         return x

        
def find_GK(preferences):
    if "GK" in preferences:
        return True
    else:
        return False


def find_CPR(preferences):
    if "China PR" in preferences:
        return True
    else:
        return False


def position_check(p):
    pos = p.split()
    # does it contain defender position
    d = any(i.strip() in defense for i in pos) 
    # does it contain midfield position
    m = any(i.strip() in midfield for i in pos)   
    # does it contain forward position
    f = any(i.strip() in forward for i in pos)  
    
    # The outer int is used to represent a binary number
    # and convert to decimal
    return int("".join([str(int(d)), str(int(m)), str(int(f))]), 2)


def extract_nations(data):
    result = []
    nation_count = {}
    for i in range(len(fifa19["Nationality"])):
        try:
            country = fifa19["Nationality"][i]
            if country == "Korea Republic":
                country = "Korea"
            elif country == "England" or country == "Wales" or country == "Scotland" or country == "Northern Ireland":
                country = "United Kingdom"
            elif country == "Republic of Ireland":
                country = "Ireland"
            elif country == "China PR" or country == "Hong Kong":
                country = "China"
            elif country == "Korea DPR":
                country = "Dem. Rep. Korea"
            elif country == 'Dominican Republic':
                country = "Dominican Rep."
            if country not in result:   
                result.append(country)
                nation_count[country] = 1
            else:
                nation_count[country] += 1
        except KeyError:
            continue
    return result, nation_count
