class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def _get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def __setitem__(self, key, value):
        items = self.arr[self._get_hash(key)]
        index = None
        for i, pair in enumerate(items):
            if pair[0] == key:
                index = i
        if index is not None:
            self.arr[self._get_hash(key)][index] = (key, value)
        else:
            self.arr[self._get_hash(key)].append((key, value))

    def __getitem__(self, key):
        items = self.arr[self._get_hash(key)]
        for pair in items:
            if pair[0] == key:
                return pair[1]
        print(f'The key {key} does not exist')
        raise Exception(f'The key {key} does not exist')

    def __delitem__(self, key):
        items = self.arr[self._get_hash(key)]
        for i, pair in enumerate(items):
            if pair[0] == key:
                items.pop(i)


if __name__ == '__main__':
    table = HashTable()
    table['first_key'] = 'first_value'
    table['second_key'] = 'second_value'
    table['third_key'] = 'third_value'
    table['fourth_key'] = 'fourth_value'
    table['fifth_key'] = 'fifth_value'
    table['sixth_key'] = 'sixth_value'

    table['sixth_key'] = 'updated_sixth_value'
    table['fifth_key'] = 'updated_fifth_value'
    print(table['fifth_key'])
    print(table['sixth_key'])
    del table['fourth_key']
    print(table['fourth_key'])
    print(table.arr)
