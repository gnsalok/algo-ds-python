'''
Implement a Hash Function / Hash Function.

HashMap
Key - Value 
(1 : Alok)
(2 : Jeff)

Steps :
1. Create bucket of size of table 
2. INSERT : Create hash key [hash(key)%size], check if already exist. If yes, then update else append.
3. GET : Get hash key, find bucket from hashkey. Check if key exist, If yes,then return value else return None.
4. DELETE : Get hash key, find bucket from hashkey. Check if key exist, If yes, POP element else return. 
5. PRINT : Print element in the list

'''

class HashTable:
    def __init__(self, size):
        self.size = size
        self.hash_table = self.create_bucket()

        
    # Create bucket 
    def create_bucket(self):
        return [[] for _ in range(self.size)]

    # Insert value in the map 
    def set_val(self, key, val):
        #create hash 
        hashed_key = hash(key) % self.size

        print("Hashed", hash(key), " -- Hashed Value", hashed_key)

        #get bucket corr. index 
        bucket = self.hash_table[hashed_key]

        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record   # [(record_key, record_val),(record_key, record_val)]

            # check if the bucket has same key as
            # the key to be inserted
            if record_key == key:
                found_key = True
                break

        # If the bucket has same key as the key to be inserted,
        # Update the key value
        # Otherwise append the new key-value pair to the bucket
        if found_key:
            bucket[index] = (key, val)
        else:
            bucket.append((key, val))
            

    # Return searched value with specific key
    def get_val(self, key):
        
        # Get the index from the key using
        # hash function
        hashed_key = hash(key) % self.size
          
        # Get the bucket corresponding to index
        bucket = self.hash_table[hashed_key]
  
        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record
              
            # check if the bucket has same key as 
            # the key being searched
            if record_key == key:
                found_key = True
                break
  
        # If the bucket has same key as the key being searched,
        # Return the value found
        # Otherwise indicate there was no record found
        if found_key:
            return record_val
        else:
            return "No record found"

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

    # To print the items of hash map
    def __str__(self):
        return "".join(str(item) for item in self.hash_table)



if __name__ == "__main__":
    hash_table = HashTable(50)
  
    # insert some values
    hash_table.set_val('gfg@example.com', 'some value')
    print(hash_table)
    print()
    
    hash_table.set_val('portal@example.com', 'some other value')
    print(hash_table)
    print()
    
    # search/access a record with key
    print(hash_table.get_val('portal@example.com'))
    print()
    
    # delete or remove a value
    hash_table.delete_val('portal@example.com')
    print(hash_table)



            





