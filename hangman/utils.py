import random, copy

'''
fetching movie names
'''
def give_movie(count=3):
    file1 = open('movie_names.txt', 'r')
    Lines = file1.readlines()
    pool = []
    for l in Lines:
        l = l.replace('\n','')
        pool.append(l)
    return random.sample(pool,count)

'''
masking movie names
'''
def mask_words(movieList):
    for movie in movieList:
        print(len(movie))
        print(movie)
        temp = copy.deepcopy(movie)
        dash = random.randint(3,len(temp.replace(" ", ""))-1) # introduce checks that no word less than 3 length
        print(f'dash : {dash}')
        idxList = random.sample(range(len(movie)), dash)
        print(f'idxList : {idxList}')
        for i, idx in enumerate(idxList):
            if movie[idx] == ' ':
                print('yes')        
                idxList[i] += 1
                assert idxList[i] < len(movie)
        #might be possible that the next idx already is present in idxList : so repetition         
        if len(set(idxList)) != len(list(idxList)): idxList = list(set(idxList))
        dashMovie = list(movie)
        for idx in idxList:
            dashMovie[idx] = '_'
        print(" ".join(dashMovie))
    return movieList

'''
visualization of game progress
'''
def draw_hangman(wrong_guesses):
    
    hanged_man = [
        r"""
        -----
        |   |
            |
            |
            |
            |
            |
            |
            |
            |
        -------
        """,
        r"""
        -----
        |   |
        O   |
            |
            |
            |
            |
            |
            |
            |
        -------
        """,
        r"""
        -----
        |   |
        O   |
       ---  |
        |   |
        |   |
            |
            |
            |
            |
        -------
        """,
        r"""
        -----
        |   |
        O   |
       ---  |
      / |   |
        |   |
            |
            |
            |
            |
        -------
        """,
        r"""
        -----
        |   |
        O   |
       ---  |
      / | \ |
        |   |
            |
            |
            |
            |
        -------
        """,
        r"""
        -----
        |   |
        O   |
       ---  |
      / | \ |
        |   |
       ---  |
      /     |
            |
            |
        -------
        """,
        r"""
        -----
        |   |
        O   |
       ---  |
      / | \ |
        |   |
       ---  |
      /   \ |
            |
            |
        -------
      
      You Are Dead
        
      
        """,
            ]

    print(hanged_man[wrong_guesses])