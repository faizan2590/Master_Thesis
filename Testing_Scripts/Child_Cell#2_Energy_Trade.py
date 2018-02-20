
# coding: utf-8

# In[2]:



import json
import time
import datetime
import requests
import math
import random

from web3 import Web3, KeepAliveRPCProvider, IPCProvider, HTTPProvider


# In[3]:


#web3 provider
web3 = Web3(HTTPProvider("http://127.0.0.1:8545", request_kwargs={'timeout': 600}))

coinbase = web3.eth.coinbase
web3.eth.defaultBlock = "latest"
transaction = {'from': coinbase}


# In[4]:


# define the adress, ABI (with parsing from str to JSON) and define the contract object
Oliorigin_address = '0xcf457b3b22c01131245dbeeb8766a0d938861bff'
Oliorigin_abi_str  = '[{"constant":true,"inputs":[{"name":"_account","type":"address"}],"name":"get_oliType","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"_account","type":"address"}],"name":"get_oliCkt","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"kill","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"_account","type":"address"}],"name":"get_oliTrafoid","outputs":[{"name":"","type":"uint32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"_tid","type":"uint32"}],"name":"get_gsoAddr","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"_account","type":"address"},{"name":"_index","type":"uint8"}],"name":"get_oliPeakLoad","outputs":[{"name":"","type":"uint16"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"oli","type":"address"},{"name":"lat","type":"uint32"},{"name":"long","type":"uint32"},{"name":"trafo","type":"uint32"},{"name":"ckt","type":"uint8"},{"name":"typex","type":"uint8"},{"name":"pload","type":"uint16[]"}],"name":"addOli","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"anonymous":false,"inputs":[{"indexed":false,"name":"paymentAddress","type":"address"},{"indexed":false,"name":"latOfLocation","type":"uint32"},{"indexed":false,"name":"longOfLocation","type":"uint32"}],"name":"newAddedOli","type":"event"}]'
Oliorigin_abi      = json.loads(Oliorigin_abi_str)
Oliorigin_contract = web3.eth.contract(abi=Oliorigin_abi,address=Oliorigin_address)


# In[5]:


# define the adress, ABI (with parsing from str to JSON) and define the contract object
Olicoin_address = '0x9b18b1509c6f12eaaf8c7d91b76cd8c8d1950467'
Olicoin_abi_str  = '[{"constant":false,"inputs":[],"name":"kill","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"caddress","type":"address"}],"name":"get_coinBalance","outputs":[{"name":"","type":"int32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_contract","type":"address"},{"name":"_tf","type":"bool"}],"name":"set_ContractAddress","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_account","type":"address"},{"name":"_change","type":"int32"}],"name":"set_OliCoinBalance","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_amount","type":"uint16"}],"name":"transfer","outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_from","type":"address"},{"indexed":true,"name":"_to","type":"address"},{"indexed":false,"name":"_value","type":"uint16"}],"name":"Transfer","type":"event"}]'
Olicoin_abi      = json.loads(Olicoin_abi_str)
Olicoin_contract = web3.eth.contract(abi=Olicoin_abi,address=Olicoin_address)


# In[6]:


