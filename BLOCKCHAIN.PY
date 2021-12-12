'''
BUILDING A SIMPLE BLOCKCHAIN
EG: NEUURAL COIN (NC)
transactions:
t1=anny 2 NC to Bob
t2 =Bob  4NC to Max
t3=Max 5NC to rohan

let's make our 1st block
here "AAA" is intital message and t1,t2,t3 are the transactions 
B1("AAA",t1,t2,t3)--->76fd34 : hexadecimal hash code uniques for each block
B2("76fd34",t4,t5,t6)--->89gh43

Neural Hash : generate new hashes and combine the hashes and if you don't have 1st hash it will concatenate the initialization  messages
or these hexadecimal code ewill convert to string and then apeend to transactions
'''

import hashlib
class NeuralCoinBlock:
    #constructor
    def __init__(self,previous_block_hash,transaction_list):
        self.previous_block_hash=previous_block_hash
        self.transaction_list=transaction_list
        self.block_data="-".join(transaction_list)+"-"+previous_block_hash
        self.block_hash=hashlib.sha256(self,block_data.encode()).hexdigest()

t1="anny sends 2 NC to Bob"
t2 ="Bob sends 4NC to Max"
t3="Max sends 5NC to rohan"
t4="rohan sends 2 NC to akku"
t5 ="akku sends 4NC to bhavesh"
t6="bhavesh sends 5NC to divya"

initial_block=NeuralCoinBlock("initial string",[t1,t2])
print(initial_block.block_data)
print(initial_block.block_hash)

second_block=NeuralCoinBlock(initial_block.block_hash,[t3,t4])
print(second_block.block_data)
print(second_block.block_hash)

third_block=NeuralCoinBlock(second_block.block_hash,[t5,t6])
print(third_block.block_data)
print(third_block.block_hash)
