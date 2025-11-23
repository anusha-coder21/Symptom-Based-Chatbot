import os
import json
import random

# Always load the dataset from the backend folder (where this script lives)
BASE_DIR = os.path.dirname(__file__)
input_file = os.path.join(BASE_DIR, "train.jsonl")
output_file = os.path.join(BASE_DIR, "train_shuffled.jsonl")

# Load lines
data = []
with open(input_file, "r", encoding="utf-8") as f:
    for line in f:
        try:
            data.append(json.loads(line))
        except:
            pass

# Shuffle
random.shuffle(data)

# Save back
with open(output_file, "w", encoding="utf-8") as f:
    for item in data:
        f.write(json.dumps(item, ensure_ascii=False) + "\n")

print(f"Shuffled dataset saved to: {output_file}")
