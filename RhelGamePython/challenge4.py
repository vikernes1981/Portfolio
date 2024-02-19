import slow_validInput
import physical_volumes

def challenge_4():
    """
    Fourth challenge: Uncover Disk Secrets.
    """
    try:
        slow_validInput.print_slow("\n\nChallenge 4: Uncover Disk Secrets\n\n")
        slow_validInput.print_slow("As you delve deeper into the digital labyrinth, the air grows heavy with the scent of rust and machinery.")
        slow_validInput.print_slow("You find yourself standing before a series of hidden chambers, their entrances concealed by the passage of time.")
        slow_validInput.print_slow("In these forgotten alcoves, the mysteries of disk management await your discovery, hidden beneath layers of code and data.")
        slow_validInput.print_slow("With each step, you can feel the weight of history pressing down upon you, urging you forward into the unknown.")
        slow_validInput.print_slow("Choose your actions wisely, for the secrets you uncover may hold the key to the salvation or downfall of the digital realm.\n")
    
        count = 0
        valid_choices = ['1', '2', '3', '4']

        while True:
            if count == 3:
                break
            
            # Add more options as needed
            print("Options:")
            print("1. View Physical Volumes")
            print("2. Create Physical Volume")
            print("3. Remove Physical Volume")
            print("4. Continue to next challenge\n")

            choice = slow_validInput.get_valid_input("Enter your choice (1-4): ", valid_choices)
            if choice == '1':
                slow_validInput.print_slow("With a sense of anticipation, you peer into the darkness of the hidden chambers, revealing the physical volumes that lie within.")
                if physical_volumes.view_physical_volumes() == False:
                    continue
                slow_validInput.print_slow("Physical volumes viewed successfully!")
                count += 1
                continue
            elif choice == '2':
                slow_validInput.print_slow("With determination in your heart, you forge a new path forward, creating a physical volume from the raw materials of the digital realm.")
                if physical_volumes.create_physical_volume() == False:
                    continue
                slow_validInput.print_slow("Physical volume created successfully!")
                count += 1
                continue
            elif choice == '3':
                slow_validInput.print_slow("With resolve guiding your hand, you remove a physical volume, untangling its threads from the fabric of the digital universe.")
                if physical_volumes.remove_physical_volume() == False:
                    continue
                slow_validInput.print_slow("Physical volume removed successfully!")
                count += 1
                continue
            elif choice == '4':
                break
    except Exception as e:
        print("An error occurred:", e)
