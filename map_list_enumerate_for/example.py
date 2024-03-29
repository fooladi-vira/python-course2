

#lambda arguments : expression

f=lambda  a:a**2
mylist=[2,4,6,8,10,80,90,90]
for a in mylist:
     r=f(a)
     print(r)






# #map
# mylist=[2,4,6,8,10,80,90,90]
# map_list=map(f,mylist)

# for a in map_list:
#      print(a)






# for f in  enumerate(map_list):
#     print(f)










mylist=[2,4,6,8,10,80,90,90]
mycontact=['ali','mohamad','zahra','ana','kati']
dic_cantact=dict(zip(mycontact,mylist))
for p in dic_cantact:
    print(p)