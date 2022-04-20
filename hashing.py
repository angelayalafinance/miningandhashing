from hashlib import sha256

MAX_NONCE = 1000000000000


def SHA256(text):
    return sha256(text.encode("ascii")).hexdigest()


def mine(transactions, prefix_zeros):
    prefix_str = '0' * prefix_zeros
    for nonce in range(MAX_NONCE):
        text = transactions + str(nonce)
        new_hash = SHA256(text)
        if new_hash.startswith(prefix_str):
            print(f"Yay! Successfully mined bitcoins with nonce value:{nonce}")
            print(nonce)
            return new_hash

    raise BaseException(f"Couldn't find correct has after trying {MAX_NONCE} times")
    
    
    
if __name__=='__main__':
    transactions='Angel Humberto '
    difficulty=6 # try changing this to higher number and you will see it will take more time for mining as difficulty increases
    import time
    start = time.time()
    print("start mining")
    new_hash = mine(transactions, difficulty) #previous hash of already mined bitcoin
    total_time = str((time.time() - start))
    print(f"end mining. Mining took: {total_time} seconds")
    print(new_hash)