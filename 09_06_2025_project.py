

# Location Intelligence: Validating UK-Based places with Python

    
           
# Sample list of English places    
english_places = {"London", "Manchester", "Leeds", "Liverpool", "Newcastle upon Tyne", 
                  "Milton Keynes","Nottingham", "Birmingham", "Sheffield", "Bristol",
                  "Leicester", "Southampton","Coventry", "Bradford", "Brighton & Hove",
                  "Derby", "Plymouth", "Luton", "Stoke-on-Trent", "Portsmouth", "Reading",
                  "Norwich", "Wolverhampton", "Kingston upon Hull", "Northampton"}  
    
while True:
    location = input("Which major urban area in England do you live in? Please begin with a capital letter: ").strip().title()
    
    if location in english_places:
        print(f"Thank you for letting me know that you live in {location}")
        break
    else:
        print("That does not appear to be a recognised major urban area in England. Please try again! ")    
    
    
    
    
    
    
    
    
    
    
    
    
    
    