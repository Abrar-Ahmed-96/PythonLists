# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 00:00:29 2021

@author: ABRAR
"""
#LIST
city_list = ['karachi','lahore','multan']
print(city_list)
print(city_list[2]) #access index

city_list.append('islamabad') #append default on end (1 value)
print(city_list)

city_list.insert(2,'quetta')  #insert can add anywhere (1 value)
print(city_list)

city_list.extend(['peshwar','chitral','karachi']) #extend allows more than 1 value
print(city_list)

city_list.count('karachi')  #counts how many times karachi is in list

city_list.index('peshwar') #tells the index location

#city_list.clear() #clear whole list

city_listTWO = city_list.copy() # copies by value
print(city_listTWO)

del  city_list[2]  #removes as it requires index
print(city_list)

city_list.remove('lahore') #removes simply by object 

popcity = city_listTWO.pop()   #last in first out 
print('the pop city is' , popcity)
print('remaining city',city_listTWO)

popcity = city_listTWO.pop()   #last in first out 
print('the pop city is' , popcity)
print('remaining city',city_listTWO)


popcity = city_listTWO.pop(4)   #by index also,we can pop
print('the pop city is' , popcity)      #islamabad
print('remaining city',city_listTWO)



city_list.sort()    #ascending order
print(city_list)

city_list.sort(reverse=True)    #descending order
print(city_list)

city_list.reverse()    #doesnot sort but only reverses
print(city_list)

fruits= ["mango", "orange","pine"]
fruits.extend(["apple","lemon","malt"])  #adds multiple iterable values
print(fruits)

fruits.count("lemon")   #how many times lemon in the list
 
fruits2 = fruits.copy()   #by value  

fruits3= fruits            #by reference  same work in fruits.same as fruits3

#fruits.index[1]     #search or find

# mango in fruits       #search or find (true)

#slicing to get more than one value

result = ['john','martin','roshan','dhoni'] #to include end give one plus
print(result[1:4])       #martin roshan dhoni   #pos index  

print(result[-4:-2])     #martin roshan dhoni   #neg index

print(result[:])       #this will give whole list

print(result[3:])     #gives after index 3 onwards

print(result[:3])     #gives before index 3 

print(result[2:-1])     #gives after 2 and before -1

print(result[4:-3])   #gives empty because direction from left to right 

step= [12,3,5,5,8,5,8,5,9,2,5,8,2,1,7]
print(step[0:8:2])        #with step 2

print(step[::3])      #with step 3 

del step[1:3]   #delete multiple values by index
print(step)

#element which is pop can be saved into another variable

#remove : permenant remove

colour = [ 12,3,5,8,7,4,8,5,2,0,12,2]
colour.pop(3)    #8 pop
print(colour)     

colour.pop()   #by default last value is pop
print(colour)


