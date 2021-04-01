
example = ["А123АА11", "А222АА123", "А12АА123", "А123СС1234", "АА123А12",
           "АА213АА11", "А3332АА212", "У123ААА123", "А234ВВ123", "Е233ВМН89",
           "С876ТУ786", "У563ВВ53", "АВ654ВВ12", "А1645СУ123", "А675СНН12",
           "А654УХ7688"]

symbols = ['А', 'В', 'Е', 'К', 'М', 'Н', 'О', 'Р', 'С', 'Т', 'У', 'Х']
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

for item, j in list(zip(example, range(len(example)))):
    count = 0
    if item[0] in symbols:
        for i in range(1, 4):
            if item[i] in digits:
                count += 1
        if count == 3:
            count = 0
            for i in range(4, 6):
                if item[i] in symbols:
                    count += 1
            if count == 2:
                count = 0
                for i in range(6, 8):
                    if item[i] in digits:
                        count += 1
                if count == 2:
                    if len(item) == 8:
                        print(item)
                    elif len(item) == 9:
                        if item[8] in digits:
                            print(item)
