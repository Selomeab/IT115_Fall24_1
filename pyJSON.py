#importing json library 
import json 

#Creating a dictionary named data1 and creating a string array for intrests section 
data1 = {

    'name':'Selomea Beyene',
    'age':30,
    'city':'Seattle,WA',
    'interests': ['Traveling','Cooking','Swimming','Hiking','Documenteries','Writing'],
    'is_student': True

}


#Creating a write mode file where changes will show up when we run our code 
with open('data1.json','w') as json_file:

    #Dump the Data Dictionary into the JSON file. 
    json.dump(data1,json_file,indent=4)
#Printing message to let user know changes have been sucessfully written into our file 
print("You have sucessfully written to data1.json")





#Opening our file data1.json in read mode so we can see the data we just wrote 
with open ('data1.json','r') as json_file: 

    loaded_data = json.load(json_file)
#This is going to print a message that we have read our data sucessfully 
print("Sucessfully able to read data1.json")
print(loaded_data)



#Now we are changing the age value from 30 to 22 
loaded_data['age'] = 22
#We are appending a new item into our original string array on line 10 
loaded_data['interests'].append('Theology') 
#Reopening the data1.json file in write mode so our updated data will show up 
with open('data1.json','w') as json_file:

    #Dump the Data Dictionary into the JSON file. 
    json.dump(loaded_data,json_file,indent=4)
#print another message to show it has actually been successfully re-written
print("You have sucessfully re-written to data1.json")
