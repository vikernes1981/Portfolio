import slow_validInput
import system_admin

def manage_permissions():
    """
    Challenge: Manage Groups, Directories, Ownership, and systems.
    """
    try:
        slow_validInput.print_slow("\n\nChallenge: Manage Groups, Directories, Ownership, and systems\n\n")
        slow_validInput.print_slow("Welcome to the systems management challenge.")
        slow_validInput.print_slow("Explore the intricacies of user and group systems, and wield the power to modify directory attributes.\n")
        slow_validInput.print_slow("You can quit at any time by typing 'quit' or 'q'.\n")

        count = 0
        valid_choices = ['1', '2', '3', '4', '5', '6', '7']

        while True:
            if count == 6:
                break
            print("Options:")
            print("1. Add a group")
            print("2. Create a directory")
            print("3. Change ownership of a file or directory")
            print("4. Change permissions of a file or directory")
            print("5. Add a user to a group")
            print("6. Modify user details")
            print("7. Continue to next challenge\n")

            choice = slow_validInput.get_valid_input("Enter your choice (1-7): ", valid_choices)

            if choice == '1':
                slow_validInput.print_slow("You add a new group, expanding the realm of user collaboration.")
                if system_admin.add_group() == False:
                    continue
                slow_validInput.print_slow("Group added successfully!\n")
                count += 1
                continue

            elif choice == '2':
                slow_validInput.print_slow("You create a new directory, providing a structured environment for data organization.")
                if system_admin.create_directory() == False:
                    continue
                slow_validInput.print_slow("Directory created successfully!\n")
                count += 1
                continue

            elif choice == '3':
                slow_validInput.print_slow("You change the ownership of a file or directory, ensuring proper access control.")
                if system_admin.change_ownership() == False:
                    continue
                slow_validInput.print_slow("Ownership changed successfully!\n")
                count += 1
                continue

            elif choice == '4':
                slow_validInput.print_slow("You change the systems of a file or directory, fine-tuning access privileges.")
                if system_admin.change_permissions() == False:
                    continue
                slow_validInput.print_slow("permissions changed successfully!\n")
                count += 1
                continue

            elif choice == '5':
                slow_validInput.print_slow("You add a user to a group, fostering collaboration and teamwork.")
                if system_admin.add_user() == False:
                    continue
                slow_validInput.print_slow("User added to group successfully!\n")
                count += 1
                continue

            elif choice == '6':
                slow_validInput.print_slow("You modify user details, updating user information and preferences.")
                if system_admin.modify_user() == False:
                    continue
                slow_validInput.print_slow("User details modified successfully!\n")
                count += 1
                continue

            elif choice == '7':
                break

    except KeyboardInterrupt:
        print("\nExiting the task due to user interruption (Ctrl+C). Farewell!")
    except Exception as e:
        print("An error occurred:", e)


