import learning
def main():
    p1=learning.getPerson(name='楊凱')
    print(p1.bmi_print())
    print('==============')
    p2 = learning.Person.getPerson(name="yang kaix aun") #class static method
    print(p2.bmi_print())
    print("===========")
    p3 = learning.Person.getPerson1(name="alice")
    print(p3.bmi_print())
    
if __name__=='__main__':
    main()
