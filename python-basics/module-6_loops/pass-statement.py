egos = ["little-king", "gian-i", "blue", "", "seven"]
for ego in egos:
    if ego == "":
        pass #todo: handle blank internal egos
    if ego == "gian-i":
        print(f"External ego: {ego} detected!")
        continue
    print(f"Internal ego: {ego}")