

import requests

def is_valid_place_in_england(place):
    url = "https://nominatim.openstreetmap.org/search"
    params = {
        "q": place,
        "countrycodes": "gb",  # Great Britain (includes England, Scotland, Wales)
        "format": "json",
        "limit": 1
    }
    headers = {
        "User-Agent": "place-validator-app"
    }

    try:
        response = requests.get(url, params=params, headers=headers, timeout=10)
        data = response.json()

        if data and "display_name" in data[0]:
            return "England" in data[0]["display_name"]
        else:
            return False
    except Exception as e:
        print("❌ Error occurred:", e)
        return False


# Main loop
while True:
    location = input("Which major urban area in England do you live in? ").strip().title()

    if is_valid_place_in_england(location):
        print(f"✅ Thank you! {location} is a valid place in England.")
        break
    else:
        print("❌ That doesn't appear to be a real place in England. Please try again.")   
    
    
    
    
    
    
    
    
    
    
    
    
    
    