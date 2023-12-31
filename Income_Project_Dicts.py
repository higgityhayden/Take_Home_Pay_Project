#Current Data
fed_tax_dict = {'Single': [[0.1, 11000], [.12, 44725], [.22, 95375],
                           [.24, 182100], [.32, 231250], [.35, 578125], [0.37, 90000000000]]}


#Data from three years ago
                #[[percentage of income up to this value], [percentage of income beyond previous brackets]]
state_tax_dict = {'AL': [[0.02, 500.0], [0.04, 2500.0], [0.05, 90000000]],
            'AK': [[0.0, 90000000]],
            'AZ': [[0.0259, 26500.0], [0.0334, 26500.0], [0.0417, 106000.0], [0.045, 90000000]],
            'AR': [[0.02, 4000.0], [0.04, 4000.0], [0.059, 71300.0], [0.066, 90000000]],
            'CA': [[0.01, 8809.0], [0.02, 12074.0], [0.04, 12077.0], [0.06, 12793.0], [0.08, 12071.0], [0.093, 237549.0], [0.103, 59072.0], [0.113, 236297.0], [0.123, 409258.0], [0.133, 90000000]],
            'CO': [[0.0463, 90000000]],
            'CT': [[0.03, 10000.0], [0.05, 40000.0], [0.055, 50000.0], [0.06, 100000.0], [0.065, 50000.0], [0.069, 250000.0], [0.0699, 90000000]],
            'DE': [[0.022, 3000.0], [0.039, 5000.0], [0.048, 10000.0], [0.052, 5000.0], [0.0555, 35000.0], [0.066, 90000000]],
            'FL': [[0.0, 90000000]],
            'GA': [[0.01, 750.0], [0.02, 1500.0], [0.03, 1500.0], [0.04, 1500.0], [0.05, 1750.0], [0.0575, 90000000]],
            'HI': [[0.014, 2400.0], [0.032, 2400.0], [0.055, 4800.0], [0.064, 4800.0], [0.068, 4800.0], [0.072, 4800.0], [0.076, 12000.0], [0.079, 12000.0], [0.0825, 102000.0], [0.09, 25000.0], [0.1, 25000.0], [0.11, 90000000]],
            'ID': [[0.0112, 1541.0], [0.0312, 1540.0], [0.0362, 1541.0], [0.0462, 1540.0], [0.0562, 1541.0], [0.0662, 3851.0], [0.06924999999999999, 90000000]],
            'IL': [[0.0495, 90000000]],
            'IN': [[0.0323, 90000000]],
            'IA': [[0.0033, 1638.0], [0.0067, 1638.0], [0.0225, 3276.0], [0.0414, 8190.0], [0.0563, 9828.0], [0.0596, 8190.0], [0.0625, 16380.0], [0.0744, 24570.0], [0.08529999999999999, 90000000]],
            'KS': [[0.031, 15000.0], [0.0525, 15000.0], [0.057, 90000000]],
            'KY': [[0.05, 90000000]],
            'LA': [[0.02, 12500.0], [0.04, 37500.0], [0.06, 90000000]],
            'ME': [[0.058, 22200.0], [0.0675, 30400.0], [0.07150000000000001, 90000000]],
            'MD': [[0.02, 1000.0], [0.03, 1000.0], [0.04, 1000.0], [0.0475, 97000.0], [0.05, 25000.0], [0.0525, 25000.0], [0.055, 100000.0], [0.0575, 90000000]],
            'MA': [[0.05, 90000000]],
            'MI': [[0.0425, 90000000]],
            'MN': [[0.0535, 26960.0], [0.068, 61590.0], [0.0785, 75850.0], [0.09849999999999999, 90000000]],
            'MS': [[0.03, 4000.0], [0.04, 5000.0], [0.05, 90000000]],
            'MO': [[0.015, 948.0], [0.02, 1053.0], [0.025, 1053.0], [0.03, 1053.0], [0.035, 1053.0], [0.04, 1053.0], [0.045, 1053.0], [0.05, 1053.0], [0.054000000000000006, 90000000]],
            'MT': [[0.01, 3100.0], [0.02, 2300.0], [0.03, 2800.0], [0.04, 2900.0], [0.05, 3200.0], [0.06, 4100.0], [0.069, 90000000]],
            'NE': [[0.0246, 3230.0], [0.0351, 16100.0], [0.0501, 11830.0], [0.0684, 90000000]],
            'NV': [[0.0, 90000000]],
            'NH': [[0.05, 90000000]],
            'NJ': [[0.014, 20000.0], [0.0175, 15000.0], [0.035, 5000.0], [0.0552, 35000.0], [0.0637, 425000.0], [0.0897, 4500000.0], [0.1075, 90000000]],
            'NM': [[0.017, 5500.0], [0.032, 5500.0], [0.047, 5000.0], [0.049, 90000000]],
            'NY': [[0.04, 8500.0], [0.045, 3200.0], [0.0525, 2200.0], [0.059, 7500.0], [0.0621, 59250.0], [0.0649, 134750.0], [0.0685, 862150.0], [0.0882, 90000000]],
            'NC': [[0.0525, 90000000]],
            'ND': [[0.011, 39450.0], [0.0204, 56050.0], [0.0227, 103750.0], [0.0264, 233950.0], [0.028999999999999998, 90000000]],
            'OH': [[0.0285, 21700.0], [0.0333, 43450.0], [0.038, 21800.0], [0.0441, 108700.0], [0.04797, 90000000]],
            'OK': [[0.005, 1000.0], [0.01, 1500.0], [0.02, 1250.0], [0.03, 1150.0], [0.04, 2300.0], [0.05, 90000000]],
            'OR': [[0.05, 3550.0], [0.07, 5350.0], [0.09, 116100.0], [0.099, 90000000]],
            'PA': [[0.030699999999999998, 90000000]],
            'RI': [[0.0375, 65250.0], [0.0475, 83100.0], [0.0599, 90000000]],
            'SC': [[0.0, 3070.0], [0.03, 3080.0], [0.04, 3080.0], [0.05, 3080.0], [0.06, 3090.0], [0.07, 90000000]],
            'SD': [[0.0, 90000000]],
            'TN': [[0.01, 90000000]],
            'TX': [[0.0, 90000000]],
            'UT': [[0.0495, 90000000]],
            'VT': [[0.0335, 39600.0], [0.066, 56400.0], [0.076, 104200.0], [0.0875, 90000000]],
            'VA': [[0.02, 3000.0], [0.03, 2000.0], [0.05, 12000.0], [0.0575, 90000000]],
            'WA': [[0.0, 90000000]],
            'WV': [[0.03, 10000.0], [0.04, 15000.0], [0.045, 15000.0], [0.06, 20000.0], [0.065, 90000000]],
            'WI': [[0.04, 11970.0], [0.0521, 11960.0], [0.0627, 239550.0], [0.0765, 90000000]],
            'WY': [[0.0, 90000000]],
            'DC': [[0.04, 10000.0], [0.06, 30000.0], [0.065, 20000.0], [0.085, 290000.0], [0.0875, 650000.0], [0.0895, -1000000.0]]
            }