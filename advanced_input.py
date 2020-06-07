#used for user-friendly int/str/float inputs
'overlay_info is displayed one line above input-line'
'main_info is displayed ON input-line'
'traceback_info is just displayed if input fails'
#-----------------------------------------------------------------------
#internal function to splice limitationkey for limited inputs
def limit_splice(limit):
    cache,limitation_list,loci='',[],0
    for i in range(len(limit)):
        if limit[i]!='/':
            cache+=limit[i]
        else:
            limitation_list+=['']
            limitation_list[loci]+=cache
            cache=''
            loci+=1
    return limitation_list
#-----------------------------------------------------------------------
#unlimited integer input
def int_input(overlay_info='',main_info='',traceback_info=''):
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
#-----------------------------------------------------------------------
def int_limited_input(limitationkey,overlay_info='',main_info='',traceback_info=''):
    limitation_list=limit_splice(limitationkey)
    for i in range(len(limitation_list)):
        pass
#-----------------------------------------------------------------------
def float_input(overlay_info='',main_info='',traceback_info=''):
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
#-----------------------------------------------------------------------
#-----------------------------------------------------------------------
def str_input(overlay_info='',main_info='',traceback_info=''):
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
#-----------------------------------------------------------------------
#-----------------------------------------------------------------------
def bool_input(overlay_info='',main_info='',traceback_info=''):
    if overlay_info!='':
        print(overlay_info)
    a=True
    while a:
        try:
            result=bool(input(main_info))
        except:
            print(traceback_info)
            continue
        a=False
    return(result)
#-----------------------------------------------------------------------
#-----------------------------------------------------------------------
ghgzvl
