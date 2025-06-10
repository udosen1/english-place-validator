

import requests

def is_valid_place_in_england(place):
    url = "https://nominatim.openstreetmap.org/search"
    params = {
        "q": place,
        "countrycodes": "gb",  # Great Britain
        "format": "json",
        "limit": 1,
        "addressdetails": 1,
        "extratags": 1
        #"featuretype": "city"
    }
    headers = {
        "User-Agent": "place-validator-app"
    }

    try:
        response = requests.get(url, params=params, headers=headers, timeout=10)
        data = response.json()
        
        
        if data and "address" in data[0]:
            place_type = data[0].get("type", "").lower()
            if not any(word in place_type for word in ["city", "town", "village", "hamlet", "suburb", "administrative"]):
                return False    # Reject buildings' named in england example; Abuja
            
            address = data[0]["address"]
           # print("DEBUG -> address from API:", address)
            country = address.get("country", "").lower()
            state = address.get("state", "").lower()
            
            return country == "united kingdom" and "england" in state
        
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
    
       
    
    
    