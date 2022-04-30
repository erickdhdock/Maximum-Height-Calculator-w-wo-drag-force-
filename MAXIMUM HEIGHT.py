from cmath import acos
import imp
from re import L

import math

print('maximum_height_calc')
def f1 ():
    print(' ')


def func_end():
    print('do you want to re-start your calculator?')
    ender = input("please type 'Y'(yes) or 'N'(no) > ")
    if ender == 'N':
        exit()
    elif ender == 'Y':
        func1()
    else:
        print("only 'Y' or 'N' can be an answer")
        func_end()

        
def func_angle():
    
    print('If you do not input any value on gravitional acceleration, it will be automatically set to 9.81m/s**2')
    g4 = input('please input the value of the gravitional acceleration> ')
    if g4 == '':
        print('your gravitational acceleration speed is set to 9.81m/s**2')
        g = 9.81    
    else:
        g = float(g4)

    H = float(input('please input the height of the maximum height> '))
    
    v0 = float(input('please input the value of the initial velocity> '))
    
    angval1 = 4 * g * H
    
    angval2 = v0 ** 2
    
    angval3 = angval1 / angval2
    
    angvalcos = 1 - angval3
    
    angvalacos = math.acos(angvalcos)
    
    angvalrad = angvalacos / 2
    
    angvaldeg = 57.2958 * angvalrad
    
    print('///set value///')
    print('g = {} m/s**2, H = {} meter0s, v0 = {}m/s'.format(g,H,v0))
    
    print('the shooting angle is {} radian and {} degrees'.format(angvalrad,angvaldeg))

    func_end()


def func_v0 ():
    
    print('If you do not input any value on gravitional acceleration, it will be automatically set to 9.81m/s**2')
    g4 = input('please input the value of the gravitional acceleration> ')
    if g4 == '':
        print('your gravitational acceleration speed is set to 9.81m/s**2')
        g = 9.81    
    else:
        g = float(g4)

    H = float(input('please input the height of the maximum height> '))

    angle = float(input('please input the launching angle in degrees> '))

    v0val1 = 2 * g * H

    v0valangrad = angle / 57.2958
    v0valangforcos = math.cos(2 * v0valangrad)

    v0valangforsin1 = 1 - v0valangforcos

    v0valangforsin2 = v0valangforsin1 / 2

    v0val2 = v0val1 / v0valangforsin2

    finalval = math.sqrt(v0val2)

    
    print('///set value///')
    print('g = {} m/s**2, angle = {} degrees, H = {}m'.format(g,angle,H))

    print ('The initial speed should be +-{}m/s'.format(finalval))

    func_end()

def func_H ():
    print('If you do not input any value on gravitional acceleration, it will be automatically set to 9.81m/s**2')
    g4 = input('please input the value of the gravitional acceleration> ')
    if g4 == '':
        print('your gravitational acceleration speed is set to 9.81m/s**2')
        g = 9.81    
    else:
        g = float(g4)
        
    angle = float(input('please input the launching angle in degrees> '))

    v0 = float(input('please input the value of the initial velocity> '))
    
    Hval1 = v0 ** 2 
    
    Hval2radiant = angle / 57.2958
    Hval3 = Hval2radiant * 2
    Hval4 = 1 - math.cos(Hval3)
    
    Hval5sin_2x = Hval4 / 2
    
    Hval6 = Hval1 * Hval5sin_2x 
    accelgrav = 2 * g
    Hval7 = Hval6 / accelgrav 


    f1()
    print('///set value///')
    print('g = {} m/s**2, angle = {} degrees, v0 = {}m/s'.format(g,angle,v0))
    f1()
    f1()
    

    print('The maximum height of the object is {}m'.format(Hval7))

    func_end()



