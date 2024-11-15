#
import json 

#
data1 = {

    'name':'Selomea Beyene',
    'age':22,
    'city':'Seattle,WA',
    'interests': ['Traveling','Cooking','Swimming','Hiking','Documenteries','Writing'],
    'is_student': True

}


#
with open('data1.json','w') as json_file:

    #Dump the Data Dictionary into the JSON file. 
    json.dump(data1,json_file,indent=4)

print("You have sucessfully written to data1.json")






with open ('data1.json','r') as json_file: 

    loaded_data = json.load(json_file)

print("Sucessfully able to read data1.json")
print(loaded_data)




loaded_data['age'] = 22

loaded_data['interests'].append('Theology')

with open('data1.json','w') as json_file:

    #Dump the Data Dictionary into the JSON file. 
    json.dump(loaded_data,json_file,indent=4)

print("You have sucessfully re-written to data1.json")
