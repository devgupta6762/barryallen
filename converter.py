weight=int(input('what is your weight: '))
unit=input('(L)bs or (K)g: ')
if unit.upper()=="L":
    converted=(weight)*0.45
    print(f"your weight is  {converted} kilos ")
else:
    converted=(weight)//0.45
    print(f"your weight is  {converted} pounds")
