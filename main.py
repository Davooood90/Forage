from flask import Flask, render_template, redirect, request
from filter import find_foods_without_allergens, find_foods_with_special_diets
from getmenu import retrieve_data


locations = {
    "dabao": {"id": "dabao", "name": "Dabao", "hours": "7:30 AM - 6:00 PM", "link": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d5206.935639042987!2d-123.2526827!3d49.2675321!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x548672b6e7ecb487%3A0xb469afb686ebb577!2sIrving%20K.%20Barber%20Learning%20Centre%20(IKB)!5e0!3m2!1sen!2sca!4v1728195632846!5m2!1sen!2sca"},
    "feast": {"id": "feast", "name": "Feast", "hours": "7:00 AM - 6:00 PM", "link": "https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d41663.08182299129!2d-123.3184421!3d49.2585336!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x548672cb47a15343%3A0xec0f3de356e04cd1!2sFeast!5e0!3m2!1sen!2sca!4v1728195621344!5m2!1sen!2sca"},
    "gather": {"id": "gather", "name": "Gather", "hours": "7:00 AM - 6:00 PM", "link": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2603.626054526958!2d-123.25863059999998!3d49.264533300000004!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x548672b4e4a99619%3A0xe5bca09347600efd!2sGather%20at%20Vanier!5e0!3m2!1sen!2sca!4v1728195611632!5m2!1sen!2sca"},
    "harvest": {"id": "harvest", "name": "Harvest", "hours": "7:00 AM - 6:00 PM", "link": "https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d2603.502466358015!2d-123.2563697!3d49.2668755!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x548672b5a0e4ce39%3A0xed10a73b45dbe3a3!2sHarvest%20Market%20%26%20Deli!5e0!3m2!1sen!2sca!4v1728195599018!5m2!1sen!2sca"},
    "hero-coffee-harvest": {"id": "hero-coffee-harvest", "name": "Hero + Harvest", "hours": "7:00 AM - 6:00 PM", "link": "https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d1301.6929354761376!2d-123.2541519!3d49.2690851!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x54867390e038fc6d%3A0x30eb0af0710b0cdf!2sHero%20%2B%20Harvest!5e0!3m2!1sen!2sca!4v1728195583275!5m2!1sen!2sca"},
    "hero-coffee": {"id": "hero-coffee", "name": "Hero Coffee + Market", "hours": "8:30 AM - 10:30 PM", "link": "https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d1301.9208358732083!2d-123.2536094!3d49.2604468!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x548672cbabf55a15%3A0x1d82acab1faef3e3!2sHero%20Coffee%20%2B%20Market!5e0!3m2!1sen!2sca!4v1728195570142!5m2!1sen!2sca"},
    "mercantes": {"id": "mercantes", "name": "Mercantes", "hours": "10 AM - 11 PM", "link": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d5207.336933425436!2d-123.2549759!3d49.26372949999999!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x548672b5984be563%3A0x2199ac3872d942ea!2sMercante!5e0!3m2!1sen!2sca!4v1728195557235!5m2!1sen!2sca"},
    "oc": {"id": "oc", "name": "Orchid Commons", "hours": "7:00 AM - 6:00 PM", "link": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2603.8402630093333!2d-123.2518245!3d49.260473499999996!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x548672cbab8085b9%3A0xd0113f8377d90e0c!2sOpen%20Kitchen!5e0!3m2!1sen!2sca!4v1728195539934!5m2!1sen!2sca"},
    "perugia": {"id": "perugia", "name": "Perugia Italian Caffè", "hours": "7:30 AM - 5 PM", "link": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d5207.4983375074025!2d-123.24499399999999!3d49.2622!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x548672c90bd26bd7%3A0x1edd3bffb80ccd29!2sPerugia%20Italian%20Caff%C3%A8!5e0!3m2!1sen!2sca!4v1728195524568!5m2!1sen!2sca"},
    "pho-real": {"id": "pho-real", "name": "Pho Real", "hours": "10:30 AM - 4 PM", "link": "https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d862.8570076653587!2d-123.24874190338792!3d49.26074090451325!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x548673622705786b%3A0xa5bc68c9c6e58d7e!2sPho%20Real!5e0!3m2!1sen!2sus!4v1728195481208!5m2!1sen!2sus"}
}


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/recommendations", methods=["GET", "POST"])
def handle_preferences():
    if request.method == "POST":
        # Get checked boxes from the form
        allergies = request.form.getlist('allergen')
        special_needs = request.form.getlist('diet')

        allergies_accounted = find_foods_without_allergens(retrieve_data(), allergies)
        special_needs_accounted = find_foods_with_special_diets(allergies_accounted, special_needs)

        options = set(item['location'] for item in special_needs_accounted.values())

        available = []

        food_options = {}
        short_list = {}
        for i in options:
            print("feast" not in "feast-lunch")
            if "feast" in i:
                if "feast" not in available:
                    available.append("feast")
            elif "gather" in i:
                if "gather" not in available:
                    available.append("gather")
            elif "oc" in i:
                if "oc" not in available:
                    available.append("oc")
            else:
                available.append(i)
        a = []
        for i in available:
            a.append(locations[i])
            food_options[i] = []
            short_list[i] = []
        for key, food in special_needs_accounted.items():
            temp = {key: food}
            if "feast" in food["location"]:
                food_options["feast"].append(temp)
                if (len(short_list["feast"]) < 4):
                    short_list["feast"].append(temp)
            elif "gather" in food["location"]:
                food_options["gather"].append(temp)
                if (len(short_list["gather"]) < 4):
                    short_list["gather"].append(temp)
            elif "oc" in food["location"]:
                food_options["oc"].append(temp)
                if (len(short_list["oc"]) < 4):
                    short_list["oc"].append(temp)
            else:
                food_options[food["location"]].append(temp)
                if (len(short_list[food["location"]]) < 4):
                    short_list[food["location"]].append(temp)
        
        print(food_options)
        # Return a response or render a template
        return render_template('index.html', options=a, short=short_list, foods=food_options)

if __name__ == "__main__":
    app.run(port=3000, debug=True)
