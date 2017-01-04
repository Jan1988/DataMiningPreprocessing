import os
import re

from Obj_Movie_With_Genres import MovieWithGenres


def convert(name):
    s1 = re.sub("([a-z])([A-Z])","\g<1> \g<2>", name)
    label = re.sub(r'((?<=[a-z])[A-Z]|(?<!\A)[A-Z](?=[a-z]))', r' \1', name)
    return label


def camel_case(identifier):
    regex = re.sub("([^-])([A-Z][a-z-]+)", r"\1 \2", identifier)
    return regex


if __name__ == '__main__':

    # Movies with Genres from CSV
    csv_file = os.path.join('Assets', 'MOVIE.csv')
    e = open(csv_file, "r")
    e.readline()

    movie_list_db = []
    hash_list_db = []

    for e_line in e:
        movie_no_genres = MovieWithGenres()
        split_e_line = e_line.split(';')
        movie_no_genres.m_id = split_e_line[0]
        movie_no_genres.title = split_e_line[1]
        movie_no_genres.year = int(split_e_line[2])
        hash_no_genres = movie_no_genres.__hash__()
        movie_list_db.append(movie_no_genres)
        hash_list_db.append(hash_no_genres)

    print('movie_list_db: ' + str(len(movie_list_db)))
    print('hash_list_db: ' + str(len(hash_list_db)))

    # Movies with Genres from CSV
    csv_file = os.path.join('Assets', 'Movie_And_Genre.csv')
    f = open(csv_file, "r")
    f.readline()

    ghost = MovieWithGenres()
    ghost.title = 'Ghost'
    ghost.year = 1990

    if ghost.__hash__() in hash_list_db:
        print('Ghost')

    # genre_new_file = os.path.join('Assets', 'Movie_And_Genre_New.csv')
    # g = open(genre_new_file, 'w')
    # g.write('Name;Year;Genres\n')


    # Initialwerte
    movie_list_genre = []
    hash_list_genre = []
    prev_line_movie_title = ''
    movie = MovieWithGenres()

    i = 0
    for line in f:
        if '(' in line:
            year_pos = line.index('(') + 1
            year = line[year_pos:year_pos+4]

            is_year = year.isdigit()

            if is_year and 1979 < int(year) < 2017:

                year_string = ' (' + year + ')'
                line = line.replace('#', '')
                line = line.replace('\n', '')
                line = line.replace(year_string, '')
                split_line = line.split(';')

                # print(convert(split_line[0]))

                # Wenn vorheriger titel nicht mit dem neuem titel übereinstimmt,
                # dann erstelle neues Movie Objekt
                if prev_line_movie_title != split_line[0]:
                    # print(movie.title + ';' + str(movie.genres))
                    # g.write(movie.title + ';' + str(movie.year) + ';' + str(movie.genres) + '\n')  # python will convert \n to os.linesep
                    hash_with_genres = movie.__hash__()
                    if hash_with_genres in hash_list_db:
                        print(movie.title)
                        i += 1
                    movie = MovieWithGenres()
                    movie.year = year
                    movie.title = split_line[0]

                movie.genres.append(split_line[1])

                prev_line_movie_title = movie.title



    print(i)


    # g.close()