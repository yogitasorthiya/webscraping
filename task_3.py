from task_1 import task1
# list=task1()
import pprint
list_1=task1()
import json
def droup_decode(movies):
    list_1=[]
    for i in movies:
        mod=i["year"]%10
        dec=i["year"]-mod
        if dec not in list_1:
            list_1.append(dec)
    list_1.sort()
    movies_dec={}
    for i in list_1:
        movies_list=[]
        for   x in movies:
            if x["year"]>=i and x["year"]<=i+10:
                movies_list.append(x)
                movies_dec[i]=movies_list
                print(movies_list)
            with open("movies_dec.json","w")as f:
                json.dump(movies_dec,f,indent=5)
    return movies_dec
droup_decode(list_1)






       
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        