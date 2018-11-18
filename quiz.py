# import pdb; pdb.set_trace()
from cryptography.fernet import Fernet

key = 'TluxwB3fV_GWuLkR1_BzGs1Zk90TYAuhNMZP_0q4WyM='

# Oh no! The code is going over the edge! What are you going to do?

message = b'gAAAAABb7sKYXEDdJjAVKPVILMmMQ3YwkwBgddFdyIjr-jivvB9U3vMwhcbNJFzAXP95Pf7GJdAbZHcLUaq7wptrId5YgEzFpKO5z0uTd4TbnJj6aTt1BI6oaydwTXlT5zvss0GJ0sMKOimtZlw6IXzmX7hZMuK6n5edEkhnIyPtP3WmoKvSjbr_s6iXZk3bk7ORkOlsYZad'

def main():
    f = Fernet(key)
    print(f.decrypt(message))

if __name__ == "__main__":
    main()
