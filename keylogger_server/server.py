# -*- coding: utf-8 -*-

from flask import *


port = 5000





app = Flask(__name__)

fichier = 0




@app.route('/', methods=['POST'])
def page():
    global fichier
    
    data = request.get_json()

    print(data)

    if "key" in data:
        with open(f"Logs/{str(fichier)}.txt", 'w') as f:
            f.write(data["key"])
            fichier += 1

    return "yep"




app.run(port=port)

