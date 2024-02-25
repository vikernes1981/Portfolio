import slow_validInput
import logical_volumes

def challenge_2():
    """
    Second challenge: Manipulate Logical Volumes.
    """
    try:
        slow_validInput.print_slow("\n\nChallenge 2: Manipulate Logical Volumes\n\n")
        slow_validInput.print_slow("But optimizing disk space requires more than just creating filesystems.")
        slow_validInput.print_slow("You recognize the importance of efficient storage management.")
        slow_validInput.print_slow("Drawing upon your expertise, you decide to create logical volumes to dynamically allocate storage space.\n")
        slow_validInput.print_slow("You issue commands to create logical volumes, carefully specifying the size and characteristics of each volume.")
        slow_validInput.print_slow("As the commands execute, you monitor the progress, ensuring that each logical volume is configured according to the system's requirements.\n")
        slow_validInput.print_slow("With each logical volume created, you feel a sense of accomplishment, knowing that you're enhancing the system's storage capabilities.")
        slow_validInput.print_slow("You meticulously review the attributes of each volume, ensuring that they align with the system's requirements and your intended use cases.")
        slow_validInput.print_slow("As the logical volumes take shape, you envision the flexibility they will provide in managing data.")
        slow_validInput.print_slow("From the root filesystem to dedicated spaces for user home directories and system swap, each volume serves a vital role in maintaining system performance.")
        slow_validInput.print_slow("With the finalization of the logical volumes, you stand back, surveying your handiwork with pride.")
        slow_validInput.print_slow("The system now possesses the flexibility and scalability needed to handle the challenges of modern computing environments.")
        slow_validInput.print_slow("With this task completed, you're one step closer to fulfilling your mission and becoming a true master of Red Hat administration.\n")
        count = 0
        valid_choices = ['1', '2', '3', '4', '5', '6']

        while True:
            if count == 5:
                break
            
            print("Options:")
            print("1. Create Logical Volume")
            print("2. Resize Logical Volume")
            print("3. Remove Logical Volume")
            print("4. Extend Logical Volume")
            print("5. View Logical Volume")
            print("6. Continue to next challenge\n")

            choice = slow_validInput.get_valid_input("Enter your choice (1-6): ", valid_choices)

            if choice == '1':
                slow_validInput.print_slow("With a deft hand, you weave the fabric of the digital realm, crafting a new logical volume from the raw essence of data.")
                if logical_volumes.check_create_logical_volume_command() == False:
                    continue
                slow_validInput.print_slow("Logical volume created successfully!\n")
                count += 1
                continue
            elif choice == '2':
                slow_validInput.print_slow("With precision and care, you resize a logical volume, reshaping its boundaries to accommodate the ever-changing needs of the digital landscape.")
                if logical_volumes.check_resize_logical_volume_command() == False:
                    continue
                slow_validInput.print_slow("Logical volume resized successfully!\n")
                count += 1
                continue
            elif choice == '3':
                slow_validInput.print_slow("With resolve in your heart, you remove a logical volume, untangling its threads from the tapestry of the digital universe.")
                if logical_volumes.check_remove_logical_volume_command() == False:
                    continue
                slow_validInput.print_slow("Logical volume removed successfully!\n")
                count += 1
                continue
            elif choice == '4':
                slow_validInput.print_slow("With determination fueling your actions, you extend a logical volume, stretching its boundaries to encompass new horizons.")
                if logical_volumes.check_extend_logical_volume_command() == False:
                    continue
                slow_validInput.print_slow("Logical volume extended successfully!\n")
                count += 1
                continue
            elif choice == '5':
                slow_validInput.print_slow("With curiosity guiding your hand, you peer into the depths of a logical volume, seeking knowledge and understanding.")
                if logical_volumes.check_view_logical_volume_command() == False:
                    continue
                slow_validInput.print_slow("Logical volume viewed successfully!\n")
                count += 1
                continue
            elif choice == '6':
                slow_validInput.print_slow("With the finalization of the logical volumes, you stand back, surveying your handiwork with pride.")
                slow_validInput.print_slow("The system now possesses the flexibility and scalability needed to handle the challenges of modern computing environments.")
                slow_validInput.print_slow("With this task completed, you're one step closer to fulfilling your mission and becoming a true master of Red Hat administration.\n")
                break
    except KeyboardInterrupt:
        print("\nExiting the program due to user interruption (Ctrl+C). Goodbye!")
    except Exception as e:
        print("An error occurred:", e)
