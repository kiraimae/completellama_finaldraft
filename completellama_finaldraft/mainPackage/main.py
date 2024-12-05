
#main.py

import dataPackage
from locationPackage.decryptedLocation import *
from dataPackage import *

def main():
    
    # Path to given files to be decrypted
    json_file = 'dataPackage/EncryptedGroupHints Fall 2024 Section 001.json'
    english_file = 'dataPackage/UCEnglish.txt'
    
    #Instanatiation line
    location_finder = findLocation(json_file, english_file)
    
    projectteamName = 'CompleteLlama'
    
    # Location decryption code
    location = location_finder.decrypt_location(projectteamName)
    
    #Output name of location!!
    print(f'Decrypted UC Location: {location}')

    if __name__ == "__main__":
        main()