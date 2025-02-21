import os
os.system("cls")
def get_day(a,b):
    match b:
        case 1: return 31
        case 2: return 29
        case 3: return 31
        case 4: return 30
        case 5: return 31
        case 6: return 30
        case _ if 7 <= b <= 8: return 31
        case 9: return 30
        case 10: return 31
        case 11: return 30
        case 12: return 31

a, b = map(int, input().split())
print(get_day(a,b))