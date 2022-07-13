import gspread

gc = gspread.oauth()

sh = gc.open("The Plan")
print(sh.sheet1.get('A1'))
print(sh.sheet1.get('C27:E31'))
print(sh.sheet1.get('Y53:Y57'))
# I want to weep like a gorilla
# I made this comment just to show a middle finger to git