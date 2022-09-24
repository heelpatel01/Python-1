'''
A company decides to give bonus to their employees on this Diwali.
#1 A '5%' bonus on salary is given to the male workers and '10%' bonus salary to the female workers.
#2 If the salary of the emaployee is less than 15000 then the employee get an extra '3%' bonus on the salary
#3 WAP to enter your salary and gender then calculate the bonus that has to given to the employee and display the salary that the employee will get.
'''

sal=int(input('enter your salary'))
gen=input('enter your gender')

if gen=='m':
    bonus=0.05*sal
else:
    bonus=0.10*sal

if sal<15000:
    print('u will get extra 3% bonus why because u r sal is less than 15000')
    bonus=bonus+0.03*sal

sal=bonus+sal

print('sal is ',sal)
