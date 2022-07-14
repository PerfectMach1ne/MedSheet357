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
        if line == 'getincidents':
            worksheet = sh_origin.sheet1
            values_list = worksheet.col_values(map_column('Y'))  # The Y column
            print(values_list)

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


# print(sh_origin.sheet1.get('A1'))
# print(sh_origin.sheet1.get('C27:E31'))
# print(sh_origin.sheet1.get('Y53:Y57'))


if __name__ == "__main__":
    MedSheet().cmdloop()
