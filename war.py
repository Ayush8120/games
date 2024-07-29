import random, logging
logging.basicConfig(level=logging.DEBUG,
            filename="app.log",
            encoding="utf-8",
            filemode="a",
            format="{asctime} - {levelname} - {message}",
            style="{",
            datefmt="%Y-%m-%d %H:%M",
        )

class Card():
    '''
    Card Class : defines the identity of a 'Card' i.e. value and suit and rank
    '''
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def toString(self):
        return self.value + 'of' + self.suit
    
    def getRank(self):
        ranks = {"Ace":14,"King":13,"Queen":12,"Jack":11,"10":10,"9":9,"8":8,"7":7,"6":6,"5":5,"4":4,"3":3,"2":2}
        return ranks[self.value]

class Deck():
    '''
    Creates a new deck class and adds all 52 to the deck
    '''
    def __init__(self):
        self.deck = []
        self.reset() # add all 52 to the deck
    
    def reset(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        for suit in suits:
            for value in values:
                self.deck.append(Card(value,suit))
    
    def shuffle(self):
        random.shuffle(self.deck)

    
if __name__ == '__main__':
    max_round = int(input('How many rounds do you want to simulate: '))
    show = input('Do you want too record the gameplay? (T/F)')
    SHOW_CARDS = 1 if show.lower() == 't' else 0 if show.lower() == 'f' else -1   
    deck = Deck()
    deck.shuffle()
    fullDeck = deck.deck
    scorePlayer1 = 0
    scorePlayer2 = 0
    deckPlayer1 = random.sample(fullDeck, 26)
    deckPlayer2 = list(set(fullDeck) - set(deckPlayer1))
    logging.info('We have distributed the cards')
    round = 1
    battleground = []
    
    while round <= max_round: 
        try: 
            card1 = deckPlayer1.pop()
            if SHOW_CARDS:
                logging.info(f'Player 1 plays : {card1.toString()}')
                
        except: 
            logging.info('-- Player 1 out of cards --')
            deckPlayer2[:0] = battleground
            battleground = []
            round += 1
            break
            
        try:
            card2 = deckPlayer2.pop()
            if SHOW_CARDS:
                logging.info(f'Player 2 plays : {card2.toString()}')
                      
        except:
            logging.info('-- Player 2 out of cards --')
            deckPlayer1[:0] = battleground
            round += 1
            battleground = []
            break

        battleground.append(card1)
        battleground.append(card2)
        if SHOW_CARDS: print(f'BattleGround: {[i.toString() for i in battleground]}')

        if card1.getRank() > card2.getRank():
            deckPlayer1[:0] = battleground
            scorePlayer1 += 1
            battleground = []
            round += 1
            logging.info('Player 1 Point')
            print()

        elif card1.getRank() < card2.getRank():
            deckPlayer2[:0] = battleground
            scorePlayer2 += 1
            round += 1
            battleground = []
            logging.info('Player 2 Point')
            print()

        elif card1.getRank() == card2.getRank():
            try: 
                '''
                check if either player is out of cards to continue the draw
                '''
                battleground.append(deckPlayer1.pop())
                battleground.append(deckPlayer2.pop())
                #each player adds 2 face down cards to the battleground
                if SHOW_CARDS: print(f'BattleGround: {[i.toString() for i in battleground]}')

            except:
                logging.warning('Someone is out of cards')
                continue

            logging.info('No Point - play continues')
            print()

    print(f'Score: {scorePlayer1} - {scorePlayer2}')
    logging.info(f'Card Count: {len(deckPlayer1)} - {len(deckPlayer2)}')
    
    if len(deckPlayer1) > len(deckPlayer2):
        winner = 1
    elif len(deckPlayer1) < len(deckPlayer2):
        winner = 2
    else:
        winner = 1 if scorePlayer1 > scorePlayer2 else 2 if scorePlayer1 < scorePlayer2 else 'DRAW'

    logging.info(f'Winner : Player {winner}')
                