import datetime
from doctest import REPORT_CDIFF
import json
import hashlib
from operator import index
from pickle import FALSE
from unicodedata import name
from urllib import response
from flask import Flask , jsonify

class Blockchain():
    def __init__(self):
        self.chain = []
        self.transaction = 0
        self.create_block(nonce=1,previous_hash="0")

    def create_block(self,nonce,previous_hash):
        block = {
            "index":len(self.chain)+1,
            "timestamp":str(datetime.datetime.now()),
            "nonce":nonce,
            "data":self.transaction,
            "previous_hash":previous_hash
        }
        self.chain.append(block)
        return block

    def get_previous_block(self):
        return self.chain[-1] 

    def hash(self,block):
        encode_block = json.dumps(block,sort_keys=True).encode()
        return hashlib.sha256(encode_block).hexdigest()

    def proof_of_work(self,previous_nonce):

        new_nonce=1
        check_proof = False

        while check_proof is False:
            hashoperation =  hashlib.sha256(str(new_nonce**2 - previous_nonce**2).encode()).hexdigest()
            if hashoperation[:4] == "0000":
                check_proof = True
            else:
                new_nonce+=1
        return new_nonce

    def is_chain_valid(self,chain):
        previous_block = chain[0]
        block_index = 1
        while block_index<len(chain):
            block = chain[block_index]
            if block["previous_hash"] != self.hash(previous_block):
                return False
            previous_nonce = previous_block["nonce"]
            nonce = block["nonce"]
            hashoperation =  hashlib.sha256(str(nonce**2 - previous_nonce**2).encode()).hexdigest()
            if hashoperation[:4]!="0000":
                return False
            previous_block=block
            block_index+=1
        return True

app = Flask(__name__)
blockchain =  Blockchain()

@app.route('/')
def hello():
    return "<h1>Hello blockchian</h1>"


@app.route('/get_chain',methods=["GET"])
def get_chain():
    response={
        "chain":blockchain.chain,
        "length":len(blockchain.chain),
    }
    return jsonify(response),200

@app.route('/mining',methods=['GET'])
def mining_block():
    amount = 1000000
    blockchain.transaction = blockchain.transaction+amount
    previous_block = blockchain.get_previous_block()
    pervious_nonce =  previous_block["nonce"]

    nonce = blockchain.proof_of_work(pervious_nonce)

    previous_hash = blockchain.hash(previous_block)

    block =  blockchain.create_block(nonce,previous_hash)
    response = {
        "message":"Mining Block เรียบร้อย",
        "index":block ["index"],
        "timestamp":block["timestamp"],
        "data":block["data"],
        "nonce":block["nonce"],
        "previous_hash":block["previous_hash"]
    }
    return jsonify(response),200

@app.route('/is_valid',methods=['GET'])
def is_valid():
    is_valid = blockchain.is_chain_valid(blockchain.chain)
    if is_valid:
        response={"message":"Blockchain is valid"}
    else:
        response={"message":"have Problem, blockchain is not valid"}
    return jsonify(response),200

if __name__ == "__main__":
    app.run()