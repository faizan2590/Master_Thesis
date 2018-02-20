
# coding: utf-8

# In[1]:


# coding: utf-8

import json
import time
import datetime
import requests
import math
import random

from web3 import Web3, KeepAliveRPCProvider, IPCProvider, HTTPProvider


# In[2]:


#web3 provider
web3 = Web3(HTTPProvider("http://127.0.0.1:8545", request_kwargs={'timeout': 600}))

coinbase = web3.eth.coinbase
web3.eth.defaultBlock = "latest"
transaction = {'from': coinbase}


# In[3]:


# define the adress, ABI (with parsing from str to JSON) and define the contract object
Oliorigin_address = '0xcf457b3b22c01131245dbeeb8766a0d938861bff'
Oliorigin_abi_str  = '[{"constant":true,"inputs":[{"name":"_account","type":"address"}],"name":"get_oliType","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"_account","type":"address"}],"name":"get_oliCkt","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"kill","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"_account","type":"address"}],"name":"get_oliTrafoid","outputs":[{"name":"","type":"uint32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"_tid","type":"uint32"}],"name":"get_gsoAddr","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"_account","type":"address"},{"name":"_index","type":"uint8"}],"name":"get_oliPeakLoad","outputs":[{"name":"","type":"uint16"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"oli","type":"address"},{"name":"lat","type":"uint32"},{"name":"long","type":"uint32"},{"name":"trafo","type":"uint32"},{"name":"ckt","type":"uint8"},{"name":"typex","type":"uint8"},{"name":"pload","type":"uint16[]"}],"name":"addOli","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"anonymous":false,"inputs":[{"indexed":false,"name":"paymentAddress","type":"address"},{"indexed":false,"name":"latOfLocation","type":"uint32"},{"indexed":false,"name":"longOfLocation","type":"uint32"}],"name":"newAddedOli","type":"event"}]'
Oliorigin_abi      = json.loads(Oliorigin_abi_str)
Oliorigin_contract = web3.eth.contract(abi=Oliorigin_abi,address=Oliorigin_address)


# In[4]:


# define the adress, ABI (with parsing from str to JSON) and define the contract object
Olicoin_address = '0x9b18b1509c6f12eaaf8c7d91b76cd8c8d1950467'
Olicoin_abi_str  = '[{"constant":false,"inputs":[],"name":"kill","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"caddress","type":"address"}],"name":"get_coinBalance","outputs":[{"name":"","type":"int32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_contract","type":"address"},{"name":"_tf","type":"bool"}],"name":"set_ContractAddress","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_account","type":"address"},{"name":"_change","type":"int32"}],"name":"set_OliCoinBalance","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_amount","type":"uint16"}],"name":"transfer","outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_from","type":"address"},{"indexed":true,"name":"_to","type":"address"},{"indexed":false,"name":"_value","type":"uint16"}],"name":"Transfer","type":"event"}]'
Olicoin_abi      = json.loads(Olicoin_abi_str)
Olicoin_contract = web3.eth.contract(abi=Olicoin_abi,address=Olicoin_address)


# In[5]:


# define the adress, ABI (with parsing from str to JSON) and define the contract object
Olidaughter_address = '0xb3cddc8da3ac6b1a348006cafe6fc39e4fde8442'
Olidaughter_abi_str  = '[{"constant":false,"inputs":[{"name":"addr","type":"address"}],"name":"setOliOrigin","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_amount","type":"uint16"},{"name":"_rate","type":"uint8"}],"name":"bid","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"addr","type":"address"}],"name":"setBilateralTrading","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"addr","type":"address"}],"name":"setOliCoin","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"addr","type":"address"}],"name":"setDynamicGridFee","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[],"name":"kill","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[],"name":"resett","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"get_producer","outputs":[{"name":"","type":"address[]"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"_rate","type":"uint8"}],"name":"get_sRate","outputs":[{"name":"","type":"uint16"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"get_consumer","outputs":[{"name":"","type":"address[]"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"_rate","type":"uint8"}],"name":"get_dRate","outputs":[{"name":"","type":"uint16"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"maxRate","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"breakEven","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"name":"gaddr","type":"address"},{"indexed":false,"name":"grate","type":"uint8"},{"indexed":false,"name":"gamount","type":"uint16"}],"name":"NewGenBid","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"caddr","type":"address"},{"indexed":false,"name":"crate","type":"uint8"},{"indexed":false,"name":"camount","type":"uint16"}],"name":"NewConBid","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"cbid","type":"uint8"}],"name":"NewMcp","type":"event"}]'
Olidaughter_abi      = json.loads(Olidaughter_abi_str)
Olidaughter_contract = web3.eth.contract(abi=Olidaughter_abi,address=Olidaughter_address)


# In[6]:


