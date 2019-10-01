import re

# change list of string from 'YYYY Mon DD' to 'DD-MM-YYYY'

change_list = {
    "January": "01",
    "February": "02",
    "March": "03",
    "April": "04",
    "May": "05",
}
list_result = []

name = input("Enter file name: ")  # request file name
handler = open(name, "r")  # open file for analysis
f = open("result.txt", "w")  # create or recreate file result.txt
for row in handler:  # analysis of each row
    match = re.search(r"(\d+)\s([a-zA-Z]+)\s(\d+)", row)  # find pattern
    tmp_var = change_list[match.group(2)]  # tmp_var will contain Mon value
    result_var = (
        match.group(3) + "-" + tmp_var + "-" + match.group(1)
    )  # create new row under result_var variable
    f.write(result_var + "\n")  # put new row to new file
handler.close()
f.close()
