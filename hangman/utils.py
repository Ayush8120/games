import random, copy, time

'''
countdown creation
'''
def countdown(shared_flag, t): 
    print('Try to do 3 within 2 minutes time')
    while t: 
        mins, secs = divmod(t, 60) 
        timer = '                                                         {:02d}:{:02d}'.format(mins, secs) 
        print(timer, end="\r") 
        time.sleep(10) 
        t -= 10
    shared_flag.value = -1
    
      
'''
fetching movie names
'''
def give_movie(count=3):
    file1 = open('movie_names.txt', 'r')
    Lines = file1.readlines()
    pool = []
    for l in Lines:
        l = l.replace('\n','').lower()
        pool.append(l)
    return random.sample(pool,count)

'''
masking movie names
'''
def mask_words(movieList):
    maskList = []
    for movie in movieList:
        temp = copy.deepcopy(movie)
        dash = random.randint(3,len(temp.replace(" ", ""))-1) # introduce checks that no word less than 3 length
        idxList = random.sample(range(len(movie)), dash)
        for i, idx in enumerate(idxList):
            if movie[idx] == ' ':
                idxList[i] += 1
                assert idxList[i] < len(movie)
        #might be possible that the next idx already is present in idxList : so repetition         
        if len(set(idxList)) != len(list(idxList)): idxList = list(set(idxList))
        dashMovie = list(movie)
        for idx in idxList:
            dashMovie[idx] = '_'
        # print(" ".join(dashMovie))
        maskList.append(" ".join(dashMovie).lower())
    return maskList

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