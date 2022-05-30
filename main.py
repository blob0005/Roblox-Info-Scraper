try:
    import os
    from os import system
    system("title " + "Roblox Info Scraper")
except:
    pass
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
        print(colorama.Fore.RED + "Original Price: Error Getting Price")
    try:
        print(colorama.Fore.GREEN + "Is For Sale: " + str(json["IsForSale"]))
    except Exception:
        print(colorama.Fore.RED + "Is For Sale: Error Getting Is For Sale")
    while True:
        save = input("Wanna Save Info In An Txt File (y/n): ")
        if save == "y" or save == "n":
            break
        else:
            print("Enter A Valid Choice")
    if save == "n":
        return
    if save == "y":
        try:
            asset_id = "Asset Id: " + str(json["AssetId"])
        except:
            asset_id = "Asset Id: Error Getting Asset Id"
        try:
            creator_user = "Creator Username: " + str(json["Creator"]["Name"])
        except:
            creator_user = "Creator Username: Error Getting Creator Username"
        try:
            creator_id = "Creator Id: " + str(json["Creator"]["Id"])
        except:
            creator_id = "Creator Id: Error Getting Creator Id"
        try:
            produkt_id = "Product Id: " + str(json["ProductId"])
        except:
            produkt_id = "Product Id: Error Getting Product Id"
        try:
            item_name = "Item Name: " + str(json["Name"])
        except:
            item_name = "Item Name: Error Getting Item Name"
        try:
            item_description = "Item Description: " + str(json["Description"])
        except:
            item_description = "Item Description: Error Getting Item Description"
        try:
            date_created = "Date Created: " + str(json["Created"])
        except:
            date_created = "Date Created: Error Getting Date Created"
        try:
            last_update = "Last Update To Item: " + str(json["Updated"])
        except:
            last_update = "Last Update To Item: Error Getting Last Update To Item"
        try:
            original_price = "Original Price: " + str(json["PriceInRobux"])
        except:
            original_price = "Original Price: Error Getting Price"
        try:
            is_for_sale = "Is For Sale: " + str(json["IsForSale"])
        except:
            is_for_sale = "Is For Sale: Error Getting Is For Sale"
        try:
            save_file = open(id+".txt", "a")
            save_file.write(asset_id+"\n")
            save_file.write(creator_user+"\n")
            save_file.write(creator_id+"\n")
            save_file.write(produkt_id+"\n")
            save_file.write(item_name+"\n")
            save_file.write(item_description+"\n")
            save_file.write(date_created+"\n")
            save_file.write(last_update+"\n")
            save_file.write(original_price+"\n")
            save_file.write(is_for_sale+"\n")
            save_file.close()
            print("Succsesfully Saves Info")
            input("")
            return
        except:
            print("Error While Saving")
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
        save = input("Wanna Save Info In An Txt File (y/n): ")
        if save == "y" or save == "n":
            break
        else:
            print("Enter A Valid Choice")
    if save == "n":
        return
    if save == "y":
        try:
            user_id = "User Id: " + str(json1["Id"])
        except:
            user_id = "User Id: ERROR Getting User Id"
        try:
            avatar_Uri = "Avatar Uri: " + str(json1["AvatarUri"])
        except:
            avatar_Uri = "Avatar Uri: ERROR Getting Avatar Uri"
        try:
            avatar_final = "Avatar Final: " + str(json1["AvatarFinal"])
        except:
            avatar_final = "Avatar Final: ERROR Getting Avatar Final"
        try:
            is_online = "Is Online: " + str(json1["IsOnline"])
        except:
            is_online = "Is Online: ERROR Getting Is Online"
        try:
            save_file = open(username+".txt", "a")
            save_file.write(user_id+"\n")
            save_file.write(avatar_Uri+"\n")
            save_file.write(avatar_final+"\n")
            save_file.write(is_online+"\n")
            print("Succsesfully Saved Info")
            input("")
            return
        except:
            print("Failed To Save Info")
            input("")
            return
