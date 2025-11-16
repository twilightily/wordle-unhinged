def play_game():
    import random
    word_list=[]

    def random_():
        word_list.extend(['bark','meow','disk', 'lost', 'word', 'poem', 'fact', 'girl', 'town', 'love', 'dirt', 'rant', 'news', 'bird', 'army', 'milk','lily', 'node', 'shot', 'heat', 'race', 'debt', 'fade', 'bean', 'meal', 'pour', 'fire', 'hang', 'cage', 'take', 'pack', 'wake', 'trip', 'half', 'crop', 'pace', 'rung', 'dorm', 'grow', 'tidy','plot'])
        #random_list = ['bark','meow','disk', 'lost', 'word', 'poem', 'fact', 'girl', 'town', 'love', 'dirt', 'rant', 'news', 'bird', 'army', 'milk','lily', 'node', 'shot', 'heat', 'race', 'debt', 'fade', 'bean', 'meal', 'pour', 'fire', 'hang', 'cage', 'take', 'pack', 'wake', 'trip', 'half', 'crop', 'pace', 'rung', 'dorm', 'grow', 'tidy','plot']
    random_()

    #def clubs_():

    #def tech_():

    #def food_():

    #def pes_():


    index_of_word = random.randint (0, len(word_list))
    num_chances = 7

    secret_word = word_list[index_of_word]
    #secret_word = 'wood'
    found = False

    secret_word_letters = list(secret_word)

    while num_chances >=0:

        green_letters = []               # letters which are correctly guessed by user aka green
        not_green_secret_word = []       # letters from the secret word that are not guessed correctly aka they're EITHER GRAY OR YELLOW
        not_green_x = []                 # letters from the guessed word x that are not green (they are either gray or yellow)

        x = input("guess!:")
        if len(x) != 4:
            print("letter can only be 4 letters,you will lose a chance")
        
        x_letters = list(x)

        if x == secret_word:
            print("you guessed it!")
            found = True
            break

        else:
            for i in range(4):
                if x_letters[i] == secret_word_letters[i]:
                    green_letters.append((x_letters[i],'at position:', i+1))
                else:
                    not_green_secret_word.append(secret_word_letters[i])
                    not_green_x.append(x_letters[i])
            
            yellow_letters_count = 0
            for letter in not_green_secret_word:
                if letter in not_green_x:           # meaning if letter is yellow
                    yellow_letters_count += 1
                    not_green_secret_word.remove(letter)    # to handle repeated letterssss

        
            print("right letter right place:", green_letters)
            print("right letter wrong place:", yellow_letters_count)
            print("you have {} chances left".format(num_chances))
            num_chances-=1

    if not found:
        print("the word was:", secret_word)