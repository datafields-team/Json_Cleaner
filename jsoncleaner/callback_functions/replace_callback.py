from callback_function import CallbackFunction

class ReplaceCallback(CallbackFunction):
    
    def __init__(self, old_key, new_key, datatype=unicode):
        CallbackFunction.__init__(self, old_key, new_key, datatype)


    def __call__(self, _, val):
        if val:
            return (self._new_key, self._datatype(val))
        else:
            return (None, None)
