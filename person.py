
class Person:

    def __init__(self, first_name, last_name):
        
        self.name = first_name + ' ' + last_name
        self.friends = []
        
    def add_friend(self, friend_person):
        self.friends.append(friend_person)

    def get_name(self):
        
        return self.name

    def get_friends(self):
        return self.friends



def load_people():
    with open('a2_sample_set.txt') as f:
        content = f.readlines()
        
    all_persons = []
    for c in content:
        names = c.strip('\n').split(': ')
        
        name = names[0].split(' ')
        person = Person(name[0], name[1])
        
        for fri in names[1].split(', '):
            person.add_friend(fri)
            
        all_persons.append(person)
    return all_persons
        
    



if __name__ == '__main__':
    print(len(load_people()))
    print(load_people()[0].get_name())
