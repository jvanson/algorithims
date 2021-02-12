class HashMap():
    def __init__(self):
        self.storage = []

    def hashit(self, key):
        hashkey = 0
        for char in key:
            charcode = ord(char)
            print(f'characode for {char} is {charcode}')
            hashkey += charcode
        print(f'my hash key {hashkey}')
        return hashkey


    def set(self, key, value):
        hashkey = self.hashit(key)
        # this doesn't work in python
        # but would in javascript or ruby. python
        # doesn't let you insert into an arbitrary index value
        self.storage[hashkey].push(key, value)

    def get(self, key):
        hashkey = self.hashit(key)
        for i in range self.storage:
            if i == hashkey:
                return self.storage[hashkey]



foo = HashMap()
print(foo.hashit('somevalue'))
