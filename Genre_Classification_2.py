import os
import re

from Obj_Movie_With_Genres import MovieWithGenres


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
    csv_file = os.path.join('Assets', 'Train_Metadata.csv')
    f = open(csv_file, "r")
    f.readline()

    # ghost = MovieWithGenres()
    # ghost.title = 'Ghost'
    # ghost.year = 1990
    #
    # if ghost.__hash__() in hash_list_db:
    #     print('Ghost')

    # Initialwerte
    genres = ['Comedy', 'Short', 'Drama', 'Animation', 'News', 'History', 'War', 'Horror', 'Adventure', 'Sci_Fi',
              'Biography','Documentary','Family','Action','Adult','Romance','Musical','Sport','Fantasy','Mystery',
              'Thriller','Music','Crime','Western']
    movie_list_genre = []
    hash_list_genre = []
    prev_line_movie_title = ''


    i = 0
    for line in f:
        split_line = line.split('\t')

        movie = MovieWithGenres()
        movie.title = split_line[1][:-7]
        movie.year = int(split_line[2])
        hash_val_movie = movie.__hash__()

        if hash_val_movie in hash_list_db:

            movie.m_id = movie_list_db[hash_list_db.index(hash_val_movie)].m_id

            genre_indices = []
            for index, item in enumerate(split_line[-24:]):

                if int(item) == 1:
                    movie.genres += genres[index] + ','
                    genre_indices.append(index)
            print(movie.title + ' - ' + movie.genres)

            i += 1
            movie_list_genre.append(movie)

    print(i)

    movie_list_genre.sort(key=lambda x: x.title, reverse=False)

    movie_genre_file = os.path.join('Assets', 'Movie_And_Genre_New.csv')
    g = open(movie_genre_file, 'w')
    g.write('MID;TITLE;YEAR;GENRES\n')
    for write_movie in movie_list_genre:
        g.write(str(write_movie.m_id) + ';' + write_movie.title + ';' + str(write_movie.year) + ';' +
                write_movie.genres + '\n')  # python will convert \n to os.linesep

    g.close()