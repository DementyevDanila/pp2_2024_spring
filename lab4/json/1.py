import json

with open("sample-data.json") as file:
    y = json.load(file)

floor1 = y["imdata"]

def output():
    pass
print("Interface Status\n================================================================================")
print("DN                                                 Description           Speed    MTU")
print("-------------------------------------------------- --------------------  ------  ------")

for i in range(0, len(y["imdata"])):
    print(y["imdata"][i]["l1PhysIf"]["attributes"]["dn"], "                           ", y["imdata"][i]["l1PhysIf"]["attributes"]["descr"], y["imdata"][i]["l1PhysIf"]["attributes"]["speed"], " ", y["imdata"][i]["l1PhysIf"]["attributes"]["mtu"])
