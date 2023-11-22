def roll_call_dwarves(list):
    i = 0
    while i < len(list):
        print(f"{i+1}. {list[i]}")
        i+=1

def summon_captain_planet(calls):
    exclaimed_calls = [f"{call.title()}!" for call in calls]
    print(exclaimed_calls)
    return(exclaimed_calls)
    

def long_planeteer_calls(calls):
    length_list = [len(call) for call in calls]
    more_than_4_list = []
    for item in length_list:
        if item > 4:
            more_than_4_list.append(item)
    if len(more_than_4_list) > 0:
        return True
    else: 
        return False

def find_the_cheese(cheeses):
    result = None
    i = 0
    while i < len(cheeses):
        if cheeses[i] == "gouda" or cheeses[i] == "camembert" or cheeses[i] == "cheddar":
            result = cheeses[i]
            break
        i += 1
    print(result)
    return result
         

snacks = ["crackers", "gouda", "thyme"]
find_the_cheese(snacks)
#=> "gouda"

soup = ["tomato soup", "cheddar", "oyster crackers", "gouda"]
find_the_cheese(soup)
#=> "cheddar"

ingredients = ["garlic", "rosemary", "bread"]
find_the_cheese(ingredients)
#=> None