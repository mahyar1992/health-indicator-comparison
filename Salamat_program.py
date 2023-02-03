list_ghad_A = []
list_vazn_A = []
list_sen_A = []
list_ghad_B = []
list_vazn_B = []
list_sen_B = []
class student_A:
    count = 0
    def __init__ (self, ghad, vazn, sen, name):
        self.ghad = ghad
        self.vazn = vazn
        self.sen = sen
        self.name = name
        student_A.count +=1
        list_ghad_A.append(int(self.ghad))
        list_vazn_A.append(int(self.vazn))
        list_sen_A.append(int(self.sen))
    def get_name(self):
        return self.name
    def avg_ghad (self):
        sum_ghad = 0
        for item in list_ghad_A:
            sum_ghad += int(item)
        return sum_ghad/self.count
    def avg_vazn (self):
        sum_vazn = 0
        for item in list_vazn_A:
            sum_vazn += int(item)
        return sum_vazn/self.count
    def avg_sen (self):
        sum_sen = 0
        for item in list_sen_A:
            sum_sen += int(item)
        return sum_sen/self.count
    def tedad (self):
        return self.count
class student_B:
    count = 0
    def __init__ (self, ghad, vazn, sen, name):
        self.ghad = ghad
        self.vazn = vazn
        self.sen = sen
        self.name = name
        student_B.count +=1
        list_ghad_B.append(int(self.ghad))
        list_vazn_B.append(int(self.vazn))
        list_sen_B.append(int(self.sen))
    def get_name(self):
        return self.name
    def avg_ghad (self):
        sum_ghad = 0
        for item in list_ghad_B:
            sum_ghad += int(item)
        return sum_ghad/self.count
    def avg_vazn (self):
        sum_vazn = 0
        for item in list_vazn_B:
            sum_vazn += int(item)
        return sum_vazn/self.count
    def avg_sen (self):
        sum_sen = 0
        for item in list_sen_B:
            sum_sen += int(item)
        return sum_sen/self.count
    def tedad (self):
        return self.count
number_of_class_a = int(input("please insert your first group participants' number:\n"))
input_sen_class_a = input('Please insert their ages (like: x y z ...):\n')
input_ghad_class_a = input('Please insert their heights (like: x y z ...):\n')
input_vazn_class_a = input('Please insert their weights (like: x y z ...):\n')
list_input_sen_class_a = input_sen_class_a.split()
list_input_ghad_class_a = input_ghad_class_a.split()
list_input_vazn_class_a = input_vazn_class_a.split()
number_of_class_b = int(input("please insert your second group participants' number:\n"))
input_sen_class_b = input('Please insert their ages (like: x y z ...):\n')
input_ghad_class_b = input('Please insert their heights (like: x y z ...):\n')
input_vazn_class_b = input('Please insert their weights (like: x y z ...):\n')
list_input_sen_class_b = input_sen_class_b.split()
list_input_ghad_class_b = input_ghad_class_b.split()
list_input_vazn_class_b = input_vazn_class_b.split()
for i in range (0, number_of_class_a):
    student_name_i = student_A(list_input_ghad_class_a[i], list_input_vazn_class_a[i], list_input_sen_class_a[i], 'A')
for j in range (0, number_of_class_b):
    student_name_j = student_B(list_input_ghad_class_b[j], list_input_vazn_class_b[j], list_input_sen_class_b[j], 'B')

print('The average of ages, heghts and weights of first group is: [%.2f, %.2f, %.2f]' %(student_name_i.avg_sen(), student_name_i.avg_ghad(), student_name_i.avg_vazn()))
print('Body mass index of group A is: %.2f' % ((student_name_i.avg_vazn())/((student_name_i.avg_ghad()/100)**2)))
print('The average of ages, heghts and weights of second group is: [%.2f, %.2f, %.2f]' %(student_name_j.avg_sen(), student_name_j.avg_ghad(), student_name_j.avg_vazn()))
print('Body mass index of group B is: %.2f' % ((student_name_j.avg_vazn())/((student_name_j.avg_ghad()/100))**2))

if (student_name_i.avg_vazn())/((student_name_i.avg_ghad()/100)**2) > (student_name_j.avg_vazn())/((student_name_j.avg_ghad()/100)**2):
    print (student_name_i.get_name()) #determine who has a bigger BMI
elif (student_name_i.avg_vazn())/((student_name_i.avg_ghad()/100)**2) < (student_name_j.avg_vazn())/((student_name_j.avg_ghad()/100)**2):
    print(student_name_j.get_name()) #determine who has a bigger BMI
else: 
    if student_name_i.avg_sen() > student_name_j.avg_sen():
        print (student_name_j.get_name()) #if the BMI was same, print who has lower age
    elif student_name_i.avg_sen() < student_name_j.avg_sen():
            print (student_name_i.get_name()) #if the BMI was same, print who has lower age
    else:
        print('Same')