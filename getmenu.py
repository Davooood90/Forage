import requests
from datetime import datetime

def retrieve_data():
    # Get current date in yyyy/mm/dd format
    slash_date = datetime.now().strftime("%Y/%m/%d")

    day_of_week = (datetime.now().weekday() + 2) % 7 or 7

    restaurant_option = {
        "dabao": f"https://ubc.api.nutrislice.com/menu/api/weeks/school/dabao/menu-type/dabao/{slash_date}",
        "feast-breakfast": f"https://ubc.api.nutrislice.com/menu/api/weeks/school/ubc-feast-totem-park-residence/menu-type/feast-at-totem-park/{slash_date}",
        "feast-lunch": f"https://ubc.api.nutrislice.com/menu/api/weeks/school/ubc-feast-totem-park-residence/menu-type/feast-totem-park-residence-lunch/{slash_date}",
        "feast-dinner": f"https://ubc.api.nutrislice.com/menu/api/weeks/school/ubc-feast-totem-park-residence/menu-type/feast-totem-park-residence-lunch-dinner/{slash_date}", 
        "gather-breakfast": f"https://ubc.api.nutrislice.com/menu/api/weeks/school/ubc-gather-place-vanier-residence/menu-type/gather-place-vanier-residence-breakfast/{slash_date}",
        "gather-lunch": f"https://ubc.api.nutrislice.com/menu/api/weeks/school/ubc-gather-place-vanier-residence/menu-type/gather-place-vanier-residence-breakfast/{slash_date}",
        "harvest": f"https://ubc.api.nutrislice.com/menu/api/weeks/school/ubc-harvest-market/menu-type/harvest/{slash_date}",
        "hero-coffee-harvest": f"https://ubc.api.nutrislice.com/menu/api/weeks/school/hero-coffee-harvest-market/menu-type/hero-coffee-harvest-market/{slash_date}",
        "hero-coffee": f"https://ubc.api.nutrislice.com/menu/api/weeks/school/hero-coffee-market/menu-type/hero-coffee-market/{slash_date}",
        "mercantes": f"https://ubc.api.nutrislice.com/menu/api/weeks/school/ubc-mercate-pizza/menu-type/mercante/{slash_date}",
        "oc-breakfast": f"https://ubc.api.nutrislice.com/menu/api/weeks/school/ubc-open-kitchen/menu-type/open-kitchen-orchard-commons-residence-breakfast/{slash_date}",
        "oc-lunch": f"https://ubc.api.nutrislice.com/menu/api/weeks/school/ubc-open-kitchen/menu-type/open-kitchen-at-orchard-commons/{slash_date}",
        "perugia": f"https://ubc.api.nutrislice.com/menu/api/weeks/school/perugia-italian-caffe/menu-type/perugia-italian-caffe/{slash_date}",
        "pho-real": f"https://ubc.api.nutrislice.com/menu/api/weeks/school/pho-real/menu-type/pho-real/{slash_date}"
    }

    menu = {}

    # Make a GET request to fetch the raw JSON data
    for location, url in restaurant_option.items():
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON data
            data = response.json()
            # Now `data` is a dictionary you can work with

            menu_items = data["days"][day_of_week - 1]["menu_items"]

            for i in (range(len(menu_items))):
                try:
                    name = menu_items[i]["food"]["name"]
                    menu[name] = {
                        "ingredients": menu_items[i]["food"]["ingredients"],
                        "allergens": [],
                        "special diets": [],
                        "location": location,
                    }
                    for j in menu_items[i]["food"]["icons"]["food_icons"]:
                        filter_type = j["food_icon_group"]
                        if filter_type == 2435:
                            menu[name]["special diets"].append(j["synced_name"])
                        else:
                            menu[name]["allergens"].append(j["synced_name"])
                except:
                    pass
            
        else:
            print(f"Failed to retrieve data: {response.status_code}. Url {url}")

    return menu