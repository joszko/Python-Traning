import os
import datetime

print(str(datetime.datetime.now()))

# directories with the files that are going to be compared
first_Dir = 'C:\\Users\\u8008701\\Desktop\\Python Gdynia\\CFG\\'
second_Dir = 'C:\\Users\\u8008701\\Desktop\\Python Gdynia\\GFD-1\\'

# dictionaries that are going to be used
first_Dir_Dict = {}
labels = {}

# loop through the files in the first directory, creating a dictionary with all the data
# os.listdir(path) creates a list with all the files in a given path

for file in os.listdir(first_Dir):
    row_count = 0
    first_Dir_Dict[file] = {}

    for row in open(first_Dir+file):

        # loop through the rows in the file, first row (row_count=0) are labels
        # creating a dictionary with all the headers indexed

        if row_count == 0:
            labels[file]={}

            # this part loops through the columns in each row, they are separated in the file with tabs "\t"

            # Code explain:
            # split() returns a list of all the words in the string, using given string as the separator ("\t")
            # enumerate(row.split("\t")[3:],1) - goes through the columns starting from the fourth one
            # and then iterating by 1
            # strip() returns a copy of the string in which all chars have been stripped from the beginning
            # and the end of the string - in this case all chars till the next row sign ("\n")

            for col_num, value in enumerate(row.split("\t")[3:],1):
                labels[file][col_num] = value.strip("\n")
                # print(labels)
                row_count += 1
        else:
            # row.split("\t")[0] - first value separated by tab
            # if we want to work on csv we should change tab to comma.
            # second column is skipped
            first_column = row.split("\t")[0]
            third_column = row.split("\t")[2]

            # result of the below code is a nested dictionary {file: {first_column: {third_column: {the rest}}}}

            first_Dir_Dict[file][first_column]={}
            first_Dir_Dict[file][first_column][third_column] = {}

            # below line need to be the same as above, otherwise there will be a mess and label won't fit the column
            for col_num,value in enumerate(row.split("\t")[3:],1):
                col_num = labels[file][col_num]
                first_Dir_Dict[file][first_column][third_column][col_num] = value.strip("\n")
                # print(first_Dir_Dict)
            row_count += 1

# loop through the files in the second directory, creating a dictionary with all the data

labels = {}
second_Dir_Dict = {}

for file in os.listdir(second_Dir):

    row_count = 0
    second_Dir_Dict[file] = {}

    for row in open(second_Dir+file):

        if row_count == 0:
            labels[file] = {}

            for col_num, value in enumerate(row.split("\t")[3:],1):
                labels[file][col_num] = value.strip("\n")
            row_count += 1
        else:
            first_column = row.split("\t")[0]
            third_column = row.split("\t")[2]

            second_Dir_Dict[file][first_column]={}
            second_Dir_Dict[file][first_column][third_column]={}

            for col_num, value in enumerate(row.split("\t")[3:], 1):
                col_num = labels[file][col_num]
                second_Dir_Dict[file][first_column][third_column][col_num] = value.strip("\n")
            row_count += 1

# opening with attribute "w" will clear the file
open("C:\\Users\\u8008701\\Desktop\\Python Gdynia\\Fail.txt", "w")
open("C:\\Users\\u8008701\\Desktop\\Python Gdynia\\Fail.txt", "w").close()
open("C:\\Users\\u8008701\\Desktop\\Python Gdynia\\Universe Mismatch.txt", "w")
open("C:\\Users\\u8008701\\Desktop\\Python Gdynia\\Universe Mismatch.txt", "w").close()

# comparing two dictionaries created above

# keys() returns a list of all the available keys in the dictionary.
# items() returns a list of tuples with the values

for file in second_Dir_Dict.keys():
    for first_column in second_Dir_Dict[file].keys():
        if not first_column in first_Dir_Dict[file].keys():
            # opens file and appends values to the end with attribute "a" - append
            # if the file doesn't exist, it will be created
            open("C:\\Users\\u8008701\\Desktop\\Python Gdynia\\Universe Mismatch.txt", "a").write(
                file + "\t" + first_column + "\t" + "Missing from CFG\n")
        else:
            for third_column in second_Dir_Dict[file][first_column].keys():
                for (lltype, llscore) in second_Dir_Dict[file][first_column][third_column].items():
                    if not third_column in second_Dir_Dict[file][first_column].keys():
                        open("C:\\Users\\u8008701\\Desktop\\Python Gdynia\\Universe Mismatch.txt", "a").write(file +
                        "\t" + first_column + "\t" + third_column + "  not in CFG\n")
                    else:
                        for (second_lltype, second_llscore) in first_Dir_Dict[file][first_column][third_column].items():
                            if not lltype == second_lltype: continue
                            if llscore == second_llscore:
                                # pass - dummy action, doesn't do anything
                                pass
                            else:
                                open("C:\\Users\\u8008701\\Desktop\\Python Gdynia\\Fail.txt", "a").write(file + "\t" +
                                str(first_column) + "\t" + lltype + "\t" + str(llscore) + "\t" + str(second_llscore)
                                 + "\t ~ Mismatch!\n")

print(str(datetime.datetime.now()))
print("Job's done")