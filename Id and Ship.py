for i in range(int(input())):
    a = input()
    if a in ('b','B'):
        print("BattleShip")
    elif a in ('C', 'c'):
        print("Cruiser")
    elif a in ('D', 'd'):
        print("Destroyer")
    elif a in ('f', 'F'):
        print("Frigate")
