import json

data = []

with open(
    "",
    "r",
    encoding="utf-8",
) as file:
    data = json.load(file)

data["business_data"]["resources"] = data["business_data"]["resources"][0:5]

with open("", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4)