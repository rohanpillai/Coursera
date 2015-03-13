from collections import *
from heapq import *

Item = namedtuple('Item', ['index', 'value', 'weight'])
#class Item:
#  def __init__(self, index, value, weight):
#    self.index = index
#    self.value = value
#    self.weight = weight



class ItemList:
  def __init__(self, K, W):
    self._list = []
    self.K = K
    self.W = W
    self.totalValue = [0 for i in range(W)]
    self.taken = [-1 for i in range(W)]

  def insert(self, item):
    heappush(self._list, (item.weight, item))


  def heapify(self):
    res = [heappop(self._list) for i in range(len(self._list))]
    self._list = res

  def DP(self):
    (minWeight, item) = self._list[0]
    for w in range(minWeight, self.W):
      for (j, item) in self._list:
        if item.weight > w:
          break
        
        if self.totalValue[w - item.weight] + item.value > self.totalValue[w]:
          self.taken[w] = item.index
          self.totalValue[w] = self.totalValue[w - item.weight] + item.value

