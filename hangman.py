from hangman import utils
import threading #useful for shared_flag between process - tried but removed
import re, os, time

'''
countdown creation
'''
def countdown(lock, t): 
    global flag
    
    print('Try to do 3 within 2 minutes time')
    while t: 
        mins, secs = divmod(t, 60) 
        timer = '\n\n---------------------- Time : {:02d}:{:02d} ---------------------- \n\n'.format(mins, secs) 
        print(timer, end="\r") 
        time.sleep(5) 
        t -= 5
    lock.acquire()
    flag = True
    lock.release()

def setup():
    movieList = utils.give_movie(3)
    maskList = utils.mask_words(movieList)
    return movieList, maskList

def play(movieList:list, maskList:list):
    score = 0
    global flag
    for i,movie in enumerate(movieList):
        wrong_count = 0
        print(f'WORD : {maskList[i]}\n\n')
        while True:
           try:
            assert flag == False 
            guess = input('Enter your Guess : ')
            assert ord(guess.lower()) >=97 and ord(guess.lower()) <= 122 
            if '_' in maskList[i]:
                if guess.lower() in movie:
                    temp = list(maskList[i].replace(" ",""))
                    indexes = [x.start() for x in re.finditer(guess.lower(), movie)]
                    space_idx = [x.start() for x in re.finditer(' ', movie)]
                    for p in space_idx : temp.insert(p, " ")
                    for z in indexes: temp[z] = guess
                    print('WORD : '+" ".join(temp) +'\n\n')
                    maskList[i] = " ".join(temp)
                    if '_' in maskList[i]:
                        continue
                    else:
                        print('Hurrrayyy -- You Win')
                        score += 1
                        break
                    
                elif guess.lower() not in movie:
                    wrong_count += 1
                    if wrong_count <6:
                        utils.draw_hangman(wrong_count-1)
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
    if not flag and score/3 == 0:
        print('Out of attempts')
        print(f'Your Score : {score}')
    elif not flag and score/3 != 0:
        print(f'Your Score : {score}')
    

if __name__ == "__main__":
    movieList, maskList = setup()
    lock = threading.Lock()
    flag = False
    countdown = threading.Thread(target = countdown, args=(lock,10,))
    countdown.start()
    gameplay = threading.Thread(target=play, args=(movieList, maskList,))
    gameplay.start()
    

    

    
    

   