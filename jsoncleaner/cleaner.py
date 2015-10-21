import json
from callback_functions.replace_callback import ReplaceCallback
from transforms.transformations import default_callback


class JsonCleaner(object):
    
    _clean_functions = {}


    @classmethod
    def _add_callback(cls, key, clean_function):
        cls._clean_functions[key] = clean_function
    

    @classmethod
    def keep_keys(cls, kept_keys):
        for key in kept_keys:
            cls._clean_functions[key] = default_callback
    

    @classmethod
    def replace_keys(cls, replaced_keys):
        for key, val in replaced_keys.iteritems():
            datatype = val.get('return_type') if val.get('return_type') else unicode
            replace_callback_function = ReplaceCallback(key, val['new_key'], datatype)
            cls._add_callback(key, replace_callback_function)


    @classmethod
    def key_clean(cls, key):
        def clean_function(clean_fn):
            def clean_function_wrapper(key, val):
                return clean_fn(key, val)
            cls._add_callback(key, clean_fn)
            return clean_function_wrapper
        return clean_function
    

    @classmethod
    def loop_through_json(cls, json_dict):
        modified_object = {}
        for key, val in json_dict.iteritems():
            if cls._clean_functions.get(key):
                new_key, new_val = cls._clean_functions[key](key, val)
            else:
                new_key, new_val = None, None
            if (new_key, new_val) != (None, None):
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
