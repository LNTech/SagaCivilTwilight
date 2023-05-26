"""Sends data from the Civil_Twilight class to a Discord Webhook"""

import json
from astral import CivilTwilight
from webhook import Embed


TEST_WEBHOOK = ""
PROD_WEBHOOK = ""


def main():
    """Main function handler for script"""
    civil_twilight = CivilTwilight()

    if TEST_WEBHOOK == "" and PROD_WEBHOOK == "":
        print("No webhooks found. Quitting...")
        return 

    with open('locations.json', 'r') as file:
        locations = json.load(file)

    for location in locations: # Iterates over locations in json file
        print(f"Getting dusk time for {location['name']}") 

        for farm in location['locations']:
            farm['times'] = civil_twilight.calculate(str(farm['lat']), str(farm['lon'])) # Get civil twilight start and end time and add to dict


        if TEST_WEBHOOK != "": # If the test_webhook variable is set then use that
            embed_object = Embed(TEST_WEBHOOK)
        else: # Otherwise use the production webhook
            embed_object = Embed(PROD_WEBHOOK)

        embed_object.send_embed(location) # Send the embed object


if __name__ == "__main__":
    main()
