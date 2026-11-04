country = input("Enter your country: ").strip().lower()

match country:
    case "trinidad & tobago" | "trinidad" | "tobago" | "tt":
        print("TT")
    case "united states" | "us":
        print('US')
    case "canada" | "can":
        print("CAN")
    case "england" | "eng":
        print('ENG')
    case _:
        print("Unrecognized Country")
    
    
    