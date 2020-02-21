import json

with open("/etc/ssowat/conf.json.persistent", "r", encoding='utf-8') as jsonFile:
    data = json.load(jsonFile)
    data["skipped_urls"].remove("/_matrix")
    data["protected_urls"].remove("/_matrix/cas_server.php/login")

with open("/etc/ssowat/conf.json.persistent", "w", encoding='utf-8') as jsonFile:
    jsonFile.write(json.dumps(data, indent=4, sort_keys=True))
