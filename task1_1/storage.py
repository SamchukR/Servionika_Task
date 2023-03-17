#!/bin/python3
import argparse
import json
import os

storage_path = "./storage.data"


def get_data():
    if not os.path.exists(storage_path):
        return ('No storage.data')

    with open(storage_path, 'r') as storage:
        raw_data = storage.read()
        if raw_data:
            return json.loads(raw_data)
        return {}


def put(key, value):
    data = get_data()
    if key in data:
        data[key].append(value)
    else:
        data[key] = [value]

    with open(storage_path, 'w') as storage:
        storage.write(json.dumps(data))


def get(key):
    data = get_data()
    return data.get(key)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--key')
    parser.add_argument('--val')

    args = parser.parse_args()

    if args.key and args.val:
        put(args.key, args.val)
    elif args.key:
        print(get(args.key))
    else:
        print('No command (Try -h to see keys)')