def group():
    main_id = input("Enter Group Id: ")
    re = requests.get("https://groups.roblox.com/v1/groups/"+main_id, "a").json()
    try:
        id = "Group Id: " + str(re["id"])
        print(colorama.Fore.GREEN + id)
    except:
        id = "Group Id: Error Getting Group Id"
        print(colorama.Fore.RED + id)
    try:
        name = "Group Name: " + str(re["name"])
        print(colorama.Fore.GREEN + name)
    except:
        name = "Group Name: Error Getting Group Name"
        print(colorama.Fore.RED + name)
    try:
        description = "Group Description" + str(re["description"])
        print(colorama.Fore.GREEN + description)
    except:
        description = "Description: Error Getting Description"
        print(colorama.Fore.RED + description)
    try:
        owner_user_id = "Owner User Id: " + str(re["owner"]["userId"])
        print(colorama.Fore.GREEN + owner_user_id)
    except:
        owner_user_id = "Owner User Id: Error Getting Owner User Id"
        print(colorama.Fore.RED + owner_user_id)
    try:
        owner_username = "Owner Username: " + str(re["owner"]["username"])
        print(colorama.Fore.GREEN + owner_username)
    except:
        owner_username = "Owner Username: Error Getting Owner Username"
        print(colorama.Fore.RED + owner_username)
    try:
        display_name = "Owner Display Name: " + str(re["owner"]["displayName"])
        print(colorama.Fore.GREEN + display_name)
    except:
        display_name = "Owner Display Name: Error Getting Owner Display Name"
        print(colorama.Fore.RED + display_name)
    try:
        group_shout = "Group Shout: " + str(re["shout"]["body"])
        print(colorama.Fore.GREEN + group_shout)
    except:
        group_shout = "Group Shout: Error Getting Group Shout"
        print(colorama.Fore.RED + group_shout)
    try:
        shout_poster_membeship = "Shout Poster Builders Club Membership Type: " + str(re["shout"]["poster"]["buildersClubMembershipType"])
        print(colorama.Fore.GREEN + shout_poster_membeship)
    except:
        shout_poster_membeship = "Shout Poster Builders Club Membership Type: Error Getting Shout Poster Builders Club Membership Type"
        print(colorama.Fore.RED + shout_poster_membeship)
    try:
        shout_user_id = "Shout Poster User Id: " + str(re["shout"]["poster"]["userId"])
        print(colorama.Fore.GREEN + shout_user_id)
    except:
        shout_user_id = "Shout Poster User Id: Error Getting Shout Poster User Id"
        print(colorama.Fore.RED + shout_user_id)
    try:
        shout_username = "Shout Poster Username: " + str(re["shout"]["poster"]["username"])
        print(colorama.Fore.GREEN + shout_username)
    except:
        shout_username = "Shout Poster Username: Error Getting Shout Poster Username"
        print(colorama.Fore.RED + shout_username)
    try:
        shout_display_name = "Shout Poster Display Name: " + str(re["shout"]["poster"]["displayName"])
        print(colorama.Fore.GREEN + shout_display_name)
    except:
        shout_display_name = "Shout Poster Display Name: Error Getting Shout Poster Display Name"
        print(colorama.Fore.RED + shout_display_name)
    try:
        created = "Shout Created Date: " + str(re["shout"]["created"])
        print(colorama.Fore.GREEN + created)
    except:
        created = "Shout Created Date: Error Getting Shout Created Date"
        print(colorama.Fore.RED + created)
    try:
        updated = "Shout Updated Date: " + str(re["shout"]["updated"])
        print(colorama.Fore.GREEN + updated)
    except:
        updated = "Shout Update Date: Error Getting Shout Update Date"
        print(colorama.Fore.RED + updated)
    try:
        member_count = "Group Member Count: " + str(re["memberCount"])
        print(colorama.Fore.GREEN + member_count)
    except:
        member_count = "Group Member Count: Error Getting Group Member Count"
        print(colorama.Fore.RED + member_count)
    try:
        is_builder_club_only = "Is Group Only Builders Club: " + str(re["isBuildersClubOnly"])
        print(colorama.Fore.GREEN + is_builder_club_only)
    except:
        is_builder_club_only = "Is Group Only Builders Club: Error Getting Is Group Only Builders Club"
        print(colorama.Fore.RED + is_builder_club_only)
    try:
        public_entry = "Public Entry: " + str(re["publicEntryAllowed"])
        print(colorama.Fore.GREEN + public_entry)
    except:
        public_entry = "Public Entry: Error Getting Public Entry"
        print(colorama.Fore.RED + public_entry)
    while True:
        save = input("Wanna Save Info In An Txt File (y/n): ")
        if save == "y" or save == "n":
            break
        else:
            print("Enter A Valid Choice")
    if save == "n":
        return
    if save == "y":
        try:
            save_file = open(main_id+".txt", "a")
            save_file.write(id+"\n")
            save_file.write(name+"\n")
            save_file.write(description+"\n")
            save_file.write(owner_user_id+"\n")
            save_file.write(owner_username+"\n")
            save_file.write(display_name+"\n")
            save_file.write(group_shout+"\n")
            save_file.write(shout_poster_membeship+"\n")
            save_file.write(shout_user_id+"\n")
            save_file.write(shout_username+"\n")
            save_file.write(shout_display_name+"\n")
            save_file.write(created+"\n")
            save_file.write(updated+"\n")
            save_file.write(member_count+"\n")
            save_file.write(is_builder_club_only+"\n")
            save_file.write(public_entry+"\n")
            save_file.close()
            print("Succsesfully Saved Info")
            input("")
            return
        except:
            print("Failed To Save")
            input("")
            return
while True:
    print("""
    1. Item Scraper
    2. User Scraper
    3. Group Scraper
    """)
    main = input("> ")
    if main == "1":
        item()
    if main == "2":
        user()
    if main == "3":
        group()
