import json
#########################################
# Example JSON objects for each command #
#########################################

VALID_EXILE = '{"id_str": "127.0.0.1:50001", "data": { \
"cmd": "exile", \
"data":"127.0.0.1:50002" \
} \
}'

VALID_WELCOME = '{"id_str": "127.0.0.1:50001", "data": { \
"cmd": "welcome", \
"data":"127.0.0.1:50002" \
} \
}'

VALID_DATA = '{"id_str": "127.0.0.1:50001", "data": { \
"cmd": "data", \
"data":"data" \
} \
}'

#50003 is our CH node in this example
VALID_FORWARD = '{"id_str": "127.0.0.1:50003", "data": { \
"cmd": "forward", \
"orig_source": "127.0.0.1:50001", \
"data":"data" \
}\
}'

#TODO: Parse all of the json data
#Takes in a JSON string, decodes it, and then returns the resultant JSON
#This will contain a nested JSON object as described by our spec.
#See any of the above constants for examples
def str_to_json(data):
    return json.loads(data)

#TODO: Encode all of the data into json
#Takes all of the data required to built the JSON objects
#orig_source is only populated if the command is "forward"
#L2_data is 
def vals_to_json(id_str, cmd, L2_data, orig_source=None):
    j = json.loads(VALID_EXILE)
    j['id_str'] = id_str
    j['data'] = L2_data

    if cmd == 'forward' and orig_source is None:
        raise Exception('Tried to make forward json request without specifying a source')

    elif cmd == 'forward' and orig_source:
        j['orig_source'] = orig_source

    return j


##TODO: Encode Layer one data 
#def encode_layer_one():
#    pass
#
##TODO: Encode layer 2 data
#def encode_layer_two():
#    pass
