
from patient import *
import matplotlib.pyplot as plt
# import statement to make use of functions/classes from earlier task(s).
# (change the xxxxxxxx to match the actual filename.)


def visual_curve(days, meeting_probability, patient_zero_health):

    n = []
    for day in range(days):
        all_patients = run_simulation(day, meeting_probability, patient_zero_health )
        patients_number = 0
        for patients in all_patients:
            if patients.is_contagious():
                patients_number += 1
        n.append(patients_number)
    return n

if __name__ == '__main__':

    days = 30
    meeting_prob = 0.5
    zero_health = 20
    print(visual_curve(days, meeting_prob, zero_health))
    plt.plot([i+1 for i in range(days)], visual_curve(days, meeting_prob, zero_health))
    plt.title('days = {0}, meeting_prob = {1}, zero_health = {2}'.format(days, meeting_prob, zero_health))
    plt.xlabel('Days')
    plt.ylabel('Number of infected persons')
    plt.savefig('1.png')
    
    plt.show()


