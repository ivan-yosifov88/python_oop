class dictionary_iter:
    def __init__(self, dict_object):
        self.dict_object = dict_object
        self.dict_keys = list(dict_object.keys())
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.dict_keys):
            raise StopIteration
        key = self.dict_keys[self.index]
        value = self.dict_object[key]
        self.index += 1
        return key, value

result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
