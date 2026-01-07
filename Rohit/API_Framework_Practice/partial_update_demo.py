import os
import sys
import json

# Ensure local package imports work when running this script directly
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from api_objects.api_class import API
from api_objects.api_datafile import update_object_id, update_object_payload_patch


def main():
    api = API()
    response, status_code = api.update_object(object_id=update_object_id, payload=update_object_payload_patch, method="patch")
    print("Status:", status_code)
    try:
        print(json.dumps(response, indent=2))
    except Exception:
        print(response)


if __name__ == '__main__':
    main()
