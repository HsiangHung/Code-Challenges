
# A. Linked-list

### The linked list nodes are defined as
```Python
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None
```

## Q1: Remove Duplicates from Sorted List

```Python
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None: return 
    
        node = head
        while node.next != None:
            nextNode = node.next
            if nextNode.val == node.val:
                if nextNode.next != None:
                    nextNextNode = nextNode.next
                    node.next = nextNextNode
                else:
                    node.next = None
            else:
                node = nextNode
                
        return head
```



```Python
for cv in range(num_cvFold):   ### using cross-validation                                          
     train, val = self.trainData.randomSplit(weights = [0.8,0.2], seed=randint(0,100))
     model = ALS.train(train,rank,seed=self.seed,iterations=self.iterations,lambda_=reg)
     X_val = val.map(lambda x: (x[0], x[1]))
     predictions = model.predictAll(X_val).map(lambda r: ((r[0], r[1]), r[2]))
     rates_and_preds = val.map(lambda r: ((int(r[0]), int(r[1])), float(r[2]))).join(predictions)
     RMSE = RMSE+math.sqrt(rates_and_preds.map(lambda r: (r[1][0] - r[1][1])**2).mean())
     MAE = MAE+rates_and_preds.map(lambda r: abs(r[1][0] - r[1][1])).mean()
```

```Python
        KMeans.train(parsedData, k_clusters, maxIterations=100,
                                runs=20, initializationMode="k-means||")
        WSSSE = parsedData.map(lambda point: error(point)).reduce(lambda x, y: x + y)
        print("Within Set Sum of Squared Error = " + str(WSSSE))
```