# define the adress, ABI (with parsing from str to JSON) and define the contract object
Olidaughter_address = '0x356d7468850ec18f94db888e9e2b0f065c05b725'
Olidaughter_abi_str  = '[{"constant":false,"inputs":[{"name":"addr","type":"address"}],"name":"setOliOrigin","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_amount","type":"uint16"},{"name":"_rate","type":"uint8"}],"name":"bid","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"addr","type":"address"}],"name":"setBilateralTrading","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"addr","type":"address"}],"name":"setOliCoin","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"addr","type":"address"}],"name":"setDynamicGridFee","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[],"name":"kill","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[],"name":"resett","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"get_producer","outputs":[{"name":"","type":"address[]"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"_rate","type":"uint8"}],"name":"get_sRate","outputs":[{"name":"","type":"uint16"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"get_consumer","outputs":[{"name":"","type":"address[]"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"_rate","type":"uint8"}],"name":"get_dRate","outputs":[{"name":"","type":"uint16"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"maxRate","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"breakEven","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"name":"gaddr","type":"address"},{"indexed":false,"name":"grate","type":"uint8"},{"indexed":false,"name":"gamount","type":"uint16"}],"name":"NewGenBid","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"caddr","type":"address"},{"indexed":false,"name":"crate","type":"uint8"},{"indexed":false,"name":"camount","type":"uint16"}],"name":"NewConBid","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"cbid","type":"uint8"}],"name":"NewMcp","type":"event"}]'
Olidaughter_abi      = json.loads(Olidaughter_abi_str)
Olidaughter_contract = web3.eth.contract(abi=Olidaughter_abi,address=Olidaughter_address)


# In[7]:


# define the adress, ABI (with parsing from str to JSON) and define the contract object
DynamicGridFee_address = '0x39a51aab23d4eddb1500ec2f2d2ea1d51771ccee'
DynamicGridFee_abi_str  = '[{"constant":true,"inputs":[{"name":"_tid","type":"uint32"},{"name":"_index","type":"uint8"}],"name":"get_gridFee","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_addr","type":"address"},{"name":"_amount","type":"uint16"}],"name":"set_trafocamount","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"addr","type":"address"}],"name":"setOliOrigin","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"_tid","type":"uint32"}],"name":"get_trafoLoad","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_addr","type":"address"},{"name":"_amount","type":"uint16"}],"name":"set_cktcamount","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[],"name":"kill","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_tid","type":"uint32"}],"name":"set_tgridFee","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"_tid","type":"uint32"}],"name":"get_trafoPeakLoad","outputs":[{"name":"","type":"uint16"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"_tid","type":"uint32"},{"name":"_index","type":"uint8"}],"name":"get_cktAmount","outputs":[{"name":"","type":"int16"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"_addr","type":"address"}],"name":"get_tGFee","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_address","type":"address"},{"name":"_fee","type":"uint8[]"}],"name":"set_minmaxgfee","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_addr","type":"address"},{"name":"_amount","type":"uint16"}],"name":"set_traforamount","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"_addr","type":"address"}],"name":"get_dGFee","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_tid","type":"uint32"}],"name":"set_dgridFee","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_addr","type":"address"},{"name":"_amount","type":"uint64"}],"name":"set_cktramount","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"_addr","type":"address"}],"name":"get_trafoAmount","outputs":[{"name":"","type":"int16"}],"payable":false,"stateMutability":"view","type":"function"}]'
DynamicGridFee_abi      = json.loads(DynamicGridFee_abi_str)
DynamicGridFee_contract = web3.eth.contract(abi=DynamicGridFee_abi,address=DynamicGridFee_address)


# In[8]:


#Ethereum Accounts/EOA
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


# In[50]:


#########DAUGHTER AUCTION########

#set oliorigin Address
web3.personal.unlockAccount(coinbase, 'felixfaizan')
Olidaughter_contract.transact({'from': coinbase}).setOliOrigin(Oliorigin_address)

#set OLIcoin address
web3.personal.unlockAccount(coinbase, 'felixfaizan')
Olidaughter_contract.transact({'from': coinbase}).setOliCoin(Olicoin_address)

#set DynamicGridFee address
web3.personal.unlockAccount(coinbase, 'felixfaizan')
Olidaughter_contract.transact({'from': coinbase}).setDynamicGridFee(DynamicGridFee_address)


# In[11]:


bids = [2500,4500,6500,6500,5500,5500,6500,6500]
i=0


# In[12]:


