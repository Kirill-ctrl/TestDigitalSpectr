import re

example = ["А123АА11", "А222АА123", "А12АА123", "А123СС1234", "АА123А12",
           "АА213АА11", "А3332АА212", "У123ААА123", "А234ВВ123", "Е233ВМН89",
           "С876ТУ786", "У563ВВ53", "АВ654ВВ12", "А1645СУ123", "А675СНН12",
           "А654УХ7688"]

arr = [re.findall(r"^[АВЕКМНОРСТУХ][0-9]{3}[АВЕКМНОРСТУХ]{2}[0-9]{2,3}\Z", item) for item in example]
result = [item[0] for item in arr if item]
print("result with re.findall: ", result)

#  --------------------------
print("result with re.match: ")
for item in example:
    if re.match(r"^[АВЕКМНОРСТУХ][0-9]{3}[АВЕКМНОРСТУХ]{2}[0-9]{2,3}\Z", item):
        print(item)
