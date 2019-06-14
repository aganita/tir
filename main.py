class Trading:
   'Calculates gains/losses of trading orders based on FIFO principle'

   def __init__(self):
      self.coinWallet = []
      self.gain = 0
   def __del__(self):
      class_name = self.__class__.__name__
      print (class_name, ' class is destroyed')

   def buy(self, buyOrder):
      ## TODO validate format
      self.coinWallet.append(buyOrder)

   def displayWallet(self):
      print ("my wallet = ", self.coinWallet)
   
   def getRemainingCoins(self):
      coinAmount = 0

      for i in self.coinWallet:
        coinAmount += i['amount']

      return coinAmount

   def getGain(self):
      return self.gain
      
   def setGain(self, newGainAmount): 
      self.gain = newGainAmount

   def getAllCoins(self):
      return self.coinWallet

   def getFirst(self):
      return self.coinWallet[0]

   def sell(self, sellOrder):
      ## TODO validate format
      if (sellOrder['amount'] > self.getRemainingCoins()):
        print ('Not enough coins in the wallet to sell. Skipping this sell order')
        return
      
      oldestOrder = self.coinWallet.pop(0)
      updatesOldestOrder = []
      remainingCoinAmount = 0

      if (oldestOrder['amount'] > sellOrder['amount']):
         remainingCoinAmount = oldestOrder['amount'] - sellOrder['amount']
         updatesOldestOrder = {'timestamp': oldestOrder['timestamp'], 'amount': remainingCoinAmount, 'value': oldestOrder['value']}
         self.coinWallet.insert(0, updatesOldestOrder)
         self.gain += sellOrder['amount'] * (sellOrder['value'] - oldestOrder['value'])
      else: 
         remainingCoinAmount = sellOrder['amount'] - oldestOrder['amount']         
         self.gain += oldestOrder['amount'] * (sellOrder['value'] - oldestOrder['value'])
         self.sell({'timestamp': sellOrder['timestamp'], 'amount': remainingCoinAmount, 'value': sellOrder['value']})

   def send(sendOrder):
      oldestOrder = self.coinWallet.pop(0)
      updatesOldestOrder = []
      remainingCoinAmount = 0

      if (oldestOrder['amount'] > sellOrder['amount']):
         remainingCoinAmount = oldestOrder['amount'] - sellOrder['amount']
         updatesOldestOrder = {'timestamp': oldestOrder['timestamp'], 'amount': remainingCoinAmount, 'value': oldestOrder['value']}
         self.coinWallet.insert(0, updatesOldestOrder)
      else:
         remainingCoinAmount = sellOrder['amount'] - oldestOrder['amount']         
         self.sell({'timestamp': sellOrder['timestamp'], 'amount': remainingCoinAmount, 'value': sellOrder['value']})



# unit tests
foo = Trading()
foo.buy({'timestamp': 1, 'amount': 40, 'value': 100})
foo.buy({'timestamp': 2, 'amount': 5, 'value': 150})
foo.sell({'timestamp': 3, 'amount': 100, 'value': 300})
foo.sell({'timestamp': 4, 'amount': 4, 'value': 300})
print (foo.getRemainingCoins())
print (foo.getGain())