import os

from Obj_Composer import Composer



if __name__ == '__main__':


    #Composer Winners List
    winner_file = os.path.join('Assets', 'Winners_Composer.csv')
    e = open(winner_file, "r")
    e.readline()

    winners_hash_list = []

    for winners_line in e:

        winners_line = winners_line.replace("\n", "")

        winner = Composer()
        split_winners_line = winners_line.split(';', 3)
        name_part = split_winners_line[0]
        winner.year = int(split_winners_line[1])-1

        split_winners_name = name_part.split(' ', 4)
        if len(split_winners_name) > 2:
            winner.firstname = split_winners_name[0] + split_winners_name[1]
            winner.lastname = split_winners_name[2]
        elif len(split_winners_name) < 2:
            winner.lastname = split_winners_name[0]
        else:
            winner.lastname = split_winners_name[1]
            winner.firstname = split_winners_name[0]

        winners_hash_list.append(winner.__hash__())

    # Composer List from CSV
    txt_file = os.path.join('Assets', 'Composer.csv')
    f = open(txt_file, "r")
    f.readline()

    composer_list = []
    comp_hash_values = []
    duplicates = 0
    year = 1900

    now_comes_composer = False

    for line in f:
        line = line.replace("\n", "")
        line = line.replace("Music by ", "")
        line = line.replace("Music and Lyrics by ", "")
        line = line.replace("Lyrics by ", "")
        line = line.replace("Orchestral Score by ", "")
        line = line.replace("Song Score by ", "")
        line = line.replace("Adaptation Score by ", "")
        line = line.replace(" and ", ", ")
        line = line.replace(";", ",")
        # print(line)

        if line:
            if line[:4].isdigit():
                year = int(line[:4])
            elif line == '--':
                now_comes_composer = True
            else:
                if now_comes_composer:

                    composer_line = line
                    split_composers = line.split(', ', 20)
                    for composer_line in split_composers:
                        composer = Composer()
                        composer.year = year

                        split_composer = composer_line.split(' ', 4)
                        if len(split_composer) > 2:
                            composer.firstname = split_composer[0]
                            composer.lastname = split_composer[1] + ' ' + split_composer[2]
                        elif len(split_composer) < 2:
                            composer.lastname = split_composer[0]
                        else:
                            composer.lastname = split_composer[1]
                            composer.firstname = split_composer[0]

                        comp_hash = composer.__hash__()

                        if comp_hash in winners_hash_list:
                            composer.award_winner = 'OscarW'

                        # duplikate filtern
                        if not comp_hash in comp_hash_values:
                            comp_hash_values.append(comp_hash)
                            composer_list.append(composer)

                            print(composer.lastname + ',' + composer.firstname + ';' + str(composer.year) + ';' +
                                  composer.award_winner)
                        else:
                            duplicates += 1
                            print(composer.lastname + ' ' + composer.firstname)
                            print(duplicates)




                    now_comes_composer = False
                else:
                    movie = line

    composer_list.sort(key=lambda x: x.lastname, reverse=False)

    composer_awarded = os.path.join('Assets', 'Awards_Composer.csv')
    g = open(composer_awarded, 'w')
    g.write('Name;Year;Oscar\n')
    for composer_item in composer_list:
        g.write(composer_item.lastname + ', ' + composer_item.firstname + ';' + str(composer_item.year) + ';' +
                composer_item.award_winner + '\n')  # python will convert \n to os.linesep

    g.close()