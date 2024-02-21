import slow_validInput
import volume_groups

def challenge_3():
    """
    Third challenge: Conquer Volume Groups.
    """
    try:
        slow_validInput.print_slow("\n\nChallenge 3: Conquer Volume Groups\n\n")
        slow_validInput.print_slow("You advance further into the heart of the digital realm, where the echoes of ancient systems reverberate through the corridors.")
        slow_validInput.print_slow("Before you stands the Citadel of Volume Groups, a towering fortress of data surrounded by an aura of mystique.")
        slow_validInput.print_slow("To claim victory, you must breach the walls of this formidable fortress and conquer the volume groups that lie within.")
        slow_validInput.print_slow("With each step, the weight of responsibility grows heavier upon your shoulders, for the fate of the digital realm hangs in the balance.")
        slow_validInput.print_slow("Choose your actions wisely, for the path to triumph is fraught with peril and uncertainty.\n")
    
        count = 0
        valid_choices = ['1', '2', '3', '4', '5', '6']

        while True:
            if count == 5:
                break
            
            print("Options:")
            print("1. Create Volume Group")
            print("2. Extend Volume Group")
            print("3. Remove Volume Group")
            print("4. View Volume Group")
            print("5. Remove a physical volume from an existing volume group")
            print("6. Continue to next challenge\n")

            choice = slow_validInput.get_valid_input("Enter your choice (1-6): ", valid_choices)

            if choice == '1':
                slow_validInput.print_slow("With determination in your heart, you lay the foundation for a new volume group, a beacon of order amidst the chaos of the digital realm.")
                if volume_groups.check_create_volume_group_command() == False:
                    continue
                slow_validInput.print_slow("Volume group created successfully!\n")
                count += 1
                continue
            elif choice == '2':
                slow_validInput.print_slow("With unwavering resolve, you extend the boundaries of a volume group, expanding its reach to encompass new territories.")
                if volume_groups.check_extend_volume_group_command() == False:
                    continue
                slow_validInput.print_slow("Volume group extended successfully!\n")
                count += 1
                continue
            elif choice == '3':
                slow_validInput.print_slow("With courage guiding your hand, you dismantle a volume group, unravelling its structure to reveal the core of its existence.")
                if volume_groups.check_remove_volume_group_command() == False:
                    continue
                slow_validInput.print_slow("Volume group removed successfully!\n")
                count += 1
                continue
            elif choice == '4':
                slow_validInput.print_slow("With keen insight, you peer into the heart of a volume group, discerning its secrets and unlocking its potential.")
                if volume_groups.check_view_volume_groups_command() == False:
                    continue
                slow_validInput.print_slow("Volume group viewed successfully!\n")
                count += 1
                continue
            elif choice == '5':
                slow_validInput.print_slow("With precision and care, you remove a physical volume from an existing volume group, reshaping its structure to suit your needs.")
                if volume_groups.check_remove_physical_volume_command() == False:
                    continue
                slow_validInput.print_slow("Physical volume removed successfully from the existing volume group!\n")
                count += 1
                continue
            elif choice == '6':
                break
    except KeyboardInterrupt:
        print("\nExiting the program due to user interruption (Ctrl+C). Goodbye!")
    except Exception as e:
        print("An error occurred:", e)
