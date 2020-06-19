#re robi lost

'''advanced_input module Version 1.1 by EZ ()
This module creats advanced inputs for Python.
They help to generate user save...
    ...varType specifice inputs.
    ...varType and multiple choise specifice inputs.'''
#----------------------------------------------------------------------------------------
def intInput(overlay_info='',main_info='',traceback_info=''):
    '''intInput generates an user save integer input.
        overlay_info (str) will be displayed the line over input line.
        main_info (str) will be displayed on the display line.
        traceback_info (str) will be displayed if the input fails due to ValueError
            input would be repeated'''
    if overlay_info!='':
        print(overlay_info)
    a=True
    while a:
        try:
            result=int(input(main_info))
        except:
            print(traceback_info)
            continue
        a=False
    return(result)
#----------------------------------------------------------------------------------------
def floatInput(overlay_info='',main_info='',traceback_info=''):
    '''floatInput generates an user save float input.
        overlay_info (str) will be displayed the line over input line.
        main_info (str) will be displayed on the display line.
        traceback_info (str) will be displayed if the input fails due to ValueError
            input would be repeated'''
    if overlay_info!='':
        print(overlay_info)
    a=True
    while a:
        try:
            result=float(input(main_info))
        except:
            print(traceback_info)
            continue
        a=False
    return(result)
#----------------------------------------------------------------------------------------
def strInput(overlay_info='',main_info='',traceback_info=''):
    '''strInput generates an user save string input.
        overlay_info (str) will be displayed the line over input line.
        main_info (str) will be displayed on the display line.
        traceback_info (str) will be displayed if the input fails due to ValueError
            input would be repeated'''
    if overlay_info!='':
        print(overlay_info)
    a=True
    while a:
        try:
            result=str(input(main_info))
        except:
            print(traceback_info)
            continue
        a=False
    return(result)
#----------------------------------------------------------------------------------------
def boolInput(overlay_info='',main_info='',traceback_info='',syn_true='True',syn_false='False'):
    '''boolInput generates an user save boolean input.
        overlay_info (str) will be displayed the line over input line.
        main_info (str) will be displayed on the display line.
        traceback_info (str) will be displayed if the input fails due to ValueError
            input would be repeated
        syn_true (str) is the synonym for the boolean value of "True", standard is "True"
        syn_false (str) is the synonym for the boolean value of "False", standard is "False"'''
        #efficiency!?
    if overlay_info!='':
        print(overlay_info)
    a=True
    while a:
        try:
            result=str(input(main_info))
            if result==syn_true:
                result=bool(True)
                break
            if result==syn_false:
                result=bool(False)
                break
            print(traceback_info)
            continue
        except:
            print(traceback_info)
            continue
        a=False
    return(result)
#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------
x=input('Hello')
print(x*2)
print('Tschüss')
print('fsef')
print('f*20')