def func1():
    
    dict1 = ( 'conversion:1',
            'start calculation:2'
        )

    for pattern1 in dict1:
        print(pattern1)
    
    str_dict1 = int(input('please input the number that you want to start with> '))

    if str_dict1 == 1:
        print('mode selected = conversion')
        print("velocity is based on 'm/s', value of the range is based on 'm', weight and mass is based on 'kg' ")
        category = ['1: inches to meter', '2: centimeter to meter', "3: 'ft' to meter"]
        for pattern in category:
            print(pattern)

        selected1 = int(input('please input number of the mode that you want to select > '))    
    
        print('your selected value is {}'.format(category[selected1-1]))
    
        if selected1 == 1:
            print('inches to meter')
            conv_select1 = int(input('please input the number that you want to convert > '))
            conv_result1 = conv_select1 * 0.0254
            print('{} inches is {} meters'.format(conv_select1, conv_result1))
            func1()
        elif selected1 == 2:
            print('centimeter to meter')
            conv_select2 = float(input('please input the number that you want to convert > '))
            conv_result2 = conv_select2 * 0.01
            print('{} centimeter is {} meters'.format(conv_select2, conv_result2))
            func1()
        elif selected1 == 3:
            print("'ft' to 'meter'")
            conv_select3 = float(input('please input the number that you want to convert > '))
            conv_result3 = conv_select3 * 0.3048
            print('{} ft is {} meters'.format(conv_select3, conv_result3))
            func1()
    if str_dict1 == 2:
        print(' ')
        print('mode selected = calculation')
        print(' ')



        mode12 = {'With drag force : 1', 'without drag force : 2'}
        for patterns1 in mode12:
            print ("'With drag force : 1', 'without drag force : 2'")
            selected_mode = float(input('please input the mode of the calculator> '))
            if selected_mode == 1:
                f1()
                print('Calculation with friction force')
                def func_friction_H():
                    
                    print("The unit of the acceleration speed is m/s**2 ")
                    print("If you press enter, the gravitational acceleration will be  automatically set to 9.81m/s**2")
                    
                    g4 = input('please input the value of the gravitional acceleration> ')
                    if g4 == '':
                        print('your gravitational acceleration speed is set to 9.81m/s**2')
                        g = 9.81    
                    else:
                        g = float(g4)
                    dict_dc1 = ['sphere : 1', 'Half-sphere:2', 'Cone : 3 ', 'Angled Cube : 4', 'Long Cylinder : 5', 'Short Cylinder : 6', 'Short Cylinder : 7', 'Streamlined body : 8', 'Streamlined Half-Body : 9']
                    print(dict_dc1)
                    selected1234 = int(input('please select the shape of the object > '))
                    if selected1234 == 1:
                        dc = 0.47
                        print('the drag coefficient is {}.'.format(dc))
                    if selected1234 == 2:
                        dc = 0.42
                        print('the drag coefficient is {}.'.format(dc))
                    if selected1234 == 3:
                        dc = 0.50
                        print('the drag coefficient is {}.'.format(dc))
                    if selected1234 == 4:
                        dc = 1.05
                        print('the drag coefficient is {}.'.format(dc))
                    if selected1234 == 5:
                        dc = 0.80
                        print('the drag coefficient is {}.'.format(dc))
                    if selected1234 == 6:
                        dc = 0.82
                        print('the drag coefficient is {}.'.format(dc))
                    if selected1234 == 7:
                        dc = 1.15
                        print('the drag coefficient is {}.'.format(dc))
                    if selected1234 == 8:
                        dc = 0.04
                        print('the drag coefficient is {}.'.format(dc))
                    if selected1234 == 9:
                        dc = 0.09
                        print('the drag coefficient is {}.'.format(dc))

                    print('radius: type "R" \
                            area: type "A"')
                    print()
                    
                    YN = input('Do you want to enter the radius or do you want to enter the area?')
                    if YN == "R":
                        print("The unit of the radius is m")
                        R = float(input('Please enter the radius of the object > '))
                        print(f'The radius of the object is {R}')
                        print()
                        Ar = math.pi * R**2
                        print(f"The area of the object is {Ar}m**2")
                            
                    elif YN == "A":
                        print("The unit of area is m**2")
                        Ar = float(input('please input the area of the object > '))
                        return Ar
                    else:
                        print ("Please check the answer and try it again.")
                        exit()

                    print()
                    print("The unit of density is kg/m**3")
                    print()
                    print("If you press enter, the density will be set to 1.225 kg/m**3")
                    print()
                    Dens1 = input('please input the density of the fluid through which the object is falling > ')
                    if Dens1 == (""):
                        Dens = 1.225
                        
                    else:
                        Dens == float(Dens1)

                    print()    
                    print (f"The density of the fluid is {Dens}")
                    print()


                    print("The unit of the mass is kg")
                    vt_m = float(input('please input the value of the mass of the object > '))
                    print()
                    print('calculating terminal velocity...')
                    print()
                    twomg = 2 * vt_m
                    
                    vt_down = Dens * Ar * dc 
                    
                    vt_rt = twomg / vt_down
                    
                    vt_sqroot = vt_rt ** 0.5
                    

                    print()
                    print()
                    print('the terminal speed is {}'.format(vt_sqroot))
                    print()
                    print()
                    
                    



                    #max height calculation
                    v0 = float(input('please input the initial speed > '))
                    twog = 2 * g 
                    sumofv0vt = v0**2 + vt_sqroot**2
                    vt_log = math.log(sumofv0vt / vt_sqroot**2)
                    vt_1 = vt_sqroot**2 / twog 
                    vt_2 =   vt_1 * vt_log

                    print('the maximum height with the friction is {}m'.format(vt_2))


                    
                func_friction_H()
                func_end()

            if selected_mode == 2:
                mode123 = ['Maximum Height : 1',
                           'Launching angle : 2',
                           'Initial speed : 3'
                            ]
                for patternsss in mode123:
                    print(patternsss)
                selecedmode123 = float(input('what value do you want to calculate? > '))
                if selecedmode123 == 1:
                    func_H()
                if selecedmode123 == 2:
                    func_angle()
                if selecedmode123 == 3:
                    func_v0()
    else:
        print("Only '1' or '2' can be accepted as an answer.")
        print('please check the answer and re type the answer')
        func1()




    print('end')

        
func1()