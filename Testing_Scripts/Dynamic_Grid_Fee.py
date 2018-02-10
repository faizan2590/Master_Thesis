
# coding: utf-8

# In[55]:


# coding: utf-8

import json
import time
import datetime
import requests
import math
import random

from web3 import Web3, KeepAliveRPCProvider, IPCProvider, HTTPProvider


# In[56]:


#web3 provider
web3 = Web3(HTTPProvider("http://127.0.0.1:8545", request_kwargs={'timeout': 600}))

coinbase = web3.eth.coinbase
web3.eth.defaultBlock = "latest"
transaction = {'from': coinbase}


# In[57]:


# define the adress, ABI (with parsing from str to JSON) and define the contract object
Oliorigin_address = '0xcf457b3b22c01131245dbeeb8766a0d938861bff'
Oliorigin_abi_str  = '[{"constant":true,"inputs":[{"name":"_account","type":"address"}],"name":"get_oliType","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"_account","type":"address"}],"name":"get_oliCkt","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"kill","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"_account","type":"address"}],"name":"get_oliTrafoid","outputs":[{"name":"","type":"uint32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"_tid","type":"uint32"}],"name":"get_gsoAddr","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"_account","type":"address"},{"name":"_index","type":"uint8"}],"name":"get_oliPeakLoad","outputs":[{"name":"","type":"uint16"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"oli","type":"address"},{"name":"lat","type":"uint32"},{"name":"long","type":"uint32"},{"name":"trafo","type":"uint32"},{"name":"ckt","type":"uint8"},{"name":"typex","type":"uint8"},{"name":"pload","type":"uint16[]"}],"name":"addOli","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"anonymous":false,"inputs":[{"indexed":false,"name":"paymentAddress","type":"address"},{"indexed":false,"name":"latOfLocation","type":"uint32"},{"indexed":false,"name":"longOfLocation","type":"uint32"}],"name":"newAddedOli","type":"event"}]'
Oliorigin_abi      = json.loads(Oliorigin_abi_str)
Oliorigin_contract = web3.eth.contract(abi=Oliorigin_abi,address=Oliorigin_address)


# In[58]:


# define the adress, ABI (with parsing from str to JSON) and define the contract object
DynamicGridFee_address = '0xbc53e6a4b58fbc6e22e4f280d664f6a1560b7904'
DynamicGridFee_abi_str  = '[{"constant":true,"inputs":[{"name":"_tid","type":"uint32"},{"name":"_index","type":"uint8"}],"name":"get_gridFee","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_addr","type":"address"},{"name":"_amount","type":"uint16"}],"name":"set_trafocamount","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"addr","type":"address"}],"name":"setOliOrigin","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_addr","type":"address"},{"name":"_amount","type":"uint16"}],"name":"set_cktcamount","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[],"name":"kill","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_tid","type":"uint32"}],"name":"set_tgridFee","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"_tid","type":"uint32"},{"name":"_index","type":"uint8"}],"name":"get_cktAmount","outputs":[{"name":"","type":"int16"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"_addr","type":"address"}],"name":"get_tGFee","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_address","type":"address"},{"name":"_fee","type":"uint8[]"}],"name":"set_minmaxgfee","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_addr","type":"address"},{"name":"_amount","type":"uint16"}],"name":"set_traforamount","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"_addr","type":"address"}],"name":"get_dGFee","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_tid","type":"uint32"}],"name":"set_dgridFee","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_addr","type":"address"},{"name":"_amount","type":"uint64"}],"name":"set_cktramount","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"_addr","type":"address"}],"name":"get_trafoAmount","outputs":[{"name":"","type":"int16"}],"payable":false,"stateMutability":"view","type":"function"}]'
DynamicGridFee_abi      = json.loads(DynamicGridFee_abi_str)
DynamicGridFee_contract = web3.eth.contract(abi=DynamicGridFee_abi,address=DynamicGridFee_address)


# In[59]:


#Ethereum Accounts/EOAs
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


# In[61]:


#########Dynamic Grid Fee#######
#set oli origin Address
web3.personal.unlockAccount(coinbase, 'felixfaizan')
DynamicGridFee_contract.transact({'from': coinbase}).setOliOrigin(Oliorigin_address)


# In[62]:


###Set Min/Max Grid Fee###
web3.personal.unlockAccount(coinbase, 'felixfaizan')
DynamicGridFee_contract.transact({'from': coinbase}).set_minmaxgfee(account_21, [4,6,1,3])
DynamicGridFee_contract.transact({'from': coinbase}).set_minmaxgfee(account_22, [4,6,1,3])

