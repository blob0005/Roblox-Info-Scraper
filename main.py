try:
    import requests
    import colorama
except Exception:
    print("Missing Module(s)")
    input("")
    exit()
colorama.init(autoreset=True)
def item():
    while True:
        try:
            id = input("Enter  Item Id: ")
            id = int(id)
            id = str(id)
            break
        except Exception:
            print("Enter Valid Id")
    json = requests.get("https://api.roblox.com/Marketplace/ProductInfo?assetId="+id).json()
    try:
        print(colorama.Fore.GREEN + "Asset Id: " + str(json["AssetId"]))
    except Exception:
        print(colorama.Fore.RED + "Asset Id: Error Getting Asset Id")
    try:
        print(colorama.Fore.GREEN + "Creator Username: " + str(json["Creator"]["Name"]))
    except Exception:
        print(colorama.Fore.RED + "Creator Username: Error Getting Creator Username")
    try:
        print(colorama.Fore.GREEN + "Creator Id: " + str(json["Creator"]["Id"]))
    except Exception:
        print(colorama.Fore.RED + "Creator Id: Error Getting Creator Id")
    try:
        print(colorama.Fore.GREEN + "Product Id: " + str(json["ProductId"]))
    except Exception:
        print(colorama.Fore.RED + "Product Id: Error Getting Product Id")
    try:
        print(colorama.Fore.GREEN + "Item Name: " + str(json["Name"]))
    except Exception:
        print(colorama.Fore.RED + "Item Name: Error Getting Item Name")
    try:
        print(colorama.Fore.GREEN + "Item Description: " + str(json["Description"]))
    except Exception:
        print(colorama.Fore.RED + "Item Description: Error Getting Item Description")
    try:
        print(colorama.Fore.GREEN + "Date Created: " + str(json["Created"]))
    except Exception:
        print(colorama.Fore.RED + "Date Created: Error Getting Date Created")
    try:
        print(colorama.Fore.GREEN + "Last Update To Item: " + str(json["Updated"]))
    except Exception:
        print(colorama.Fore.RED + "Last Update To Item: Error Getting Last Update To Item")
    try:
        print(colorama.Fore.GREEN + "Original Price: " + str(json["PriceInRobux"]))
    except Exception:
        print(colorama.Fore.RED + "Price: Error Getting Price")
    try:
        print(colorama.Fore.GREEN + "Is For Sale: " + str(json["IsForSale"]))
    except Exception:
        print(colorama.Fore.RED + "Is For Sale: Error Getting Is For Sale")
    print("All Info Printed")
    input("")
    return
def user():
    username = input("Input Username: ")
    json1 = requests.get("https://api.roblox.com/users/get-by-username?username="+username).json()
    try:
        print(colorama.Fore.GREEN + "User Id: " + str(json1["Id"]))
    except Exception:
        print(colorama.Fore.RED + "User Id: ERROR Getting User Id")
    try:
        print(colorama.Fore.GREEN + "Avatar Uri: " + str(json1["AvatarUri"]))
    except Exception:
        print(colorama.Fore.RED + "Avatar Uri: ERROR Getting Avatar Uri")
    try:
        print(colorama.Fore.GREEN + "Avatar Final: " + str(json1["AvatarFinal"]))
    except Exception:
        print(colorama.Fore.RED + "Avatar Final: ERROR Getting Avatar Final")
    try:
        print(colorama.Fore.GREEN + "Is Online: " + str(json1["IsOnline"]))
    except Exception:
        print(colorama.Fore.RED + "Is Online: ERROR Getting Is Online")
while True:
    print("""
    1. Item Scraper
    2. User Scraper
    """)
    main = input("> ")
    if main == "1":
        item()
    if main == "2":
        user()
