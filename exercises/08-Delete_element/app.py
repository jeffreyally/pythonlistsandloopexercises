people = ['juan','ana','michelle','daniella','stefany','lucy','barak']

people = ['juan','ana','michelle','daniella','stefany','lucy','barak']

#Your code go here:
def deletePerson(person_name):
    if person_name != 'daniella' and person_name != 'juan' and person_name != 'emilio': 
        return person_name
    


listy = list(filter(deletePerson,people))

print(listy)