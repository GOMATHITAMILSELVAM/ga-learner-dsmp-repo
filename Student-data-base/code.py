# --------------
# Code starts here
class_1= ['Geoffrey Hinton','Andrew Ng','Sebastian Raschka','Yoshua Bengio']
class_2= ['Hilary Mason','Carla Gentry','Corinna Cortes']
new_class=class_1+class_2
print(new_class)
new_class.append('Peter Warden')
new_class.remove('Carla Gentry')
print(new_class)



# Code ends here


# --------------
# Code starts here
courses={'Math':65,'English':70,'History':80,'French':70,'Science':60}
print(courses['Math'])
print(courses['English'])
print(courses['History'])
print(courses['French'])
print(courses['Science'])
total=65+70+80+70+60
print(total)
percentage=(total*100/500)
print(percentage)



# --------------
# Code starts here
mathematics={'Geoffrey Hinton': '78','Andrew Ng': '95','Sebastian Raschka': '65','Yoshua Benjio':'50','Hilary Mason':'70','Corinnan Cortes':'66','Peter Warden':'75'}
topper=max(mathematics,key=mathematics.get)
print(topper)






# Code ends here  


# --------------
# Given string
topper = 'andrew  ng '
first_name= (topper.split()[0])
last_name= (topper.split()[1])
print(first_name)
print(last_name)
space=' '
full_name= last_name+space+first_name
print(full_name)
full_name.upper()
certificate_name=full_name.upper()
print(certificate_name)


