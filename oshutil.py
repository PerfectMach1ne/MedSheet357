# Origin sheet utilities (so specialized for my own old Google Sheet)
import re

import main

sh_origin = main.gc.open("The Plan") # This is the "origin sheet" on my Google Drive.


def getincidents(printmode):
    worksheet = sh_origin.sheet1
    dates = worksheet.col_values(main.map_column('A'))
    weekdays = worksheet.col_values(main.map_column('B'))
    datalist = list()

    incidents = worksheet.col_values(main.map_column('Y'))  # The Y column/Incidents column
    for date, weekday, incident in zip(dates, weekdays, incidents):
        # zip iterates over several iterables in parallel using tuples
        if printmode:
            if date == 'DATE':
                print(date, 5 * " ", str(weekday).ljust(9, ' '), incident)
                continue
            print(date, weekday.ljust(9, ' '), incident)
        else:
            tup = (date, str(weekday), incident)
            datalist.append(tup)
    if not printmode:
        return datalist


def getiddata(printmode):
    worksheet = sh_origin.sheet1
    dates = worksheet.col_values(main.map_column('A'))
    weekdays = worksheet.col_values(main.map_column('B'))
    datalist = list()

    iddata = worksheet.col_values(main.map_column('Z'))  # The Z column/ID Data column
    for date, weekday, data in zip(dates, weekdays, iddata):
        if printmode:
            if date == 'DATE':
                print(date, 5 * " ", weekday.ljust(9, ' '), data)
                continue
            print(date, weekday.ljust(9, ' '), data)
        else:
            tup = (date, str(weekday), data)
            datalist.append(tup)
    if not printmode:
        return datalist


def validateincidents():
    inclist = getincidents(False)
    sinclist = list()
    for inc in inclist:
        if inc[0] == 'DATE':
            continue
        newtup = inc[0], inc[1], inc[2]
        sinclist.append(newtup)
    for sinc in sinclist:
        rex = re.findall(r"E[1-3]=[0-2]?\d:[0-5]\d|AA=[0-2]?\d:[0-5]\d", sinc[2])
        print(sinc[0] + " " + str(rex))


def validateiddata():
    datalist = getiddata(False)


def getmeds(printmode):
    # Note: for some reason this extracts a string in a **list in a list**. Example
    # [['Ibooprofen']]
    worksheet = sh_origin.sheet1

    if printmode:
        print(worksheet.get("C1")[0][0])
        print(worksheet.get("G1")[0][0])
    else:
        return worksheet.get("C1:F1"), worksheet.get("G1:H1")


def getmedinfo(printmode):
    worksheet = sh_origin.sheet1
    dates = worksheet.col_values(main.map_column('A'))
    weekdays = worksheet.col_values(main.map_column('B'))

    if printmode:
        # Note: Might need to hardcode this due to API request limitations (also I know my dose history lol)
        pass
    else:
        print("Do nothing for now")
