def calc_value_map(self, fx_rate):
    value_map = {}
    if fx_rate != None:
        for i in [1, 10, 1000, 1000000]:
            value_map[i] = i * fx_rate
    return value_map

ccy_map = {"USD":1.07306, "SEK":11.1082, "NOK":12.4283, "GBP":0.92572}
ccy = "USD"
value_map = calc_value_map(ccy, ccy_map.get(ccy))

for value in value_map:
    print(value)
