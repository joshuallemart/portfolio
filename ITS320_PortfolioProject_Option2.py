# create a yes list for yes options
yeslist = ['y', 'Y', 'yes', 'Yes', 'YES', 'yeah', 'Yeah', 'YEAH']
# create dictionary to add entries
directory = {}
# class for Home
class Home:
    
    def __init__(self, address, city, state, zipcode, Modelname, squarefeet, salestatus):
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.Modelname = model
        self.squarefeet = squarefeet
        self.salestatus = status

    def get_input():
        
        print('Enter: address, city, state, zipcode, model, squarefeet, status')
        address, city, state, zipcode, model, squarefeet, status = input().split(', ')

        print('\n', address, '\n ', city, state, zipcode, '\n ', model, '\n ', squarefeet, 'sqft', '\n ', status)

        print('\nIs this correct?')
        confirm = str(input())

        if confirm in yeslist:
            directory[address] = {'City': city,
                      'State': state,
                      'Zipcode': int(zipcode),
                      'Model': model,
                      'Squarefeet': int(squarefeet),
                      'SaleStatus': status}
        else:
            print('Try again')
            Home.get_input()

def main():
    print('\nSelect an option')
    print('\n 1. Add a home\n 2. Remove a home\n 3. Update a home\n 4. Show directory\n 5. Export directory\n 6. Exit')

    option = int(input())

    if option == 1:
        Home.get_input()
        main()

    elif option == 2:
        print('\nEnter an address to remove from directory')
        remove = str(input())

        if remove in directory:
            del directory[remove]
            main()

        else:
            print('Address not found!')
            main()

    elif option == 3:
        print('\nEnter an address to update')
        update_key = str(input())

        if update_key in directory:
            print('\n', directory[update_key])
            print('Select a value to change (i.e. City, State, etc.)')
            update_val = str(input())
            print('\nEnter new value for', update_val)
            directory[update_key][update_val] = input()
            main()

        else:
            print('Address not found!')
            main()

    elif option == 4:
        for key, value in directory.items():
            print('\n', key, '\n', value)
        main()

    elif option == 5:
        directory_file = open('directory.txt', 'w')
        for key in directory:
            directory_file.write('%s\n %s %s %s\n %s\n %s sqft\n %s\n' % (key,
                                                                        directory[key]['City'],
                                                                        directory[key]['State'],
                                                                        directory[key]['Zipcode'],
                                                                        directory[key]['Model'],
                                                                        directory[key]['Squarefeet'],
                                                                        directory[key]['SaleStatus']))
            directory_file.write('\n')
            
        print('\nDirectory has been exported successfully!')
        directory_file.close()
        
        print('\nWould you like to continue?')
        answer = str(input())

        if answer in yeslist:
            main()

        else:
            exit()

    elif option == 6:
        exit()

    else:
        print('Input not recognized')
        main()

main()
