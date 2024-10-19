import random
from django.shortcuts import render

# Game options
choices = ['rock', 'paper', 'scissors']

# Home view to display the form
def home(request):
    return render(request, 'home.html')

# Play view to handle the game logic
def play(request):
    user_choice = request.GET.get('choice')
    computer_choice = random.choice(choices)
    
    result = ''
    
    if user_choice == computer_choice:
        result = 'It\'s a tie!'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        result = 'You win!'
    else:
        result = 'You lose!'
    
    # Track the scores (optional)
    user_score = request.session.get('user_score', 0)
    computer_score = request.session.get('computer_score', 0)

    if result == 'You win!':
        user_score += 1
    elif result == 'You lose!':
        computer_score += 1

    # Update session scores
    request.session['user_score'] = user_score
    request.session['computer_score'] = computer_score

    return render(request, 'result.html', {
        'user_choice': user_choice,
        'computer_choice': computer_choice,
        'result': result,
        'user_score': user_score,
        'computer_score': computer_score,
    })
