from hangman import utils
import multiprocessing as mp #useful for shared_flag between process - tried but removed
import re

def setup():
    movieList = utils.give_movie(3)
    maskList = utils.mask_words(movieList)
    return movieList, maskList

def play(movieList:list, maskList:list):
    score = 0
    
    for i,movie in enumerate(movieList):
        wrong_count = 0
        print(f'WORD : {maskList[i]}')
        while True:
           guess = input('Enter your Guess : ')
           try:
            assert ord(guess.lower()) >=97 and ord(guess.lower()) <= 122 
            if '_' in maskList[i]:
                if guess.lower() in movie:
                    temp = list(maskList[i].replace(" ",""))
                    indexes = [x.start() for x in re.finditer(guess.lower(), movie)]
                    space_idx = [x.start() for x in re.finditer(' ', movie)]
                    for p in space_idx : temp.insert(p, " ")
                    for z in indexes: temp[z] = guess
                    print(" ".join(temp))
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
                        utils.draw_hangman(wrong_count-1)
                        print('Game Over - You lose this point')
                        break
                            
        
           except Exception as e:
               print(e)
               continue
    return score

if __name__ == "__main__":
    movieList, maskList = setup()
    shared_flag = mp.Value('i', 0)
    countdown = mp.Process(target = utils.countdown, args=(shared_flag,120,))
    countdown.daemon = True
    countdown.start()
    score = play(movieList, maskList)
    if shared_flag.value == -1:
       print('You Lose : On Time')
    elif score/3 == 0:
        print('Out of attempts')
    print(f'Your Score : {score}')
    
   