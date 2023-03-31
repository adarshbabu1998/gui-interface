class food:
   
    def veg(self,a,b):
        self.a=a
        self.b=b
        print(a,'\n',b,)
    def rate1(self,ra):
        self.ra=ra
        print(ra)
        
    def rate2(self,rb):
        self.rb=rb
        print(rb)
    def non_veg(self,a,b):
        self.a=a
        self.b=b
        print(a,'\n',b,)
       
    def rate3(self,ra):
         self.ra=ra
         print(ra)

    def rate4(self,rb):
         self.rb=rb
         print(rb)
       
obj=food() 
# obj.fud()
# obj.non_veg()
# obj.veg()

# class person:
#     def sample(self,a,b):
#         self.a=a
#         self.b=b
#         sum = self.a+self.b
#         return sum
# ob = person()