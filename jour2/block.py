from hashlib import sha256
import sys
from datetime import datetime
import json
import os

class Block:
    def __init__(self, previousBlock, signature, data, id):
        self.id = id
        self.previousBlock = previousBlock
        self.signature = signature
        self.data = data
        self.timestamp =  datetime.now()
        self.nonce = 0

    # get functions
    def get_Hash(self):
        return self.hash

    def get_Id(self):
        return self.id
    
    def get_previousBlock(self):
        return self.previousBlock
    
    def get_signature(self):
        return self.signature

    def get_timestamp(self):
            return self.timestamp
      
    def get_nonce(self):
            return self.nonce

    def get_data(self):
            return self.data

    # hashing functions
    def hashing(self):
        block = str(self.signature) + str(self.timestamp) + str(self.data) + str(self.nonce)
        return(sha256(block.encode('utf-8')).hexdigest())
        
    def hashCheck(self):
        hashed = self.hashing()
        while hashed[0:3] != '000':
            self.nonce += 1
            hashed = self.hashing()
        else:
            self.hash = hashed

    # printing functions
    def __str__(self):       
        return self.blockJsonify()

    def blockJsonify(self):
        values = {
            'id': self.id,
            'previous_hash': str(self.previousBlock),
            'timestamp': str(self.timestamp),
            'signature': str(self.signature),
            'data': str(self.data), 
            'hash': str(self.hash),
            'nonce': str(self.nonce),
        }
        return values

#  -------------------- CECI EST LA BLOCKCHAIN ---------------------------------

class Blockchain:
    def __init__(self):
        self.location = "jour2/blockchain.json"
        self.blockList = []


    # get functions
    def getAllBlocks(self):
        with open(self.location, 'r') as jsonfile:
            self.blockList = json.load(jsonfile)
    
    def amISecure(self):
        for i in range(0, len(self.blockList)):
            if i !=0 and self.blockList[i - 1]["hash"] != self.blockList[i]["previous_hash"]:
                return False
        return True
        
    def getLastHash(self):
        return self.blockList[-1]["hash"]

    def getLastBlockId(self):
        return self.blockList[-1]["id"]

    def getBlockById(self, id):
        for i in self.blockList:
            if i['id'] == id:
                self.blockList = i

    # actions

    def createBlock(self, signature, data):
        lastBlockId = self.getLastBlockId() + 1
        
        block = Block( self.getLastHash(), signature, data, lastBlockId)
        block.hashCheck()
        self.blockList.append(block.blockJsonify())
        os.remove(self.location)
        with open(self.location, 'w') as jsonfile:
            json.dump(self.blockList, jsonfile, indent=4)

    def deleteLastBlock(self):
        self.blockList.pop(-1)
        os.remove(self.location)
        with open(self.location, 'w') as jsonfile:
            json.dump(self.blockList, jsonfile, indent=4)
    
#   printing functions

    def printLastBlock(self):
        lastBlock = self.blockList[-1]
        for value in lastBlock:
            print(value + ': ' + str(lastBlock[value]))

    def printAllBlocks(self):
        i = 0
        for item in self.blockList:
            for value in item:
                print(value + ': ' + str(item[value]))
            print()

    def printBlockById(self, id):
        self.getBlockById(id)
        for value in self.blockList:
            print(value + ': ' + str(self.blockList[value]))

    def printAmISecure(self):
        if(self.amISecure() == True):
            print("This blockchain is secure and operational")
        if(self.amISecure() == False):
            answer = input("This blockchain is not secure would you like to delete blocks to correct it(Yes or No) ?")
            answer.lower()
            if answer == "yes" or answer == "y":
                while self.amISecure() == False:
                    self.deleteLastBlock()
            elif answer == "no" or answer == "n":
                sys.exit()
            else:
                self.printAmISecure()

def retry():
    answer = input("Does not match. Would you like to retry(Yes or No) ?")
    answer.lower()
    if answer == "yes" or answer == "y":
        main()
    elif answer == "no" or answer == "n":
        sys.exit()
    else:
        retry()

def main():
    blockchain = Blockchain()
    blockchain.getAllBlocks()
    function = input("What do you want (add (1), checkBlock(2), getAll(3), getLastBlock(4), deleteLastBlock(5), securityCheck(6)): ")
    if str(function) == '1': 
        signature = input("Enter the signature of your block: ")
        data = input("Enter the data of your block: ")
        blockchain.createBlock(signature, data)
        print("Your block has been added")
    elif str(function) == '2':
        id = int(input("Enter the id of your block: "))
        blockchain.printBlockById(id)
    elif str(function) == '3':
        blockchain.printAmISecure()
        blockchain.printAllBlocks()
    elif str(function) == '4':
        blockchain.printLastBlock()
    elif str(function) == '5':
        blockchain.deleteLastBlock()
        print('Le dernier block a bien été supprimé')
    elif str(function) == '6':
        blockchain.printAmISecure()
    else:
        retry()
main()
