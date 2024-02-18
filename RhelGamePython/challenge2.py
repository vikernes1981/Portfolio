import slow_validInput
import logical_volumes

def challenge_2():
    """
    Second challenge: Manipulate Logical Volumes.
    """
    try:
        slow_validInput.print_slow("Challenge 2: Manipulate Logical Volumes")
        slow_validInput.print_slow("As you journey deeper into the digital realm, the neon glow of the terminals fades, replaced by the faint hum of machinery.")
        slow_validInput.print_slow("You find yourself amidst a labyrinth of interconnected nodes, each pulsating with energy and potential.")
        slow_validInput.print_slow("Before you lies a nexus of data, a convergence point where logical volumes intertwine and diverge like threads of destiny.\n")
        slow_validInput.print_slow("To navigate this intricate web, you must master the manipulation of logical volumes, shaping them to your will and bending them to your command.\n")
        slow_validInput.print_slow("Choose your path wisely, for the fate of the digital realm hangs in the balance.\n")

        count = 0
        valid_choices = ['1', '2', '3', '4', '5', '6']

        while True:
            if count == 5:
                break
            
            # Add more options as needed
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
                logical_volumes.check_create_logical_volume_command()
                slow_validInput.print_slow("Logical volume created successfully!\n")
                count += 1
                continue
            elif choice == '2':
                slow_validInput.print_slow("With precision and care, you resize a logical volume, reshaping its boundaries to accommodate the ever-changing needs of the digital landscape.")
                logical_volumes.check_resize_logical_volume_command()
                slow_validInput.print_slow("Logical volume resized successfully!\n")
                count += 1
                continue
            elif choice == '3':
                slow_validInput.print_slow("With resolve in your heart, you remove a logical volume, untangling its threads from the tapestry of the digital universe.")
                logical_volumes.check_remove_logical_volume_command()
                slow_validInput.print_slow("Logical volume removed successfully!\n")
                count += 1
                continue
            elif choice == '4':
                slow_validInput.print_slow("With determination fueling your actions, you extend a logical volume, stretching its boundaries to encompass new horizons.")
                logical_volumes.check_extend_logical_volume_command()
                slow_validInput.print_slow("Logical volume extended successfully!\n")
                count += 1
                continue
            elif choice == '5':
                slow_validInput.print_slow("With curiosity guiding your hand, you peer into the depths of a logical volume, seeking knowledge and understanding.")
                logical_volumes.check_view_logical_volume_command()
                slow_validInput.print_slow("Logical volume viewed successfully!\n")
                count += 1
                continue
            elif choice == '6':
                break
    except Exception as e:
        print("An error occurred:", e)
