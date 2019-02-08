#a wrapped dict which allows to be visited by a.b


class wrapped_dict(dict):

    def __init__(self, _dict):
        if type(_dict) == dict:
            for key in _dict.keys():
                self[key] = _dict[key]# if type(_dict[key]) != dict else wrapped_dict(_dict[key])
        return super(wrapped_dict, self).__init__()

    def __key(self, key):
        return "" if key is None else key.lower()

    def __getattr__(self, key):
        return self.get(self.__key(key))

    def __setattr__(self, key, value):
        self[self.__key(key)] = value

    def __getitem__(self, key):
        return super(wrapped_dict, self).get(self.__key(key))

    def __setitem__(self, key, value):
        super(wrapped_dict,self).__setitem__(self.__key(key), value)