# exception handling
try:
          class numbers:
            def sum(self,a,b):
                 self.a=a
                 self.b=b
                 x=a/b
                 print(x)
            pass
          obj=numbers()
          obj.sum(2,2)
        

except:
    print('not possible')
else:
    print('possible')
#         finally:
#             print('yep')
    

