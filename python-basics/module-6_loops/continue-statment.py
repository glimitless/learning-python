egos = ["little-king", "gian-i", "blue", "", "seven"]
for ego in egos:
    if ego == "":
        print("Blank detected! Terminating program.")
        break
    if ego == "gian-i":
        print(f"External ego: {ego} detected!")
        continue
    print(f"Internal ego: {ego}")