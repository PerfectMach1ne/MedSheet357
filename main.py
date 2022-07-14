import gspread
import cmd

# End User OAuth Client for original spreadsheet
gc = gspread.oauth()
sh_origin = gc.open("The Plan")


# Maps column letters to numerical values used by some gspread methods
def map_column(col):
    column_ids = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                  'U', 'V', 'W', 'X', 'Y', 'Z']
    return column_ids.index(col.upper()) + 1


class MedSheet(cmd.Cmd):
    intro = '\n'.join(['MedSheet357 command line shell.',
                       'For assisting tracking medicine intake via Google Sheets API.',
                       'Type \'?\' or \'help\' to list all the commands.'
                       ])
    prompt = '> '

    def do_readA1(self, line):
        'Read the A1 cell.'
        print(sh_origin.sheet1.get('A1'))

    # Default implementation repeats last command. This overrides that to do nothing.
    def emptyline(self) -> bool:
        return

    def do_osh(self, line):
        'Manage origin spreadsheet.'
        worksheet = sh_origin.sheet1
        dates = worksheet.col_values(map_column('A'))
        weekdays = worksheet.col_values(map_column('B'))
        if line == 'getincidents':
            incidents = worksheet.col_values(map_column('Y')) # The Y column/Incidents column
            for date, weekday, incident in zip(dates, weekdays, incidents):
                # zip iterates over several iterables in parallel using tuples
                if date == 'DATE':
                    print(date, 5*" ", str(weekday).ljust(9, ' '), incident)
                    continue
                print(date, weekday.ljust(9, ' '), incident)
        elif line == 'getiddata' or 'getdata':
            iddata = worksheet.col_values(map_column('Z')) # The Z column/ID Data column
            for date, weekday, data in zip(dates, weekdays, iddata):
                if date == 'DATE':
                    print(date, 5*" ", weekday.ljust(9, ' '), data)
                    continue
                print(date, weekday.ljust(9, ' '), data)

    def do_createsh(self, line):
        'Creates a new spreadsheet.'
        while True:
            try:
                choice = input('Are you sure you want to create a new spreadsheet? (y/N) ')
                if choice.lower() == 'y':
                    print('where doing it man\nwhere MAKING THIS HAPEN')
                    return
                elif choice.lower() == 'n':
                    return

            except ValueError:
                pass

    def do_exit(self, line):
        'Exit the command line.'
        return True


if __name__ == "__main__":
    MedSheet().cmdloop()
