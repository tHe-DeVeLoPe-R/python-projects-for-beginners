# game will contain 5 levels
# life of user will be one less than the attempts he can made 
# good guess  = +10
# wrong guess = -5

import random

# list of numbers from which user will predict
numbers_for_level_1 = [1,2,3,4,5]
numbers_for_level_2 = [1,2,3,4,5,6,7,8,9,10]

def second_level(user_score):
    print('-------- WELCOME TO LEVEL 2 ----------')
    total_score = user_score
    lives = 5
    generated_number = random.randint(1, len(numbers_for_level_2))
    for live in range(0,lives):
        print(f'Guess the number including 1 and {len(numbers_for_level_2)} you have {lives} lives remaining')
        user_choice = input()
        if int(user_choice) == generated_number:
            total_score = total_score + 10
            print(f'Hurry! you got it with total score {total_score}')
            levelUp = input('Move to the next level ? (y,n)')
            if levelUp == 'y':
                pass
            else:
                print(total_score)
        else:
            total_score = total_score - 5
            lives = lives - 1
            print(f'Wrong guess you lost 1 life and more 5 points , remaining lives are {lives}')
            if lives == 0:
                print(f"Game over !!! at level 2 ------ Right number was {generated_number}")
                print(f"your total score was {total_score}")
            
    
def level_one():
    total_score = 0
    lives = 4
    generated_number = random.randint(1, len(numbers_for_level_1))
    for live in range(0,lives):
        print(f'Guess the number including 1 and {len(numbers_for_level_1)} you have {lives} lives remaining')
        user_choice = input()
        if int(user_choice) == generated_number:
            total_score = total_score + 10
            print('Hurry! you got it')
            levelUp = input('Move to the next level ? (y,n)')
            if levelUp == 'y':
                second_level(total_score)
                break
            else:
                print(total_score)
        else:
            total_score = total_score - 5
            lives = lives - 1
            print(f'Wrong guess you lost 1 life and more 5 points , remaining lives are {lives}')
            if lives == 0:
                print(f"Game over !!! at level 1 ------ Right number was {generated_number}")
                print(f"your total score was {total_score}")

level_one()
