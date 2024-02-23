import slow_validInput
import fstab_vdo_stratis
import vdo_admin
from create_fs import create_vdo


def configure_vdo():
    """
    Challenge: Configure VDO (Virtual Data Optimizer).
    """
    try:
        slow_validInput.print_slow("\n\nChallenge: Configure VDO (Virtual Data Optimizer)\n\n")
        slow_validInput.print_slow("As you traverse the virtual landscape, neon lights flicker, casting an ethereal glow over your surroundings.")
        slow_validInput.print_slow("Your journey leads you to a desolate outpost, a relic of a bygone era, where a solitary terminal awaits.")
        slow_validInput.print_slow("Approaching cautiously, you activate the terminal, and its ancient screen flickers to life, revealing a cryptic message:")
        slow_validInput.print_slow("'To proceed, you must shape the very essence of this digital world by configuring its local storage.'\n")
        slow_validInput.print_slow("Before you stretch arrays of data, their digital pulses echoing like the heartbeat of the cyber realm.")
        slow_validInput.print_slow("Your mission is clear: navigate the labyrinth of disks and partitions, harness the power of UUIDs, and ensure the integrity of the digital landscape.\n")
        slow_validInput.print_slow("Choose wisely, for the fate of this digital domain lies in your hands.\n")
        slow_validInput.print_slow("You can quit at any time by typing 'quit' or 'q'.\n")

        count = 0
        valid_choices = ['1', '2', '3', '4', '5', '6', '7', '8']

        while True:
            if count == 7:
                break
            print("Options:")
            print("1. Install VDO")
            print("2. VDO Create")
            print("3. Expand VDO volume")
            print("4. Remove VDO volume")
            print("5. List VDO volumes")
            print("6. Add VDO volume to /etc/fstab")
            print("7. VDO write modes info")
            print("8. Continue to next challenge\n")

            choice = slow_validInput.get_valid_input("Enter your choice (1-8): ", valid_choices)

            if choice == '1':
                slow_validInput.print_slow("With unwavering resolve, you install VDO, optimizing the digital landscape for maximum efficiency.")
                if vdo_admin.install_vdo() == False:
                    continue
                slow_validInput.print_slow("VDO installed successfully!\n")
                count += 1
                continue

            elif choice == '2':
                slow_validInput.print_slow("You choose to create a new VDO volume, shaping the digital landscape with efficiency and precision.")
                 
                if create_vdo() == False:
                    continue
                slow_validInput.print_slow("VDO volume created successfully!\n")
                count += 1
                continue

            elif choice == '3':
                slow_validInput.print_slow("You choose to expand the existing VDO volume, unlocking additional storage capacity.")

                if vdo_admin.expand_vdo() == False:
                    continue
                slow_validInput.print_slow("VDO volume expanded successfully!\n")
                count += 1
                continue

            elif choice == '4':
                slow_validInput.print_slow("With careful consideration, you opt to remove the VDO volume, restoring the digital landscape to its original state.")
                
                if vdo_admin.remove_vdo() == False:
                    continue
                slow_validInput.print_slow("VDO volume removed successfully!\n")
                count += 1
                continue

            elif choice == '5':
                slow_validInput.print_slow("You decide to list all VDO volumes, gaining insight into their configurations and capacities.")
                
                if vdo_admin.list_vdo() == False:
                    continue
                slow_validInput.print_slow("VDO volumes listed successfully!\n")
                count += 1
                continue

            elif choice == '6':
                slow_validInput.print_slow("You choose to add the VDO volume to /etc/fstab, ensuring it is mounted automatically on boot.")
                if fstab_vdo.add_vdo_fstab() == False:
                    continue
                slow_validInput.print_slow("VDO volume added to /etc/fstab successfully!\n")
                count += 1
                continue

            elif choice == '7':
                slow_validInput.print_slow("You seek information about VDO write modes, exploring the various options available.")
                if vdo_admin.vdo_write_modes() == False:
                    continue
                slow_validInput.print_slow("VDO write modes info displayed successfully!\n")
                count += 1
                continue

            elif choice == '8':
                break
    except KeyboardInterrupt:
        print("\nExiting the task due to user interruption (Ctrl+C). Farewell!")
    except Exception as e:
        print("An error occurred:", e)


