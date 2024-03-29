import json

data = '''
{
  "name" : "Chuck",
  "phone" : {
    "type" : "intl",
    "number" : "+1 734 303 4456"
   },
   "email" : {
     "hide" : "yes"
   }
}'''



myJcode='''
{
    "member":"zeinab"
    ,"member":"zahra"
    ,"member":"ali" ,
    "tel":{
        "mobile":"98",
        "constant":"077"
    },
    "gender":"female"
}'''
info = json.loads(myJcode)
print('member is', info["member"])
print('tel===', info["tel"]["mobile"])
