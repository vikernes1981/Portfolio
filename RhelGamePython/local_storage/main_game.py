import intro
import challenge1
import challenge2
import challenge3
import challenge4
import challenge5
import challenge6
import challenge7
import outro



def main():
    """
    Main function to run the game.
    """
    try:
        intro.start_game()
        challenge1.challenge_1()
        challenge2.challenge_2()
        challenge3.challenge_3()
        challenge4.challenge_4()
        challenge5.challenge_5()
        challenge6.challenge_6()
        challenge7.challenge_7()
        outro.conclusion()  # Display the conclusion after completing all challenges.
    except Exception as e:
        print("An error occurred during the game:", e)

if __name__ == "__main__":
    main()
