########################################
# Hash Table
# Author : Tom Choi
########################################

class HashNode:
    __slots__ = ["key", "value", "deleted"]

    def __init__(self, key, value, deleted=False):
        self.key = key
        self.value = value
        self.deleted = deleted

    def __repr__(self):
        return f"HashNode({self.key}, {self.value})"

    def __eq__(self, other):
        return self.key == other.key and self.value == other.value


class HashTable:
    """
    Hash Table Class
    """
    __slots__ = ['capacity', 'size', 'table', 'collisions', 'prime_index']

    primes = (
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83,
        89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179,
        181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277,
        281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389,
        397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499,
        503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617,
        619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739,
        743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859,
        863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991,
        997)

    def __init__(self, capacity=8):
        """
        Initializes hash table
        :param capacity: capacity of the hash table
        """
        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity

        i = 0
        while HashTable.primes[i] <= self.capacity:
            i += 1
        self.prime_index = i - 1

    def __eq__(self, other):
        """
        Equality operator
        :param other: other hash table we are comparing with this one
        :return: bool if equal or not
        """
        if self.capacity != other.capacity or self.size != other.size:
            return False
        for i in range(self.capacity):
            if self.table[i] != other.table[i]:
                return False
        return True

    def __repr__(self):
        """
        Represents the table as a string
        :return: string representation of the hash table
        """
        represent = ""
        bin_no = 0
        for item in self.table:
            represent += "[" + str(bin_no) + "]: " + str(item) + '\n'
            bin_no += 1
        return represent

    def __setitem__(self, key, value):
        """
        Allows for the use of the set operator to insert into table
        :param key: string key to insert
        :param value: value to insert
        :return: None
        """
        return self.insert(key=key, value=value)

    def __getitem__(self, item):
        """
        Allows get operator to retrieve a value from the table
        :param item: string key of item to retrieve from tabkle
        :return: HashNode
        """
        return self.get(item)

    def __contains__(self, item):
        """
        Checks whether a given key exists in the table
        :param item: string key of item to retrieve
        :return: Bool
        """
        if self.get(item) is not None:
            return True
        return False

    def _hash_1(self, key):
        """
        Converts a string x into a bin number for our hash table
        :param x: key to be hashed
        :return: bin number to insert hash item at in our table, -1 if x is an empty string
        """
        if not key:
            return None
        hashed_value = 0

        for char in key:
            hashed_value = 181 * hashed_value + ord(char)
        return hashed_value % self.capacity

    def _hash_2(self, key):
        """
        Converts a string x into a hash
        :param x: key to be hashed
        :return: a hashed value
        """
        if not key:
            return None
        hashed_value = 0

        for char in key:
            hashed_value = 181 * hashed_value + ord(char)

        prime = HashTable.primes[self.prime_index]

        hashed_value = prime - (hashed_value % prime)
        if hashed_value % 2 == 0:
            hashed_value += 1
        return hashed_value

    
    def hash(self, key, inserting=False):
        """
        Given a key string return an index in the hash table. Implements double hashing
        :param key: given key
        :param inserting: check if inserting or not
        :return: index
        """
        i = 0
        while i <= self.capacity:
            if inserting is True:
                returnIndex = (self._hash_1(key) + i * self._hash_2(key)) % self.capacity
                if self.table[returnIndex] is None or self.table[returnIndex].deleted:
                    break
                else:
                    i += 1
            elif inserting is False:
                returnIndex = (self._hash_1(key) + i * self._hash_2(key)) % self.capacity
                if self.table[returnIndex] is None or self.table[returnIndex].key == key:
                    break
                else:
                    i += 1
        return returnIndex

    def insert(self, key, value):
        """
        insert the key value pair into hash table
        :param key: given key
        :param value: given value
        :return: none
        """
        index = self.hash(key, inserting=True)
        self.table[index] = HashNode(key, value)
        self.size += 1

        if self.size / self.capacity >= 0.5:
            self.grow()

    def get(self, key):
        """
        find the hashnode by key in hashtable
        :param key: given key
        :return: hashnode if found, else none
        """
        index = self.hash(key)
        if self.table[index] is not None:
            if self.table[index].key == key:
                return self.table[index]
            else:
                return None

    def delete(self, key):
        """
        delete the hashnode which contains the key and leave as deleted node
        :param key: given key
        :return: none
        """
        if self.get(key):
            index = self.hash(key)
            self.table[index].key = None
            self.table[index].value = None
            self.table[index].deleted = True
            self.size -= 1
            return None

    def grow(self):
        """
        grow hashtable's size by 2 times
        :return: none
        """
        new_table = HashTable(self.capacity * 2)
        for i in range(0, self.capacity):
            if self.table[i] is not None and not self.table[i].deleted:
                new_table.insert(self.table[i].key, self.table[i].value)

        self.table = new_table.table
        self.size = new_table.size
        self.capacity = new_table.capacity
        self.prime_index = new_table.prime_index

def word_frequency(string, lexicon, table):
    """
    Given a string S with no spaces or punctuation and a list of words (lexicon) return the frequency of the longest
    words in the string.
    :param string: the given string
    :param lexicon: words in the list which are also in string
    :param table: empty hashtable
    :return: hashtable which has all the words in it
    """
    word = ""
    another_word = ""
    i = 0
    j = len(string)
    for item in lexicon:
        table.insert(item, 0)

    while 0 < len(string):

        word = string[i:j]
        if word != "":
            if table.get(word) is None:
                i += 1
                continue
            else:
                another_word = word
                string = string[0:i]
                i += 1
                j -= len(word)
                i = 0
                table.get(word).value += 1
        if i != 0 and i == j:
            string += another_word
            table.get(another_word).value -= 1
            i = j + 1
            j = len(string)

    if string == "":
        for item in lexicon:
            if not table.get(item):
                table.insert(item, 0)

    return table
