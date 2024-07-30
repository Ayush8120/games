from hangman import utils


def setup():
    movieList = utils.give_movie(3)
    maskList = utils.mask_words(movieList)

def play(maskList:list):
    pass
    