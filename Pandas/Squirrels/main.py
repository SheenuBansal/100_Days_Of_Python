# Find how many squirrels are of which color
# Create a dataframe
import pandas as pd 
data = pd.read_csv("Squirrel_Data.csv")


# colors_of_squirrels = list(pd.unique(data["Primary Fur Color"]))
# print(colors_of_squirrels)

# -- Another method of getting colors of squirrels ---- 
# --- It will drop NaN values too ----

unique_squirrels = pd.unique(data["Primary Fur Color"])
colors_of_squirrels = (pd.DataFrame(unique_squirrels).dropna())[0]  # Removing NaN and fetching the column 
colors_of_squirrels = colors_of_squirrels.tolist()

new_dict={}
for color in colors_of_squirrels:
    # squirrels = data[data["Primary Fur Color"] == color]
    # new_dict[color] = squirrels["Primary Fur Color"].count()

    # Another Method in one line
    new_dict[color]=len(data[data["Primary Fur Color"] == color])
# print(new_dict)

squirrels_count={"Fur Color" : [], "Count" : []}

for key,value in new_dict.items():
    squirrels_count["Fur Color"].append(key)
    squirrels_count["Count"].append(value)

pd.DataFrame(squirrels_count).to_csv("squirrels_count.csv")