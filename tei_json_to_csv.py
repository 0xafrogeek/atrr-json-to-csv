import pandas as pd
import json

with open("./path/path2/attributeDataValues.json") as f:
    data = json.load(f)["trackedEntityInstances"]

# Flatten to dic
for obj in data:
    if isinstance(obj["attributes"], list):
        attributes_dict = {
            attr.get("code", attr["attribute"]): attr["value"]
            for attr in obj["attributes"]
        }
        obj.update(attributes_dict)
        del obj["attributes"]
    else:
        print(f"Unexpected attributes type in object: {obj}")

df = pd.DataFrame(data)

df.to_csv("attributeDataValues.csv", index=False)
