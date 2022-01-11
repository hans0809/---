heap=[1,2,3,4,5]
i=0
while i<1:
    heap[i],heap[i+1]=heap[i+1],heap[i]
    print(heap)
    i+=1
print(heap)