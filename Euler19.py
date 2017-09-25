MonthBaseDays = {"1":31,"2":28,"3":31,"4":30,"5":31,"6":30,"7":31,"8":31,"9":30,"10":31,"11":30,"12":31};
DayOfWeek = 1;
Year = 1900;
Sundays = 0;
Month = 0;
while Year<2001:
    if DayOfWeek == 0:
        if Year>1900:
            Sundays+=1;

    DayOfWeek += MonthBaseDays[str(Month+1)];
    if Month ==1:
        if Year%4==0:
            DayOfWeek+=1;
    Month = (Month+1)%12;
    if Month == 0:
        Year+=1;
    DayOfWeek = DayOfWeek%7;

print(Sundays);
