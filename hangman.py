from hangman import utils
import threading 
import re, os, time

'''
countdown creation
'''
def countdown(lock, t): 
    global flag
    while t and not flag: 
        mins, secs = divmod(t, 60) 
        timer = '\n\n---------------------- Time : {:02d}:{:02d} ---------------------- \n\n'.format(mins, secs) 
        print(timer, end="\r") 
        if flag:
            break
        time.sleep(5) 
        t -= 5
    if not flag:
        lock.acquire()
        flag = True
        lock.release()

def setup():
    while True:
        try:
            rounds = int(input('How many words can you do in 2 minutes?\n'))
            break
        except:
            continue
    movieList = utils.give_movie(rounds)
    maskList = utils.mask_words(movieList)
    return rounds, movieList, maskList

def play(rounds:int, movieList:list, maskList:list):
    score = 0
    global flag
    for i,movie in enumerate(movieList):
        guess_hist = []
        wrong_count = 0
        print(f'WORD : {maskList[i]}\n')
        while True:
           try:
            assert flag == False 
            guess = input('Enter your Guess : ')
            assert ord(guess.lower()) >=97 and ord(guess.lower()) <= 122 
            guess_hist.append(guess)
            print(f'Guess history : {set(guess_hist)}\n')
            if '_' in maskList[i]:
                if guess.lower() in movie:
                    temp = list(maskList[i].replace(" ",""))
                    indexes = [x.start() for x in re.finditer(guess.lower(), movie)]
                    space_idx = [x.start() for x in re.finditer(' ', movie)]
                    for p in space_idx : temp.insert(p, " ")
                    for z in indexes: temp[z] = guess.lower()
                    print('WORD : '+" ".join(temp) +'\n')
                    maskList[i] = " ".join(temp)
                    print('Great Guess!\n')
                    if '_' in maskList[i]:
                        continue
                    else:
                        print('Hurrrayyy -- You Win')
                        score += 1
                        break
                    
                elif guess.lower() not in movie:
                    wrong_count += 1
                    print('Wrong Guess!')
                    if wrong_count <6:
                        utils.draw_hangman(wrong_count-1)
                        print(f'WORD : {maskList[i]}' +'\n')
                        continue
                    else:
                        utils.draw_hangman(wrong_count)
                        print('Game Over - You lose this point')
                        break
                            
        
           except Exception as e:
               print(e)
               if flag:
                   print('Oops! You Ran Out of Time!')
                   print(f'Your Score : {score}')
                   break
               continue
        if flag:
            break
        
    if not flag and score < rounds:
        print('Out of attempts')
        print(f'Your Score : {score}')
    elif not flag and score == rounds:
        print('Congrats!!')
        print(f'Your Score : {score}')
    lock.acquire()
    flag = True
    lock.release()
    

if __name__ == "__main__":
    rounds, movieList, maskList = setup()
    lock = threading.Lock()
    flag = False
    countdown = threading.Thread(target = countdown, args=(lock,120,))
    countdown.start()
    gameplay = threading.Thread(target=play, args=(rounds, movieList, maskList,))
    gameplay.start()
    

    

    
    

   