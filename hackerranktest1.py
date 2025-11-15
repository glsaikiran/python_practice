 n = int(input())

   # create_range=range(1,n+1)
    #int_to_string_list=[str(i) for i in create_range]
    #concat="".join(int_to_string_list)
    #print(concat)

    str_var_for_conc=""
    rg=range(1,n+1)
    for itera in rg:
        str_var_for_conc=str_var_for_conc+str(itera)
    print(str_var_for_conc)
