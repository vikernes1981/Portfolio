import slow_validInput
import stratis_config
import fstab_vdo_stratis
from create_fs import manage_and_create_stratis_pool_fs

def configure_stratis():
    """
    Challenge: Configure Stratis Storage Management.
    """
    try:
        slow_validInput.print_slow("\n\nChallenge: Configure Stratis Storage Management\n\n")
        slow_validInput.print_slow("Welcome to the Stratis configuration challenge.")
        slow_validInput.print_slow("Your mission is to master the art of Stratis storage management.")
        slow_validInput.print_slow("Navigate the digital landscape, wield the power of Stratis, and shape the future of storage.\n")
        slow_validInput.print_slow("You can quit at any time by typing 'quit' or 'q'.\n")

        count = 0
        valid_choices = ['1', '2', '3', '4', '5']

        while True:
            if count == 7:
                break
            print("Options:")
            print("1. Install Stratis Packages")
            print("2. Administrate a Stratis Pool and Filesystem")
            print("3. Create a Snapshot of the Stratis Filesystem")
            print("4. Add Stratis volume in /etc/fstab")
            print("5. Continue to next challenge\n")

            choice = slow_validInput.get_valid_input("Enter your choice (1-8): ", valid_choices)

            if choice == '1':
                slow_validInput.print_slow("You embark on your journey by installing Stratis packages, laying the foundation for advanced storage management.")
                if stratis_config.install_stratis() == False:
                    continue
                slow_validInput.print_slow("Stratis packages installed successfully!\n")
                count += 1
                continue

            elif choice == '2':
                slow_validInput.print_slow("You choose to administrate a Stratis pool, a reservoir of digital potential, ready to store and protect your data.")
                if manage_and_create_stratis_pool_fs() == False:
                    continue
                slow_validInput.print_slow("Stratis pool created and destroyed successfully!\n")
                count += 1
                continue

            elif choice == '3':
                slow_validInput.print_slow("You capture a moment in time by creating a snapshot of your Stratis filesystem, preserving its state for future reference.")
                if stratis_config.create_stratis_snapshot() == False:
                    continue
                slow_validInput.print_slow("Snapshot of Stratis filesystem created successfully!\n")
                count += 1
                continue
            elif choice == '4':
                slow_validInput.print_slow("You choose to add the Stratis volume to /etc/fstab, ensuring it is mounted automatically on boot.")
                if fstab_vdo_stratis.add_stratis_fstab() == False:
                    continue
                slow_validInput.print_slow("Stratis volume added to /etc/fstab successfully!\n")
                count += 1
                continue
            elif choice == '5':
                break

    except KeyboardInterrupt:
        print("\nExiting the task due to user interruption (Ctrl+C). Farewell!")
    except Exception as e:
        print("An error occurred:", e)

