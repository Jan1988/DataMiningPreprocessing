import os

from Obj_Writer import Writer



if __name__ == '__main__':

    # Writer List from CSV
    csv_file = os.path.join('Assets', 'Awards_Writing_Neu.csv')
    f = open(csv_file, "r")
    f.readline()

    writers_list_orig_screen = []
    writers_list_adapted_screen = []
    writers_hash_values = []
    duplicates = 0


    year = 1900

    for line in f:


        award_winner = ''

        line = line.replace('"', "")
        line = line.replace(";", ",")
        line = line.replace("\n", "")
        line = line.replace(" & ", ",")
        line = line.replace(" and ", ",")
        line = line.replace("Written for the Screen by ", "")
        line = line.replace("Written for the screen by ", "")
        line = line.replace("Adapted for the screen by ", "")
        line = line.replace("Screen ", "")

        # line = line.replace(" ,", ",")

        if line[:4].isdigit():
            year = int(line[:4])
        elif line == 'WRITING (Adapted Screenplay),':
            writing_type = 'Adapted'
        elif line == 'WRITING (Original Screenplay),':
            writing_type = 'Original'
        else:
            line = line.replace("Original ", "")
            line = line.replace(", Jr.", " Jr.")
            line = line.replace(", ", ",")
            line = line.replace("Stories by ", "")



            split_line = line.split(',', 4)
            L = len(split_line)
            if split_line[L-1] == 'WIN':
                award_winner = 'OscarW'
            for names in split_line:
                if names != 'WIN' and names != '':

                    writer = Writer()
                    spl_name = names.split(' ', 4)
                    if len(spl_name) > 2:
                        writer.firstname = spl_name[0] + ' ' + spl_name[1]
                        writer.lastname = spl_name[2]
                        # print(spl_name[0] + ' ' + spl_name[1] + ', ' + spl_name[2] + ', ' + str(
                        #     year) + ', ' + award_winner + ', ' + writing_type)
                    elif len(spl_name) < 2:
                        writer.lastname = spl_name[0]
                        # print(spl_name[0] + ', ' + str(
                        #     year) + ', ' + award_winner + ', ' + writing_type)
                    else:
                        writer.firstname = spl_name[0]
                        writer.lastname = spl_name[1]
                        # print(spl_name[0] + ', ' + spl_name[1] + ', ' + str(
                        #     year) + ', ' + award_winner + ', ' + writing_type)

                    writer.year = year
                    writer.award_winner = award_winner
                    writer.writing_type = writing_type

                    hash_val = writer.__hash__()

                    if not hash_val in writers_hash_values:

                        if writing_type == 'Original':
                            writers_hash_values.append(hash_val)
                            writers_list_orig_screen.append(writer)
                        else:
                            writers_hash_values.append(hash_val)
                            writers_list_adapted_screen.append(writer)
                    else:
                        duplicates += 1
                        print(writer.lastname + ' ' + writer.firstname)
                        print(duplicates)

    writers_list_orig_screen.sort(key=lambda x: x.lastname, reverse=False)
    writers_list_adapted_screen.sort(key=lambda x: x.lastname, reverse=False)

    adapted_new_file = os.path.join('Assets', 'adapted_screen_writers.csv')
    g = open(adapted_new_file, 'w')
    g.write('Name;Year;Oscar\n')
    for writer in writers_list_adapted_screen:
        g.write(writer.lastname + ', ' + writer.firstname + ';' + str(writer.year) + ';' + writer.award_winner + '\n')  # python will convert \n to os.linesep

    g.close()

    original_new_file = os.path.join('Assets', 'original_screen_writers.csv')
    h = open(original_new_file, 'w')
    h.write('Name;Year;Oscar\n')
    for writer in writers_list_orig_screen:
        h.write(writer.lastname + ', ' + writer.firstname + ';' + str(writer.year) + ';' + writer.award_winner + '\n')  # python will convert \n to os.linesep

    h.close()
