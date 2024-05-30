import random
import requests

def auto(pre="100092529", length=6):
    rand = ''.join(random.choices("0123456789", k=length))
    return pre + rand

# Prompt user for the file path where the results will be saved
file_path = input("Enter the file path where the results will be saved: ")
axo = int(input("How much: "))
for i in range(axo):
    uid = auto()
    print(uid)
    
    # Check if UID is live using the provided API
    response = requests.get(f"https://thanhlike.com/modun/tool/get_facebook.php?type=checklive&id={uid}").text
    print(response)
    
    if "live" in response:
        # Fetch name using another API
        api_url = f"https://api.mr999plus.site/fb-id-info/https://www.facebook.com/profile.php?id={uid}"
        pi = requests.get(api_url)
        
        if pi.status_code == 200:
            data = pi.json()
            
            if data.get("success"):
                name = data["data"]["name"]
                with open(file_path, "a", encoding="utf-8") as file:  # Open the file with UTF-8 encoding
                    file.write(f"{uid}|{name}\n")
                print(f"Saved UID: {uid} with Name: {name}")
            else:
                print(f"Failed to retrieve name for UID: {uid} - Success flag is false.")
        else:
            print(f"Failed to retrieve data for UID: {uid} - HTTP status code {pi.status_code}")
