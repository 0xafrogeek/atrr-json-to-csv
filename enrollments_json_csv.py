import pandas as pd
import json
import re

# Replace with your actual file path (absolute path)
json_file_path = "/path/to/CBS-Enrollments.json"

# Function to parse JSON, handling double-escaped strings
def parse_json_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        json_content = f.read()
    
    try:
        first_parse = json.loads(json_content)
        print("After first parsing:")
        print(type(first_parse))
        print(first_parse)
        
        if isinstance(first_parse, str):
            second_parse = json.loads(first_parse)
            print("\nAfter second parsing:")
            print(type(second_parse))
            print(second_parse)
            return second_parse
        elif isinstance(first_parse, dict):
            return first_parse
        else:
            print("Unexpected JSON structure after first parsing.")
            return {}
    except json.JSONDecodeError as e:
        print(f"JSON decoding failed: {e}")
        return {}

parsed_json = parse_json_file(json_file_path)

if isinstance(parsed_json, dict) and "enrollments" in parsed_json:
    data = parsed_json["enrollments"]
    
    df = pd.DataFrame(data)
    
    print("\nDataFrame Preview:")
    print(df.head())
    
    csv_file_path = "CBS-Enrollments.csv"
    df.to_csv(csv_file_path, index=False)
    print(f"\nSuccessfully converted JSON to CSV and saved to {csv_file_path}")
else:
    print("The parsed JSON does not contain the key 'enrollments' or is not a valid JSON object.")