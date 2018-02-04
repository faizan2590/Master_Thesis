
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


# In[18]:


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


# In[53]:


#Register OLIs/Agents

web3.personal.unlockAccount(coinbase, 'felixfaizan')

Oliorigin_contract.transact({'from': coinbase}).addOli(account_1, int(49.30e4), int(8.35e4), 67376, 0, 0, [1000])
Oliorigin_contract.transact({'from': coinbase}).addOli(account_2, int(48.39e4), int(9.97e4), 67376, 1, 3, [1000])
Oliorigin_contract.transact({'from': coinbase}).addOli(account_3, int(48.77e4), int(9.16e4), 67376, 0, 5, [1000])
Oliorigin_contract.transact({'from': coinbase}).addOli(account_4, int(49.40e4), int(8.67e4), 67376, 1, 0, [1000])
Oliorigin_contract.transact({'from': coinbase}).addOli(account_5, int(48.89e4), int(9.20e4), 67376, 0, 5, [1000])


Oliorigin_contract.transact({'from': coinbase}).addOli(account_6, int(48.62e4), int(9.83e4), 67376, 0, 6, [1000])
Oliorigin_contract.transact({'from': coinbase}).addOli(account_7, int(48.00e4), int(7.84e4), 67376, 1, 6, [1000])
Oliorigin_contract.transact({'from': coinbase}).addOli(account_8, int(49.49e4), int(8.47e4), 67376, 0, 7, [1000])
Oliorigin_contract.transact({'from': coinbase}).addOli(account_9, int(49.32e4), int(8.44e4), 67376, 1, 7, [1000])
Oliorigin_contract.transact({'from': coinbase}).addOli(account_10, int(48.41e4), int(10.00e4), 67376, 0, 7, [1000])


Oliorigin_contract.transact({'from': coinbase}).addOli(account_11, int(48.69e4), int(9.21e4), 67377, 0, 0, [1000])
Oliorigin_contract.transact({'from': coinbase}).addOli(account_12, int(49.47e4), int(8.47e4), 67377, 1, 3, [1000])
Oliorigin_contract.transact({'from': coinbase}).addOli(account_13, int(48.42e4), int(10.07e4), 67377, 0, 5, [1000])
Oliorigin_contract.transact({'from': coinbase}).addOli(account_14, int(48.80e4), int(9.22e4), 67377, 1, 0, [1000])
Oliorigin_contract.transact({'from': coinbase}).addOli(account_15, int(48.87e4), int(9.22e4), 67377, 0, 5, [1000])


Oliorigin_contract.transact({'from': coinbase}).addOli(account_16, int(48.87e4), int(9.19e4), 67377, 0, 6, [1000])
Oliorigin_contract.transact({'from': coinbase}).addOli(account_17, int(48.81e4), int(9.18e4), 67377, 1, 6, [1000])
Oliorigin_contract.transact({'from': coinbase}).addOli(account_18, int(48.40e4), int(9.96e4), 67377, 0, 7, [1000])
Oliorigin_contract.transact({'from': coinbase}).addOli(account_19, int(48.50e4), int(10.06e4), 67377, 1, 7, [1000])
Oliorigin_contract.transact({'from': coinbase}).addOli(account_20, int(48.60e4), int(10.16e4), 67377, 0, 7, [1000])


# In[ ]:


#Register DSOs

web3.personal.unlockAccount(coinbase, 'felixfaizan')
Oliorigin_contract.transact({'from': coinbase}).addOli(account_21, int(49.30e4), int(8.35e4), 67376, 2, 8, [1000, 750, 750])
Oliorigin_contract.transact({'from': coinbase}).addOli(account_22, int(48.69e4), int(9.21e4), 67377, 2, 8, [1000, 750, 750])

