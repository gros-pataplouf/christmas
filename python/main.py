import json

instructions = None

with open("instructions.json") as instructions_file:
    instructions = json.load(instructions_file)
