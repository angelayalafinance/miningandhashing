from hashlib import sha256
import time

MAX_NONCE = 1000000000000


def SHA256(text):
    return sha256(text.encode("ascii")).hexdigest()


def mine(input, prefix_zeros):
    
    prefix_str = '0' * prefix_zeros #Prefix string is x amount of zeros
    
    for nonce in range(MAX_NONCE):
        text = input + str(nonce)    #Hash is string input + nonce
        new_hash = SHA256(text)
        if new_hash.startswith(prefix_str): #If prefix string is x amount of zeros
            print(f"Yay! Successfully mined bitcoins with nonce value: {input}{nonce}")
            return new_hash

    raise BaseException(f"Couldn't find correct has after trying {MAX_NONCE} times")
    
    
    
    
    
if __name__=='__main__':
    input ='Angel Humberto '
    zeros=7 # try changing this to higher number and you will see it will take more time for mining as difficulty increases
    start = time.time()
    print("Start Mining!")
    new_hash = mine(input, zeros)
    
    total_time = str((time.time() - start)) #   keep track of time
    print(f"Mining took: {total_time} seconds")
    print(new_hash)
