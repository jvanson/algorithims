class Hashmap:
    def __init__(self):
        self.storage = [None for _ in range(16)]
        print(f'here is storage: {self.storage}')

    def hashStr(self, key):
        if isinstance(key, int):
            return key

        result = 0
        for char in key:
            result += ord(char)
            #result = 1 * result + ord(char)
        print(f'here is result:{result}')
        return result

    def set(self, key, val):
        idx = self.hashStr(key)%16
        print(f'here is idx: {idx}')
        self.storage[idx] =  val

    def get(self, key):
        idx = self.hashStr(key)%16
        return self.storage[idx]

dict = Hashmap()
dict.set("jess", 1231231)
dict.set("val", 12930)
dict.set("anson", 'skdjf')
print(dict.get("val"))
print(dict.get("anson"))
print(dict.storage)
