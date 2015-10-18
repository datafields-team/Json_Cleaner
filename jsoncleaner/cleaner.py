import json
from transforms.transformations import default_callback


class JsonCleaner(object):
    clean_functions = {}
    default_clean_function = default_callback


    @classmethod
    def _default_callback(cls, key, val):
        return key, val


    @classmethod
    def _add_callback(cls, key, clean_function):
        cls.clean_functions[key] = clean_function


    @classmethod
    def key_clean(cls, key):
        def clean_function(clean_function_name):
            def func_wrapper(key, val):
                return clean_function_name(key, val)
            cls._add_callback(key, clean_function_name)
            return func_wrapper
        return clean_function


    @classmethod
    def loop_through_json(cls, json_dict):
        modified_object = {}
        for key, val in json_dict.iteritems():
            if cls.clean_functions.get(key):
                new_key, new_val = cls.clean_functions[key](key, val)
            else:
                new_key, new_val = key, val
            modified_object[new_key] = new_val
        return modified_object


    @classmethod
    def stream_json(cls, json_data):
        modified_objects = []
        for json_object in json_data:
            if type(json_object) == str:
                try:
                    json_dict = json.loads(json_object)
                except ValueError:
                    print 'invalid JSON!'
                    continue
            else:
                json_dict = json_object
            modified_object = cls.loop_through_json(json_dict)
            modified_objects.append(modified_object)
        return modified_objects

