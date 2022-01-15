'''
Implement HashTable from scractch.
'''

from typing import ItemsView


class HashTable:
    def __init__(self, size):
        self.size = size 
        self.hash_table = self.createBucket()

    # Create bucket for the hashtable
    # [[], [], [], []]
    def createBucket(self):
        return [[]for _ in range(self.size)]

    #set value inside the hashtable
    def set_value(self, key, val):
        hashed_key = hash(key) % self.size
        bucket = self.hash_table[hashed_key]
        isExist = False 
        for index, record in enumerate(bucket):
            record_key, record_val = record 

            if(record_key == key):
                isExist = True
                break 

        if(isExist):
            #Update 
            bucket[index] = (key, val)
        else:
            #Inset 
            bucket.append((key, val))

    
    #get value from the table 
    def get_value(self, key):
        hashed_key = hash(key) % self.size
        bucket = self.hash_table[hashed_key]
        isExist = False
        for k, v in enumerate(bucket):
            r_key, r_val = v 
            if(r_key == key):
                isExist = True
                break 
        if(isExist):
            return r_val
        else:
            return "Not found"

    # Remove a value with specific key
    def delete_val(self, key):
        
        # Get the index from the key using
        # hash function
        hashed_key = hash(key) % self.size
          
        # Get the bucket corresponding to index
        bucket = self.hash_table[hashed_key]
  
        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record
              
            # check if the bucket has same key as
            # the key to be deleted
            if record_key == key:
                found_key = True
                break
        if found_key:
            bucket.pop(index)
        return
    
    def __str__(self):
        return "".join(str(item) for item in self.hash_table)


if __name__ == "__main__":
    hash_table = HashTable(50)
  
    # insert some values
    hash_table.set_value('gfg@example.com', 'some value')
    print(hash_table)
    print()
    
    hash_table.set_value('portal@example.com', 'some other value')
    print(hash_table)
    print()
    
    # search/access a record with key
    print(hash_table.get_value('portal@example.com'))
    print()
    
    # delete or remove a value
    hash_table.delete_val('portal@example.com')
    print(hash_table)