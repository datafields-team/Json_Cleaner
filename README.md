# Json_Cleaner
Json_Cleaner is a Python library that's used to help write maintainable code to clean JSON based on its keys. It provides the ability to declaratively specify how a particular JSON field and its corresponding value are handled thereby making code less verbose and more maintainable.

## Demo

1. Replacing a JSON field with a different name
      
    ```python
    from cleaner import JSONCleaner
    
    replacement_keys = {
        'rate_of_interest': {'new_key': 'interest_rate', 'return_type': float},
    }
    
    
    if __name__ == '__main__':
        data = {'rate_of_interest': '3'}
        JSONCleaner.replace_keys(replacement_keys)
        clean_data = JSONCleaner.clean_json(data)
        # clean_data has {'interest_rate': 3.0}
    ```
    
    As simple as that.
    
2. More complex handling of a particular field
    
    ```python
    
    # For data such as this:
    # {'geo_coordinates': [['54.3321', '23.1134'], ['-75.1223', '-60.6656'], ['10.3302', '11.0029']]}
    
    
    # This callback gets registered and is later called in the 'clean_json' function
    @JSONCleaner.key_clean('geo_coordinates')
    def clean_coordinates(key, val):
        if val:
            geo_coordinates = []
            geo_coords = [coords.strip() for coords in val.split(';')]
            for coords in geo_coords:
                coordinates = coords.split(',')
                coordinates = [float(c) for c in coordinates]
                geo_coordinates.append(coordinates)
            return {'lgc': geo_coordinates}
        else:
            return None
            
    
    ```
