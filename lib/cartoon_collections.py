def roll_call_dwarves(names):
    i = 1
    for name in names:
        print(f'{i}. {name}')
        i +=1

def summon_captain_planet(calls):
    capital_calls = [f'{call.capitalize()}!'for call in calls]
    return capital_calls

def long_planeteer_calls(calls):
    for call in calls:
        if len(call) > 4:
            return True
    return False
        


def find_the_cheese(ingredients):
    cheeses =  ["cheddar", "gouda", "camembert"]
    for ingredient in ingredients:
        if ingredient in cheeses:
            return ingredient
    return None
    pass
