perDay = {1: 333, 2: 2768, 3: 1182, 4: 90, 5: 1755, 6: 778, 7: 1911, 8: 20, 9: 1608, 10: 1541, 11: 1093, 12: 1502, 13: 207, 14: 679, 15: 780, 16: 422, 17: 636, 18: 309, 19: 358, 20: 472, 21: 2, 22: 2188, 23: 324, 24: 202, 25: 3142, 26: 1213, 27: 1097, 28: 6, 29: 23, 30: 555, 31: 1261, 32: 622, 33: 1281, 34: 896, 35: 593, 36: 1543, 37: 1871, 38: 940, 39: 2052, 40: 1081, 41: 403,
          42: 1, 43: 6, 44: 196, 45: 166, 46: 348, 47: 2462, 48: 549, 49: 352, 50: 481, 51: 1471, 52: 2336, 53: 1786, 54: 302, 56: 2, 57: 747, 58: 1454, 59: 1675, 60: 892, 61: 191, 62: 1651, 63: 1824, 64: 1098, 65: 639, 66: 1314, 67: 1346, 68: 24, 69: 1451, 70: 802, 71: 33, 72: 504, 73: 594, 74: 2501, 75: 691, 76: 937, 77: 1466, 78: 896, 79: 498, 80: 445, 81: 1883, 82: 2055, 83: 1641, 84: 452}
perMonth = {1: 21183, 2: 18801, 3: 25388, 4: 14609}          
vallist = []
def dictToList(vallist,dict):
    for k,v in dict.items():
        # print k,v
        vallist.append(v)
        # print vallist
    return (vallist)
val2 = dictToList(vallist,perDay)
print val2
vallist = []
val3 = dictToList(vallist, perMonth)
print val3