import slow_validInput

def expand_vdo():
    """
    Function to expand a VDO (Virtual Data Optimizer) volume.
    """
    try:
        slow_validInput.print_slow("As you journey deeper into the realm of data optimization, you encounter a VDO volume,")
        slow_validInput.print_slow("its digital essence pulsating with the promise of untapped potential.")
        slow_validInput.print_slow("To unleash its full power, you must expand its boundaries,")
        slow_validInput.print_slow("allowing it to absorb new data and grow in strength.\n")
        slow_validInput.print_slow("Remember, you can exit at any time by typing 'quit' or 'q'.\n")

        while True:
            user_input = input("Type the command to expand a VDO volume: ")

            if user_input.strip().lower() in ['quit', 'q']:
                slow_validInput.print_slow("Exiting the task. Farewell!")
                return False

            if user_input.strip() == "vdo growfs /dev/mapper/vdo1":
                slow_validInput.print_slow("VDO volume expanded successfully!")
                slow_validInput.print_slow("\nAdditional Information:")
                slow_validInput.print_slow("The 'vdo growfs' command expands the filesystem of a VDO volume")
                slow_validInput.print_slow("to utilize the entire logical size previously set during its creation.")
                slow_validInput.print_slow("This operation dynamically adjusts the filesystem to utilize all available space.")
                return True
            else:
                slow_validInput.print_slow("Incorrect command. Please try again or type 'quit' to exit.")
                slow_validInput.print_slow("Hint: Use 'vdo growfs /dev/mapper/vdo1'")
                continue
    except KeyboardInterrupt:
        slow_validInput.print_slow("\nExiting the program due to user interruption (Ctrl+C). Goodbye!")
        return False
    except Exception as e:
        slow_validInput.print_slow("An error occurred:", e)
        return False
