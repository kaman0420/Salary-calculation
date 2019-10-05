# General Retail Industry Award (Full-time, Part-time, Casual, Age, Time, Hour)
# Age > 21 Retail employee level 1

# Casual
# $26.76 per hour - Mon to Fri for the first 38 hours
# $27.83 per hour in the evening - Mon to Fri after 6 pm
# $29.97 per hour - Sat
# $37.47 per hour - Overtime - Mon to Sat for the first 3 hours
# $48.17 per hour - Overtime - Mon to Sat after 3 hours
# $37.47 per hour - Sun
# $48.17 per hour - Overtime - Sun
# $53.53 per hour - PH
# $58.88 per hour - Overtime - PH

# Full-time & part-time
# $21.41 per hour - Mon to Fri for the first 38 hours
# $26.76 per hour in the evening - Mon to Fri after 6 pm
# $26.76 per hour - Sat
# $32.12 per hour - Overtime - Mon to Sat for the first 3 hours
# $42.82 per hour - Overtime - Mon to Sat after 3 hours
# $35.33 per hour - Sun
# $48.82 per hour - Overtime - Sun
# $48.17 per hour - PH
# $53.53 per hour - Overtime - PH
        
import datetime
x = datetime.datetime.now()
print("{0}-{1}-{2} {3}".format(x.strftime("%d"),x.strftime("%m"),x.strftime("%Y"),x.strftime("%A")))

# get employment type
def input_type ():
    
    print ("Welcome to salary calculation system: ")
    print ()
    print ("F > Full-time")
    print ("P > Part-time")
    print ("C > Casual")
    print ()
    
    emp_type = input ("Enter your employment type: ")
    print ()
    return emp_type

# Ask working hours
def working_hours ():

    # Ask working hours - Mon to Fri before 6 pm
    before6 = input ("Enter hours of work from Mon to Fri before 6 pm: ")
    input_before6 = int (before6)

    # Ask working hours - Mon to Fri after 6 pm
    after6 = input ("Enter hours of work from Mon to Fri after 6 pm: ")
    input_after6 = int (after6)
    
    # Ask working hours - Sat
    sat = input ("Enter hours of work on Sat: ")
    input_sat = int (sat)
    
    # Ask OT working hours - Mon to Sat 
    weekday_ot = input ("Enter overtime working hours from Mon to Sat: ")
    input_weekday_ot = int (weekday_ot)

    # Ask OT working hours - Mon to Sat 
    weekday_ot = input ("Enter overtime working hours from Mon to Sat: ")
    input_weekday_ot = int (weekday_ot)

    # Ask working hours - Sun
    sun = input ("Enter hours of work on Sun: ")
    input_sun = int (sun)

    # Ask OT working hours - Sun
    sun_ot = input ("Enter overtime working hours on Sun: ")
    input_sun_ot = int (sun_ot)
   
    # Ask working hours - PH

    ph = input ("Enter hours of work on public holiday: ")
    input_ph = int (ph)
    
    # Ask OT working hours - PH
    ph_ot = input ("Enter overtime working hours on public holiday: ")
    input_ph_ot = int (ph_ot)

    print ()

    return input_before6, input_after6, input_sat, input_weekday_ot, input_sun, input_sun_ot, input_ph, input_ph_ot

# Calculate salary
def calculate_salary ():

    while True:
        
        # work type
        #emp_type = input_type ()
        
        if (emp_type == "C"):

            input_before6, input_after6, input_sat, input_weekday_ot, input_sun, input_sun_ot, input_ph, input_ph_ot = working_hours ()
            
            # Overtime - Mon to Sat for the first 3 hours
            if (input_weekday_ot < 4 ):

                weekday_ot_salary = 37.47 * input_weekday_ot 

            # Overtime - Mon to Sat after 3 hours
            else:

                weekday_ot_salary = 37.47 * 3 + 48.17 * (input_weekday_ot - 3)
            
            # calculate salary
            salary = 26.76 * input_before6 + 27.83 * input_after6 + 29.97 * input_sat + weekday_ot_salary + 37.47 * input_sun + 48.17 * input_sun_ot + 53.53 * input_ph + 58.88 * input_ph_ot
        
        elif (emp_type == "F") or (emp_type == "P"):

            input_before6, input_after6, input_sat, input_weekday_ot, input_sun, input_sun_ot, input_ph, input_ph_ot = working_hours ()
            
            # Overtime - Mon to Sat for the first 3 hours
            if (input_weekday_ot < 4 ):

                weekday_ot_salary = 32.12 * input_weekday_ot 

            # Overtime - Mon to Sat after 3 hours
            else:

                weekday_ot_salary = 32.12 * 3 + 42.82 * (input_weekday_ot - 3)
            
            # calculate salary
            salary = 21.41 * input_before6 + 26.76 * input_after6 + 26.76  * input_sat + weekday_ot_salary + 35.33 * input_sun + 48.82 * input_sun_ot + 48.17 * input_ph + 53.53 * input_ph_ot

        return salary

# run main program
emp_type = input_type ()
#print ("Total working hours of the week is: {0}".format())
salary = calculate_salary ()
print ("Your employment type is : {0}".format(emp_type))
print ("Your salary before tax of the week is: AUD {0}".format(salary))

# taxable income

