import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify,render_template


#################################################
# Database Setup
#################################################
rds_connection_string = "postgres:postgres@localhost:5432/Pokemon_Gen1"
engine = create_engine(f'postgresql://{rds_connection_string}')


#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api")
def welcome():
    """List all available api routes."""
    return (
        f"Routes available for all Gen 1 Pokemon<br/>"
        f"To retrieve a specific pokemon, input a pokemon's name in the api route below (replacing the word pokemon):<br/>"
        f"/api/v1.0/pokemon<br/>"

    )

# New route taking two parameters for battle - this is where our Machine Learning code will go 
@app.route("/api/v1.0/battle/<pokemon1>/<pokemon2>")
def battle(pokemon1,pokemon2):
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd
    from sklearn.linear_model import LinearRegression
    import requests
    import json
    import random
    from pprint import pprint
    filePath2 = "testingDF_results.csv"
    poke_df = pd.read_csv(filePath2)
    # results = engine.execute('SELECT * FROM gen1_data')
    # poke_df = pd.DataFrame(results)
    X = poke_df[["HP", "Attack", "Defense", "Special Attack", "Special Defense", "Speed"]]
    y = poke_df["W/L"].values.reshape(-1)
    print(f"Labels: {y[:10]}")
    print(f"Data: {X[:10]}")
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)
    from sklearn.linear_model import LogisticRegression
    classifier = LogisticRegression()
    classifier.fit(X_train, y_train)
    print(f"Training Data Score: {classifier.score(X_train, y_train)}")
    print(f"Testing Data Score: {classifier.score(X_test, y_test)}")

    return jsonify({"W/L": 1})


