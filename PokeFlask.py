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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'bulbasaur\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'ivysaur\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'venusaur\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'charmander\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'charmeleon\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'charizard\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'squirtle\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'wartortle\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'blastoise\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'caterpie\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'metapod\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'butterfree\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'weedle\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'kakuna\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'beedrill\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'pidgey\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'pidgeotto\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'pidgeot\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'rattata\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'raticate\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'spearow\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'fearow\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'ekans\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'arbok\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'pikachu\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'raichu\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'sandshrew\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'sandslash\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'nidoran-f\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'nidorina\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'nidoqueen\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'nidoran-m\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'nidorino\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'nidoking\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'clefairy\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'clefable\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'vulpix\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'ninetales\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'jigglypuff\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'wigglytuff\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'zubat\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'golbat\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'oddish\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'gloom\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'vileplume\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'paras\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'parasect\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'venonat\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'venomoth\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'diglett\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'dugtrio\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'meowth\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'persian\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'psyduck\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'golduck\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'mankey\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'primeape\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'growlithe\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'arcanine\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'poliwag\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'poliwhirl\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'poliwrath\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'abra\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'kadabra\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'alakazam\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'machop\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'machoke\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'machamp\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'bellsprout\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'weepinbell\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'victreebel\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'tentacool\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'tentacruel\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'geodude\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'graveler\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'golem\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'ponyta\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'rapidash\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'slowpoke\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'slowbro\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'magnemite\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'magneton\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'farfetchd\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'doduo\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'dodrio\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'seel\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'dewgong\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'grimer\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'muk\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'shellder\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'cloyster\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'gastly\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'haunter\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'gengar\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'onix\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'drowzee\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'hypno\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'krabby\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'kingler\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'voltorb\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'electrode\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'exeggcute\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'exeggutor\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'cubone\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'marowak\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'hitmonlee\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'hitmonchan\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'lickitung\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'koffing\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'weezing\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'rhyhorn\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'rhydon\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'chansey\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'tangela\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'kangaskhan\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'horsea\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'seadra\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'goldeen\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'seaking\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'staryu\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'starmie\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'mr-mime\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'scyther\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'jynx\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'electabuzz\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'magmar\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'pinsir\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'tauros\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'magikarp\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'gyarados\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'lapras\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'ditto\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'eevee\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'vaporeon\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'jolteon\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'flareon\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'porygon\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'omanyte\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'omastar\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'kabuto\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'kabutops\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'aerodactyl\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'snorlax\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'articuno\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'zapdos\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'moltres\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'dratini\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'dragonair\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'dragonite\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'mewtwo\'')

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
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "name" = \'mew\'')

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
    