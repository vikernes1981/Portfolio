import slow_validInput

def start_game():
    """
    Start the Red Hat Odyssey game.
    """
    try:
        slow_validInput.print_slow("Welcome to the Red Hat Odyssey!\n")
        slow_validInput.print_slow("In the year 2150, humanity made a quantum leap into the digital age, transcending the boundaries of the physical world.")
        slow_validInput.print_slow("As the world's reliance on technology grew, so did the need for skilled administrators to navigate the complexities of the digital realm.")
        slow_validInput.print_slow("You, a seasoned cybernaut, have honed your skills in the art of Red Hat administration, mastering the intricacies of Linux systems.")
        slow_validInput.print_slow("Today, you embark on a journey that will test your knowledge, courage, and resilience like never before.")
        slow_validInput.print_slow("Welcome to the Red Hat Odyssey, where legends are born and destinies are forged amidst the endless expanse of cyberspace.\n")
        slow_validInput.print_slow("As you step into the virtual realm, you are greeted by the luminous glow of neon terminals and the hum of servers.")
        slow_validInput.print_slow("A message materializes before you, beckoning you to unlock the secrets of the digital universe:")
        slow_validInput.print_slow("‘Welcome, adventurer. Your mission, should you choose to accept it, is to conquer the challenges that lie ahead")
        slow_validInput.print_slow("and emerge as the ultimate master of Red Hat administration. But beware, for the path ahead is fraught with peril and uncertainty.")
        slow_validInput.print_slow("Only by harnessing your skills and intellect can you hope to prevail in the face of adversity.'\n")
        input("Press Enter to embark on your journey...")
    except KeyboardInterrupt:
        print("\nGame interrupted. Exiting...")
        exit()