import json
from jsoncleaner.cleaner import JsonCleaner


@JsonCleaner.key_clean('/text')
def text_extract(key, val):
    return {'tweet': val.strip()}


kept_keys = []

replacement_keys = {
    '/user/screen_name': {'new_key': 'screen_name', 'return_type': str},

                    }


if __name__ == '__main__':
    with open('data.json') as data_file:
        json_data = json.loads(data_file.read())

    JsonCleaner.replace_keys(replacement_keys)
    JsonCleaner.keep_keys(kept_keys)