run = 1
while run == 1:
    web3.personal.unlockAccount(account_11, 'felixfaizan')
    Olidaughter_contract.transact({'from': account_11}).bid(bids[i], 5)

    web3.personal.unlockAccount(account_12, 'felixfaizan')
    Olidaughter_contract.transact({'from': account_12}).bid(random.randint(2000,2050), 10)

    web3.personal.unlockAccount(account_13, 'felixfaizan')
    Olidaughter_contract.transact({'from': account_13}).bid(random.randint(800,850), 12)

    web3.personal.unlockAccount(account_14, 'felixfaizan')
    Olidaughter_contract.transact({'from': account_14}).bid(random.randint(2000,2050), 13)

    web3.personal.unlockAccount(account_15, 'felixfaizan')
    Olidaughter_contract.transact({'from': account_15}).bid(random.randint(1550,1600), 14)

    #    time.sleep(15)

    web3.personal.unlockAccount(account_16, 'felixfaizan')
    Olidaughter_contract.transact({'from': account_16}).bid(random.randint(2200,2205), 7)

    web3.personal.unlockAccount(account_17, 'felixfaizan')
    Olidaughter_contract.transact({'from': account_17}).bid(random.randint(1500,1550), 9)

    web3.personal.unlockAccount(account_18, 'felixfaizan')
    Olidaughter_contract.transact({'from': account_18}).bid(random.randint(2300,2350), 11)

    web3.personal.unlockAccount(account_19, 'felixfaizan')
    Olidaughter_contract.transact({'from': account_19}).bid(random.randint(1000,1050), 12)

    web3.personal.unlockAccount(account_20, 'felixfaizan')
    Olidaughter_contract.transact({'from': account_20}).bid(random.randint(3000,3050), 13)

    i=i+1
    time.sleep(60)
    
    #MCP
    web3.personal.unlockAccount(account_19, 'felixfaizan')
    Olidaughter_contract.transact({'from': account_19}).breakEven()    

    time.sleep(60)
    
    #Resett
    web3.personal.unlockAccount(account_20, 'felixfaizan')
    Olidaughter_contract.transact({'from': account_20}).resett()
    
    time.sleep(60)


# In[58]:


web3.personal.unlockAccount(account_11, 'felixfaizan')
Olidaughter_contract.transact({'from': account_11}).bid(bids[i], 5)

web3.personal.unlockAccount(account_12, 'felixfaizan')
Olidaughter_contract.transact({'from': account_12}).bid(random.randint(2000,2050), 10)

web3.personal.unlockAccount(account_13, 'felixfaizan')
Olidaughter_contract.transact({'from': account_13}).bid(random.randint(800,850), 12)

web3.personal.unlockAccount(account_14, 'felixfaizan')
Olidaughter_contract.transact({'from': account_14}).bid(random.randint(2000,2050), 13)

web3.personal.unlockAccount(account_15, 'felixfaizan')
Olidaughter_contract.transact({'from': account_15}).bid(random.randint(1550,1600), 14)

#    time.sleep(15)

web3.personal.unlockAccount(account_16, 'felixfaizan')
Olidaughter_contract.transact({'from': account_16}).bid(random.randint(2200,2205), 7)

web3.personal.unlockAccount(account_17, 'felixfaizan')
Olidaughter_contract.transact({'from': account_17}).bid(random.randint(1500,1550), 9)

web3.personal.unlockAccount(account_18, 'felixfaizan')
Olidaughter_contract.transact({'from': account_18}).bid(random.randint(2300,2350), 11)

web3.personal.unlockAccount(account_19, 'felixfaizan')
Olidaughter_contract.transact({'from': account_19}).bid(random.randint(1000,1050), 12)

web3.personal.unlockAccount(account_20, 'felixfaizan')
Olidaughter_contract.transact({'from': account_20}).bid(random.randint(3000,3050), 13)

i=i+1


# In[59]:


#MCP
web3.personal.unlockAccount(account_19, 'felixfaizan')
Olidaughter_contract.transact({'from': account_19}).breakEven()    


# In[9]:


#Resett
web3.personal.unlockAccount(account_20, 'felixfaizan')
Olidaughter_contract.transact({'from': account_20}).resett()

