import random
import blackjack_art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def calculate_score(cards_list):
    score = sum(cards_list)
    while score > 21 and 11 in cards_list:
        cards_list.remove(11)
        cards_list.append(1)
        score = sum(cards_list)
    return score

def deal_card(player_cards):
    player_cards.append(random.choice(cards))
    return calculate_score(player_cards)

play = input("Do you want to play a game of Blackjack? Type 'y' for yes or 'n' for no: ")

while play == "y":
    print("\n" * 10)

    my_cards = [random.choice(cards), random.choice(cards)]
    computer_cards = [random.choice(cards), random.choice(cards)]
    my_cards_sum = calculate_score(my_cards)
    computer_cards_sum = calculate_score(computer_cards)

    print(blackjack_art.logo)
    print(f"Your cards:{my_cards}, current score: {my_cards_sum}")
    print(f"Computer's first card: {computer_cards[0]}")

    if my_cards_sum == 21 and len(my_cards) == 2:
        print("You have a Blackjack! 🎉")
        if computer_cards_sum == 21:
            print("Computer also has Blackjack. It's a draw! 🙃")
        else:
            print("You win! 😃")
    elif computer_cards_sum == 21 and len(computer_cards) == 2:
        print("Computer has a Blackjack! You lose 😭")
    else:
        game_over = False
        while not game_over:
            if my_cards_sum > 21:
                print("You went over. You lose 😭")
                game_over = True
            else:
                more_cards = input("Type 'y' to get another card, type 'n' to pass: ")
                if more_cards == 'y':
                    my_cards_sum = deal_card(my_cards)
                    print(f"Your cards: {my_cards}, current score: {my_cards_sum}")
                    print(f"Computer's first card: {computer_cards[0]}")
                else:
                    game_over = True

        if my_cards_sum <= 21:
            print(f"Computer's cards: {computer_cards}, current score: {computer_cards_sum}")

            while computer_cards_sum < 17:
                computer_cards_sum = deal_card(computer_cards)
                print(f"Computer draws: {computer_cards}, current score: {computer_cards_sum}")

            if computer_cards_sum > 21:
                print("Computer went over. You win 😁")
            elif my_cards_sum > computer_cards_sum:
                print("You win 😃")
            elif my_cards_sum < computer_cards_sum:
                print("You lose 😤")
            else:
                print("Draw 🙃")

    play = input("Do you want to play again? Type 'y' for yes or 'n' for no: ")