@app.route("/api/v1.0/pokemon")
def types():
    
    results = engine.execute('SELECT DISTINCT "name" FROM gen1_data')

    all_pokemon = []
    for name in results:
        print(name)
        pokemon_dict = {}
        pokemon_dict["name"] = name[0]
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/bulbasaur")
def bulbasaur():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'bulbasaur\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/ivysaur")
def ivysaur():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'ivysaur\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/venusaur")
def venusaur():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'venusaur\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/charmander")
def charmander():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'charmander\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/charmeleon")
def charmeleon():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'charmeleon\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/charizard")
def charizard():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'charizard\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/squirtle")
def squirtle():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'squirtle\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/wartortle")
def wartortle():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'wartortle\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/blastoise")
def blastoise():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'blastoise\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/caterpie")
def caterpie():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'caterpie\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/metapod")
def metapod():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'metapod\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/butterfree")
def butterfree():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'butterfree\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/weedle")
def weedle():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'weedle\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/kakuna")
def kakuna():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'kakuna\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/beedrill")
def beedrill():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'beedrill\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/pidgey")
def pidgey():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'pidgey\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/pidgeotto")
def pidgeotto():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'pidgeotto\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/pidgeot")
def pidgeot():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'pidgeot\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/rattata")
def rattata():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'rattata\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/raticate")
def raticate():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'raticate\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/spearow")
def spearow():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'spearow\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/fearow")
def fearow():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'fearow\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/ekans")
def ekans():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'ekans\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/arbok")
def arbok():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'arbok\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/pikachu")
def pikachu():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'pikachu\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/raichu")
def raichu():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'raichu\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/sandshrew")
def sandshrew():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'sandshrew\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/sandslash")
def sandslash():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'sandslash\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/nidoran-f")
def nidoranf():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'nidoran-f\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/nidorina")
def nidorina():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'nidorina\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/nidoqueen")
def nidoqueen():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'nidoqueen\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/nidoran-m")
def nidoranm():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'nidoran-m\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/nidorino")
def nidorino():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'nidorino\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/nidoking")
def nidoking():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'nidoking\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/clefairy")
def clefairy():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'clefairy\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/clefable")
def clefable():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'clefable\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/vulpix")
def vulpix():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'vulpix\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/ninetales")
def ninetales():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'ninetales\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/jigglypuff")
def jigglypuff():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'jigglypuff\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/wigglytuff")
def wigglytuff():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'wigglytuff\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/zubat")
def zubat():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'zubat\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/golbat")
def golbat():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'golbat\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/oddish")
def oddish():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'oddish\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/gloom")
def gloom():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'gloom\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/vileplume")
def vileplume():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'vileplume\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/paras")
def paras():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'paras\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/parasect")
def parasect():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'parasect\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/venonat")
def venonat():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'venonat\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/venomoth")
def venomoth():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'venomoth\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/diglett")
def diglett():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'diglett\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/dugtrio")
def dugtrio():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'dugtrio\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/meowth")
def meowth():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'meowth\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/persian")
def persian():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'persian\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/psyduck")
def psyduck():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'psyduck\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/golduck")
def golduck():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'golduck\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/mankey")
def mankey():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'mankey\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/primeape")
def primeape():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'primeape\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/growlithe")
def growlithe():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'growlithe\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/arcanine")
def arcanine():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'arcanine\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/poliwag")
def poliwag():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'poliwag\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/poliwhirl")
def poliwhirl():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'poliwhirl\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/poliwrath")
def poliwrath():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'poliwrath\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/abra")
def abra():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'abra\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/kadabra")
def kadabra():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'kadabra\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/alakazam")
def alakazam():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'alakazam\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/machop")
def machop():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'machop\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/machoke")
def machoke():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'machoke\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/machamp")
def machamp():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'machamp\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/bellsprout")
def bellsprout():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'bellsprout\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/weepinbell")
def weepinbell():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'weepinbell\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/victreebel")
def victreebel():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'victreebel\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/tentacool")
def tentacool():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'tentacool\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/tentacruel")
def tentacruel():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'tentacruel\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/geodude")
def geodude():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'geodude\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/graveler")
def graveler():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'graveler\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/golem")
def golem():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'golem\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/ponyta")
def ponyta():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'ponyta\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/rapidash")
def rapidash():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'rapidash\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/slowpoke")
def slowpoke():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'slowpoke\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/slowbro")
def slowbro():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'slowbro\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/magnemite")
def magnemite():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'magnemite\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/magneton")
def magneton():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'magneton\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/farfetchd")
def farfetchd():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'farfetchd\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/doduo")
def doduo():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'doduo\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/dodrio")
def dodrio():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'dodrio\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/seel")
def seel():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'seel\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/dewgong")
def dewgong():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'dewgong\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/grimer")
def grimer():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'grimer\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/muk")
def muk():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'muk\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/shellder")
def shellder():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'shellder\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/cloyster")
def cloyster():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'cloyster\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/gastly")
def gastly():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'gastly\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/haunter")
def haunter():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'haunter\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/gengar")
def gengar():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'gengar\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/onix")
def onix():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'onix\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/drowzee")
def drowzee():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'drowzee\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/hypno")
def hypno():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'hypno\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/krabby")
def krabby():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'krabby\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/kingler")
def kingler():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'kingler\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/voltorb")
def voltorb():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'voltorb\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/electrode")
def electrode():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'electrode\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/exeggcute")
def exeggcute():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'exeggcute\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/exeggutor")
def exeggutor():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'exeggutor\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/cubone")
def cubone():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'cubone\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/marowak")
def marowak():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'marowak\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/hitmonlee")
def hitmonlee():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'hitmonlee\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/hitmonchan")
def hitmonchan():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'hitmonchan\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/lickitung")
def lickitung():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'lickitung\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/koffing")
def koffing():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'koffing\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/weezing")
def weezing():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'weezing\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/rhyhorn")
def rhyhorn():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'rhyhorn\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/rhydon")
def rhydon():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'rhydon\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/chansey")
def chansey():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'chansey\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/tangela")
def tangela():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'tangela\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/kangaskhan")
def kangaskhan():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'kangaskhan\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/horsea")
def horsea():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'horsea\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/seadra")
def seadra():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'seadra\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/goldeen")
def goldeen():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'goldeen\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/seaking")
def seaking():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'seaking\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/staryu")
def staryu():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'staryu\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/starmie")
def starmie():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'starmie\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/mr-mime")
def mrmime():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'mr-mime\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/scyther")
def scyther():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'scyther\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/jynx")
def jynx():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'jynx\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/electabuzz")
def electabuzz():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'electabuzz\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/magmar")
def magmar():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'magmar\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/pinsir")
def pinsir():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'pinsir\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/tauros")
def tauros():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'tauros\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/magikarp")
def magikarp():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'magikarp\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/gyarados")
def gyarados():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'gyarados\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/lapras")
def lapras():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'lapras\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/ditto")
def ditto():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'ditto\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/eevee")
def eevee():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'eevee\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/vaporeon")
def vaporeon():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'vaporeon\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/jolteon")
def jolteon():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'jolteon\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/flareon")
def flareon():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'flareon\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/porygon")
def porygon():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'porygon\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/omanyte")
def omanyte():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'omanyte\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/omastar")
def omastar():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'omastar\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/kabuto")
def kabuto():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'kabuto\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/kabutops")
def kabutops():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'kabutops\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/aerodactyl")
def aerodactyl():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'aerodactyl\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/snorlax")
def snorlax():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'snorlax\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/articuno")
def articuno():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'articuno\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/zapdos")
def zapdos():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'zapdos\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/moltres")
def moltres():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'moltres\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/dratini")
def dratini():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'dratini\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/dragonair")
def dragonair():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'dragonair\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/dragonite")
def dragonite():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'dragonite\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/mewtwo")
def mewtwo():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'mewtwo\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/mew")
def mew():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'mew\' ORDER BY "name"')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)


if __name__ == '__main__':
    app.run(debug=True)
    