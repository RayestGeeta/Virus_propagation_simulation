
from person import *
import random

class Patient(Person):
    def __init__(self, first_name, last_name, health):
        super().__init__(first_name, last_name)
        self.name = first_name + ' ' + last_name
        self.health = health
        if self.health >= 50:
            self.contagious = False
        else:
            self.contagious = True

    def get_health(self):
        return self.health

    def set_health(self, new_health):
        self.health = new_health
        
    def is_contagious(self):
        return self.contagious

    def infect(self, viral_load):
        viral_load = 5 + ((viral_load - 25)**2)/62
        
        if self.health >= 50:
            self.health = self.health - 2 * viral_load
        elif 29 <= self.health < 50:
            self.health = self.health - viral_load
        elif self.health < 29:
            self.health = self.health - 0.1*viral_load
            
        if self.health < 50:
            self.contagious = True

        

    def sleep(self):
        self.health += 5
        if self.health >= 50:
            self.contagious = False


def run_simulation(days, meeting_probability, patient_zero_health):

    all_patients = load_patients(patient_zero_health)
    all_names = []

    for patient in all_patients:
        all_names.append(patient.get_name())

    for day in range(days):

        for patient in all_patients:
            for fri in patient.get_friends():
                if meeting_probability > random.random():
                    if patient.is_contagious():
                        all_patients[all_names.index(fri)].infect(patient.health)
                    if all_patients[all_names.index(fri)].is_contagious():
                        patient.infect(all_patients[all_names.index(fri)].health)

        for patient in all_patients:
            patient.sleep()
    return all_patients


def load_patients(initial_health):
    with open('a2_sample_set.txt') as f:
        content = f.readlines()

    all_patients =  []
    first = True
    for c in content:
        names = c.strip('\n').split(': ')

        name = names[0].split(' ')
        if first:
            person = Patient(name[0], name[1], initial_health)
            first = False
        else:
            person = Patient(name[0], name[1], 75)

        for fri in names[1].split(', '):
            person.add_friend(fri)

        all_patients.append(person)
    return all_patients



if __name__ == '__main__':

    days = 20
    meeting_prob = 0.5
    zero_health = 20

    
    n = []
    for day in range(days):
        all_patients = run_simulation(day, meeting_prob, zero_health )
        patients_number = 0
        for patients in all_patients:
            if patients.is_contagious():
                patients_number += 1
        n.append(patients_number)
    print(n)


