secret_number=6
guess_count=0
guess_limit=5
while guess_count<5:
    guess=int(input('Guess: '))
    guess_count=guess_count+1
    if guess==secret_number:
        print('You won!!')
    break
    if guess_count>4;
        print('You loose!!')


