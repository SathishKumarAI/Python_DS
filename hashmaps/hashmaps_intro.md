[How to Use HashMap in Python](https://www.turing.com/kb/how-to-use-hashmap-in-python)

1. Hashmap's are data structures that are used to store data in a key-value format.

2. They allow for reading and working with large datasets when looking for keys or values and make it faster to search for specific values in 0(1).

# How the hash function works


    def my_hash_func(key: str) -> int:
        hash_value = 17
        for ch in key:
            hash_value = hash_value * 31 + ord(ch)
        return hash_value 


collisions: in 

Chaining: 