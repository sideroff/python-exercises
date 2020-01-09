from Crypto.Hash import SHA256

def main():
    password = input("Password: ").encode("UTF-8")

    
    h = SHA256.new()
    h.update(password)

    print("Password hash: %s" % (h.hexdigest()))

if __name__ == '__main__': main()