# define the adress, ABI (with parsing from str to JSON) and define the contract object
DynamicGridFee_address = '0x0ef2c74e908f2dd458c390f78a2486124280d7ec'
DynamicGridFee_abi_str  = '[{"constant":true,"inputs":[{"name":"_tid","type":"uint32"},{"name":"_index","type":"uint8"}],"name":"get_gridFee","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_addr","type":"address"},{"name":"_amount","type":"uint16"}],"name":"set_trafocamount","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"addr","type":"address"}],"name":"setOliOrigin","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_addr","type":"address"},{"name":"_amount","type":"uint16"}],"name":"set_cktcamount","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[],"name":"kill","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_tid","type":"uint32"}],"name":"set_tgridFee","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"_tid","type":"uint32"},{"name":"_index","type":"uint8"}],"name":"get_cktAmount","outputs":[{"name":"","type":"int16"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"_addr","type":"address"}],"name":"get_tGFee","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_address","type":"address"},{"name":"_fee","type":"uint8[]"}],"name":"set_minmaxgfee","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_addr","type":"address"},{"name":"_amount","type":"uint16"}],"name":"set_traforamount","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"_addr","type":"address"}],"name":"get_dGFee","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_tid","type":"uint32"}],"name":"set_dgridFee","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_addr","type":"address"},{"name":"_amount","type":"uint64"}],"name":"set_cktramount","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"_addr","type":"address"}],"name":"get_trafoAmount","outputs":[{"name":"","type":"int16"}],"payable":false,"stateMutability":"view","type":"function"}]'
DynamicGridFee_abi      = json.loads(DynamicGridFee_abi_str)
DynamicGridFee_contract = web3.eth.contract(abi=DynamicGridFee_abi,address=DynamicGridFee_address)


# In[7]:


#Ethereum accounts/EOA
account_0=web3.eth.accounts[0]
account_1=web3.eth.accounts[1]
account_2=web3.eth.accounts[2]
account_3=web3.eth.accounts[3]
account_4=web3.eth.accounts[4]
account_5=web3.eth.accounts[5]
account_6=web3.eth.accounts[6]
account_7=web3.eth.accounts[7]
account_8=web3.eth.accounts[8]
account_9=web3.eth.accounts[9]
account_10=web3.eth.accounts[10]
account_11=web3.eth.accounts[11]
account_12=web3.eth.accounts[12]
account_13=web3.eth.accounts[13]
account_14=web3.eth.accounts[14]
account_15=web3.eth.accounts[15]
account_16=web3.eth.accounts[16]
account_17=web3.eth.accounts[17]
account_18=web3.eth.accounts[18]
account_19=web3.eth.accounts[19]
account_20=web3.eth.accounts[20]
account_21=web3.eth.accounts[21]
account_22=web3.eth.accounts[22]


# In[8]:


#########DAUGHTER AUCTION########

#set oli origin Address

web3.personal.unlockAccount(coinbase, 'felixfaizan')
Olidaughter_contract.transact({'from': coinbase}).setOliOrigin(Oliorigin_address)

#set OLIcoin address
web3.personal.unlockAccount(coinbase, 'felixfaizan')
Olidaughter_contract.transact({'from': coinbase}).setOliCoin(Olicoin_address)


#set DynamicGridFee address
web3.personal.unlockAccount(coinbase, 'felixfaizan')
Olidaughter_contract.transact({'from': coinbase}).setDynamicGridFee(DynamicGridFee_address)


# In[12]:


bids = [4500,6500,7500,5500,5500,6500,6500]
i=0


# In[13]:


#Bid
run = 1
while run == 1:
    web3.personal.unlockAccount(account_1, 'felixfaizan')
    Olidaughter_contract.transact({'from': account_1}).bid(bids[i], 3)

    web3.personal.unlockAccount(account_2, 'felixfaizan')
    Olidaughter_contract.transact({'from': account_2}).bid(random.randint(1000,1050), 10)

    web3.personal.unlockAccount(account_3, 'felixfaizan')
    Olidaughter_contract.transact({'from': account_3}).bid(random.randint(500,550), 13)

    web3.personal.unlockAccount(account_4, 'felixfaizan')
    Olidaughter_contract.transact({'from': account_4}).bid(random.randint(2000,2050), 14)

    web3.personal.unlockAccount(account_5, 'felixfaizan')
    Olidaughter_contract.transact({'from': account_5}).bid(random.randint(1550,1600), 15)

    web3.personal.unlockAccount(account_6, 'felixfaizan')
    Olidaughter_contract.transact({'from': account_6}).bid(random.randint(1000,1050), 9)

    web3.personal.unlockAccount(account_7, 'felixfaizan')
    Olidaughter_contract.transact({'from': account_7}).bid(random.randint(1500,1550), 10)

    web3.personal.unlockAccount(account_8, 'felixfaizan')
    Olidaughter_contract.transact({'from': account_8}).bid(random.randint(2000,2550), 12)

    web3.personal.unlockAccount(account_9, 'felixfaizan')
    Olidaughter_contract.transact({'from': account_9}).bid(random.randint(1000,1050), 13)

    web3.personal.unlockAccount(account_10, 'felixfaizan')
    Olidaughter_contract.transact({'from': account_10}).bid(random.randint(3000,3050), 14)
    
    i=i+1

    time.sleep(60)
    
    #MCP
    web3.personal.unlockAccount(account_9, 'felixfaizan')
    Olidaughter_contract.transact({'from': account_9}).breakEven()    
    time.sleep(60)
    web3.personal.unlockAccount(account_10, 'felixfaizan')
    Olidaughter_contract.transact({'from': account_10}).resett()    
    time.sleep(60)


# In[11]:


web3.personal.unlockAccount(account_10, 'felixfaizan')
Olidaughter_contract.transact({'from': account_10}).resett()

