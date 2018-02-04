
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


# In[5]:


# define the adress, ABI (with parsing from str to JSON) and define the contract object
Olibilateral_address = '0x642ad95fa0b08913f8bf941eb5d8667d781eb232'
Olibilateral_abi_str  = '[{"constant":false,"inputs":[{"name":"addr","type":"address"}],"name":"setOliOrigin","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_stock","type":"address"},{"name":"_rate","type":"uint8"}],"name":"stockBidding","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"_stock","type":"address"}],"name":"get_stockAmount","outputs":[{"name":"","type":"uint16"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"kill","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_amount","type":"uint16"},{"name":"_rate","type":"uint8"},{"name":"_period","type":"uint32"},{"name":"_btime","type":"uint32"}],"name":"regStock","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"_stock","type":"address"}],"name":"get_stockBidder","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"_stock","type":"address"}],"name":"get_stockRate","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"anonymous":false,"inputs":[{"indexed":false,"name":"saccount","type":"address"},{"indexed":false,"name":"samount","type":"uint16"},{"indexed":false,"name":"smrate","type":"uint8"},{"indexed":false,"name":"speriod","type":"uint32"},{"indexed":false,"name":"sbiddingTime","type":"uint32"}],"name":"NewStock","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"baccount","type":"address"},{"indexed":false,"name":"bmrate","type":"uint8"}],"name":"NewStockBid","type":"event"}]'
Olibilateral_abi      = json.loads(Olibilateral_abi_str)
Olibilateral_contract = web3.eth.contract(abi=Olibilateral_abi,address=Olibilateral_address)


# In[18]:


#Ethereum Accounts
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


# In[56]:



#########BILATERAL TRADE#########
#set oli origin Address
web3.personal.unlockAccount(coinbase, 'felixfaizan')
Olibilateral_contract.transact({'from': coinbase}).setOliOrigin(Oliorigin_address)


# In[40]:


###BILATERAL TRADE####
#Stock registering
web3.personal.unlockAccount(account_5, 'felixfaizan')
Olibilateral_contract.transact({'from': account_5}).regStock(5, 5, 108000, 240)
time.sleep(30)

#Stock Biddings
web3.personal.unlockAccount(account_6, 'felixfaizan')
Olibilateral_contract.transact({'from': account_6}).stockBidding(account_5, 7)
time.sleep(30)

web3.personal.unlockAccount(account_7, 'felixfaizan')
Olibilateral_contract.transact({'from': account_7}).stockBidding(account_5, 8)
time.sleep(30)

web3.personal.unlockAccount(account_8, 'felixfaizan')
Olibilateral_contract.transact({'from': account_8}).stockBidding(account_5, 9)
time.sleep(30)

