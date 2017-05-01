import json
#########################################
# Example JSON objects for each command #
#########################################

VALID_EXILE = "{\"id_str\": \"127.0.0.1:50001\", \"data\": { \
\"cmd\": \"exile\" \
\"data\":\"127.0.0.1:50002\" \
} \
}"

VALID_WELCOME = "{\"id_str\": \"127.0.0.1:50001\", \"data\": { \
\"cmd\": \"welcome\" \
\"data\":\"127.0.0.1:50002\" \
} \
}"

VALID_DATA = "{\"id_str\": \"127.0.0.1:50001\", \"data\": { \
\"cmd\": \"data\" \
\"data\":\"data\" \
} \
}"

#50003 is our CH node in this example
VALID_FORWARD = "{\"id_str\": \"127.0.0.1:50003\", \"data\": { \
\"cmd\": \"forward\", \
\"orig_source\": \"127.0.0.1:50001\", \
\"data\":\"data\" \
}\
}"

#TODO: Parse all of the json data
#Takes in a JSON string, decodes it, and then returns the resultant JSON
#This will contain a nested JSON object as described by our spec.
#See any of the above constants for examples
def json_to_str(data):
    return json.loads(data)

#TODO: Encode all of the data into json
#Takes all of the data required to built the JSON objects
#orig_source is only populated if the command is "forward"
#L2_data is 
def vals_to_json(id_str, cmd, orig_source=None, L2_data):
    #build the json from the provided information
    #have separate cases for each command type

    #
    pass

##TODO: Encode Layer one data 
#def enccode_layer_one():
#    pass
#
##TODO: Encode layer 2 data
#def encode_layer_two():
#    pass
