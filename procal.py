import time

def greeting():
    print("Hello There! I am here to help you find the proration for your move in/move out.")
    time.sleep(1)

def workflow():
    workflow.momi = input('Is this a MI or MO?: ')

    if workflow.momi == str('mo') or str('MO'):
        moveout()
           
    elif workflow.momi == str('mi') or str('MI'):
        movein()

def restart():
    restart.restart = input('Would you like to do another?: ')

    if restart.restart == str('yes'):
        workflow()
    
    elif restart.restart == str('no'):
        quit()

def mon():
    month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    mon.mon = input('Month: ')

    if mon.mon == str('1'):
        mon.mon = float(month[0])
    elif mon.mon == str('2'):
        mon.mon = float(month[1])
    elif mon.mon == str('3'):
        mon.mon = float(month[2])
    elif mon.mon == str('4'):
        mon.mon = float(month[3])
    elif mon.mon == str('5'):
        mon.mon = float(month[4])
    elif mon.mon == str('6'):
        mon.mon = float(month[5])
    elif mon.mon == str('7'):
        mon.mon = float(month[6])
    elif mon.mon == str('8'):
        mon.mon = float(month[7])
    elif mon.mon == str('9'):
        mon.mon = float(month[8])
    elif mon.mon == str('10'):
        mon.mon = float(month[9])
    elif mon.mon == str('11'):
        mon.mon = float(month[10])
    elif mon.mon == str('12'):
        mon.mon = float(month[11])

    return(mon.mon)

def movein():
    movein.month = mon()
    movein.day = input('MI Day: ')
    movein.rent = input('Rent Amount: ')
    
    dof = ((float(movein.month) - float(movein.day)) + 1)
    done = ((float(movein.rent) / float(movein.month)) * dof)
    
    print(round(done, 2))

    restart()

def moveout():
    moveout.month = mon()
    moveout.day = input('MO Day: ')
    moveout.rent = input('Rent Amount: ')

    done2 = ((float(moveout.rent) / float(moveout.month)) * float(moveout.day))
    
    print(round(done2, 2))

    restart()

if __name__ == '__main__':
    greeting()
    workflow()
