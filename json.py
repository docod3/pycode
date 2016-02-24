json_string = """
{
    "pk": 1, 
    "fa": "cc.ee"
    "fb": 
        "fc": "", 
        "fd_id": "12345"
    }
}"""

import simplejson as json
data = json.loads(json_string)
if data["fa"] == "cc.ee":
    data["fb"][new_key"] = "cc.ee was present!"

print json.dumps(data)
