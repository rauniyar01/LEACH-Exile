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

MALICIOUS_DATA = '{"id_str": "127.0.0.1:50001", "data": { \
"cmd": "data", \
"data":"BADBOYE" \
} \
}'


def str_to_json(data):
    return json.loads(data)


def vals_to_json(id_str, cmd, L2_data, orig_source=None):
    j = json.loads(VALID_EXILE)
    j['id_str'] = id_str
    j['data']['data'] = L2_data
    j['data']['cmd'] = cmd

    if cmd == 'forward' and orig_source is None:
        raise Exception('Tried to make forward json request without specifying a source')

    elif cmd == 'forward' and orig_source:
        j['data']['orig_source'] = orig_source

    return j

