import D3AC_N
mydata = [[5,10],[4,10],[5,9],[5,11],[3,10],[6,10],[20,15],[19,15],[21,15],[20,14],[20,16],[19,16],[19,14]]
result=D3AC_N.cluster(mydata,2)
print(result)
print("Got {} clusters total. ".format(len(result)))