import random

while True:
	player = input("Choose: rock, paper, scissors: ")
	player_guess = player.lower()
	computer = ["rock", "paper", "scissors"]
	randomIndex = random.randint(0, len(computer) - 1)
	
	if (player_guess != "rock") and (player_guess != "paper") and (player_guess != "scissors"):
		print("Please choose a correct answer!")
		continue
	
	computer_guess = computer[randomIndex]
	
	if player_guess == computer_guess:
		print(f'Draw as player: {player_guess} <=> computer: {computer_guess}')
		continue
		
	elif player_guess == "rock":
		if computer_guess == "paper":
			print(f'Computer wins as player: {player_guess} <=> computer: {computer_guess}')
			break
		elif computer_guess == "scissors":
			print(f'Player wins as player: {player_guess} <=> computer: {computer_guess}')
			break
	
	elif player_guess == "paper":
		if computer_guess == "rock":
			print(f'Player wins as player: {player_guess} <=> computer: {computer_guess}')
			break
		elif computer_guess == "scissors":
			print(f'Computer wins as player: {player_guess} <=> computer: {computer_guess}')
			break
			
	elif player_guess == "scissors":
		if computer_guess == "paper":
			print(f'Player wins as player: {player_guess} <=> computer: {computer_guess}')
			break
		elif computer_guess == "rock":
			print(f'Computer wins as player: {player_guess} <=> computer: {computer_guess}')
			break
