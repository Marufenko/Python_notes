import os

def main():
    file_name = return_file()
    dictionary_with_rows = file_handler(file_name)

    # show all exist rows:
    if dictionary_with_rows:
        for k, v in dictionary_with_rows.items():
            print(k, '|', v)
    else:
        print('no items are in the list')


def new_file():
    # function returns name for new file
    return input("Please enter name for new file: ") + ".lst"

def return_file():

    # select all files from current directory
    all_file_list = os.listdir(".")

    # select only *.lst files
    lst_file_list = []
    for i in range(len(all_file_list)):
        if all_file_list[i][-4:] == '.lst':
            lst_file_list.append(all_file_list[i])

    # block handles case when no *.lst files in folder
    if len(lst_file_list) == 0:
        return new_file()

    # print *.lst file list
    print("List of available files:")
    for i in range(len(lst_file_list)):
        print(i+1, '|', lst_file_list[i])
    print("\n")

    # request file number from user
    file_number = input("Please enter file number or zero to create new file: ")

    # return file name for following processing
    if file_number == "0":
        return new_file()
    else:
        # handler of Index Error
        try:
            return lst_file_list[int(file_number)-1]
        except IndexError:
            print("Wrong file number")

def file_handler(file_name):
    # open file with read/write priviledges
    open_file = open(file_name, 'r+')

    # create dictionary with rows nad their numbers
    row_dict = {}
    row_count = 1
    for line in open_file:
        row_dict[row_count] = line
        row_count += 1

    # return dictionary
    return row_dict


if __name__ == "__main__":
    main()