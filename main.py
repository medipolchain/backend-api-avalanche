import json
from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.get("/token/{item}")
def get_male(item: int):
    try:

        if item == 0:
            return {
                "name": "Wheat Seed",
                "description": "The seed of Wheat, which is used within the game MetaFarm to plant wheat.",
                "image": "",
            }

        elif item == 1:
            return {
                "name": "Corn Seed",
                "description": "The seed of Corn, which is used within the game MetaFarm to plant corn.",
                "image": "",
            }

        elif item == 2:
            return {
                "name": "Wheat",
                "description": "The Wheat, which is the version of the seed wheat after it is planted and grown in the game MetaFarm.",
                "image": "",
            }

        elif item == 3:
            return {
                "name": "Corn",
                "description": "The Corn, which is the version of the seed corn after it is planted and grown in the game MetaFarm.",
                "image": "",
            }

        elif item == 4:
            return {
                "name": "Cow",
                "description": "The cow animal to be used in the game MetaFarm.",
                "image": "",
            }

        elif item == 5:
            return {
                "name": "Chicken",
                "description": "The chicken animal to be used in the game MetaFarm.",
                "image": "",
            }

        elif item == 6:
            return {
                "name": "Windmill",
                "description": "The windmill to produce new products from the acquired plants to be used in the game MetaFarm.",
                "image": "",
            }

        elif item == 7:
            return {
                "name": "Feedmixer",
                "description": "The feedmixer to produce new products from the acquired plants to be used in the game MetaFarm.",
                "image": "",
            }

        elif item == 8:
            return {
                "name": "Furnace",
                "description": "The furnace to produce new products from the acquired goods to be used in the game MetaFarm.",
                "image": "",
            }

        elif item == 9:
            return {
                "name": "Bread",
                "description": "The bread to be sold or used to acquire new goods to be used in the game MetaFarm.",
                "image": "",
            }

        elif item == 10:
            return {
                "name": "Popcorn",
                "description": "The popcorn to be sold or used in the game MetaFarm.",
                "image": "",
            }

        elif item == 11:
            return {
                "name": "Milk",
                "description": "The milk to be sold or used to acquire new goods to be used in the game MetaFarm.",
                "image": "",
            }

        elif item == 12:
            return {
                "name": "Egg",
                "description": "The egg to be sold or used to acquire new goods to be used in the game MetaFarm.",
                "image": "",
            }

        elif item == 13:
            return {
                "name": "Provender",
                "description": "The provender to be sold or feed the animals in the game MetaFarm to produce new goods.",
                "image": "",
            }

        elif item == 14:
            return {
                "name": "Dirt",
                "description": "The dirt, which is required to be bought to be able to plants the seeds and grow them.",
                "image": "",
            }

        elif item == 100:
            return {
                "name": "First Avatar",
                "description": "The dirt, which is required to be bought to be able to plants the seeds and grow them.",
                "image": "",
            }

        elif item == 101:
            return {
                "name": "Second Avatar",
                "description": "This is the avatar to be used in MetaFarm.",
                "image": "",
            }

        elif item == 102:
            return {
                "name": "Third Avatar",
                "description": "This is the avatar to be used in MetaFarm.",
                "image": "",
            }

        elif item == 103:
            return {
                "name": "Fourth Avatar",
                "description": "This is the avatar to be used in MetaFarm.",
                "image": "",
            }

        elif item == 104:
            return {
                "name": "Fifth Avatar",
                "description": "This is the avatar to be used in MetaFarm.",
                "image": "",
            }

    except Exception as e:
        return e
