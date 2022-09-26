
# Pete likes to bake some cakes. He has some recipes and ingredients. 
# Unfortunately he is not good in maths. Can you help him to find out, 
# how many cakes he could bake considering his recipes?

# Write a function cakes(), which takes the recipe (object) and the available 
# ingredients (also an object) and returns the maximum number of cakes Pete can
#  bake (integer). For simplicity there are no units for the amounts (e.g. 1 lb 
# of flour or 200 g of sugar are simply 1 or 200). Ingredients that are not 
# present in the objects, can be considered as 0.

#make sure all the ingredients from the recipe are in available

#See if we have enough of each ingredient to make a cake

#number of cakes is going to be limited by the the ingredient that prodices the fewest cakes

#return an int of number of cakes

def cakes(recipe, available):
    cakes_per_ingredient = []
    for ingredient in recipe:
        if ingredient not in available:
            return 0
        else:
            cakes_per_ingredient.append(available[ingredient]//recipe[ingredient])
    return min(cakes_per_ingredient)


#Better Solution uses .get on the dictionary. If .get cant find the key in this case it returns 0
def cakes(recipe, available):
    return min(available.get(k, 0)/recipe[k] for k in recipe)