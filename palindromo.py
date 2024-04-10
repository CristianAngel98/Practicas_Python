for i in range(1, 6):
    palabraUser = input("Por favor ingrese una palabra: ").lower()

    if palabraUser == palabraUser[::-1]:
        print(palabraUser.upper(), " Esta palabra es Palindroma: ")
    else:
        print("Esta palabra !!! NO es Palindroma !!!")










"""
palabraUser = input("Por favor ingrese una palabra: ").lower()

if palabraUser == palabraUser[::-1]:
    print(palabraUser.upper(), " Esta palabra es Palindroma: ")
else:
    print("Esta palabra !!! NO es Palindroma !!!")""
"""