import pypict.tools
import itertools

ConfigParams = {
    "Model": ["vx805", "vx820"],
    "OS": ["Windows", "Linux", "DOS", "WINCE"],
    "Interface": ["USB", "RS-232", "Ethernet"], # "Bluetooth"
    "Lib": ["SBRF.dll", "Pilot_nt", "Sb_pilot", "Gate.dll"]
}

combinations = itertools.product(*(ConfigParams[Name] for Name in ConfigParams))
print(list(combinations))

# for case in pypict.tools.from_dict(ConfigParams):
#     print(case)
#     count += 1
#     print(count)