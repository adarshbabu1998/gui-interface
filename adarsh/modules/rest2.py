import rest

print("welcome")
print('your choices are','\n' ,'veg','\n','non veg')
choice=input('enter your choice: ')
if choice=='veg':
    print(rest.obj.veg('veg meals','veg salad'))
    dish=input('enter your dish: ')
    if dish=='vegmeals':
        print(rest.obj.rate1(120))
    elif dish=='vegsalad':
        print(rest.obj.rate2('110')) 
else:
     if choice=='nonveg':
        print(rest.obj.non_veg('chicken biriyani','kuzhimandhi'))
        dish=input('enter your dish: ')
        if dish=='chickenbiriyani':
            print(rest.obj.rate3(160))
            
        elif choice=='kuzhimandhi':
            print(rest.obj.rate4(200))  


# import rest

# r=rest.obj.rate2(120)
# print(rest.ob.sample(1,4))