import json

def remove_elements_json(element):
    json_file = open('test_payload.json')
    json_data = json.load(json_file)

    if element in json_data["inParams"]:
        json_data["inParams"].pop(element)
    else:
        json_data.pop(element)

    json_string = json.dumps(json_data)

    with open("upated_test_payload.json", "w") as j_file:
        j_file.write(json_string)

remove_elements_json("sessionId")
