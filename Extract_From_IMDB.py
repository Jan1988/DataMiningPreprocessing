import os

from Obj_Actor import Actor

if __name__ == '__main__':

    # Actor List from DB
    csv_file = os.path.join('Assets', 'actor_DB.csv')

    f = open(csv_file, "r")
    f.readline()

    db_actor_list = []

    for line in f:
        db_actor = Actor()

        line = line.replace("'", "")
        line = line.replace("\n", "")
        split_line = line.split(',', 4)

        L = len(split_line)

        if L == 3:
            db_actor.a_id = split_line[0]
            db_actor.firstname = split_line[2]
            db_actor.lastname = split_line[1]
        elif L == 2:
            db_actor.a_id = split_line[0]
            db_actor.lastname = split_line[1]

        db_actor_list.append(db_actor)

    # Actor List with Oscars from Flo
    csv_file_2 = os.path.join('Assets', 'ACTRESS_IN_A_LEADING_ROLE.csv')

    g = open(csv_file_2, "r")
    g.readline()

    aa_actor_list = []

    for line in g:
        aa_actor = Actor()

        line = line.replace("\n", "")
        split_line = line.split(";", 3)

        name = split_line[0].split(", ", 1)
        year = split_line[1]

        if len(name) < 2:
            aa_actor.lastname = name[0]
        else:
            aa_actor.lastname = name[0]
            aa_actor.firstname = name[1]

        if split_line[2] == 'WIN':
            aa_actor.academy_awards.append(year)
        else:
            aa_actor.nominees.append(year)

        aa_actor_list.append(aa_actor)

    for actor_temp in aa_actor_list[0:50]:
        print(actor_temp.firstname + ' ' + actor_temp.lastname + ' ', actor_temp.academy_awards)



