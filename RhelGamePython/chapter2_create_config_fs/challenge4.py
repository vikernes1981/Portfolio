import slow_validInput
import create_fs
import inspect_fs
import repair_fs

def manage_filesystems():
    """
    Challenge: Manage Filesystems and Perform Repairs.
    """
    try:
        slow_validInput.print_slow("\n\nChallenge: Manage Filesystems and Perform Repairs\n\n")
        slow_validInput.print_slow("Welcome to the filesystem management challenge.")
        slow_validInput.print_slow("Explore the realm of filesystems and wield the power to create, inspect, and repair them.\n")
        slow_validInput.print_slow("You can quit at any time by typing 'quit' or 'q'.\n")

        count = 0
        valid_choices = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

        while True:
            if count == 8:
                break
            print("Options:")
            print("1. Create VFAT filesystem")
            print("2. Create EXT4 filesystem")
            print("3. Create XFS filesystem")
            print("4. Repair XFS filesystem")
            print("5. Repair EXT4 filesystem")
            print("6. Repair VFAT filesystem")
            print("7. Get XFS filesystem info")
            print("8. Inspect EXT4 filesystem")
            print("9. Continue to next challenge\n")

            choice = slow_validInput.get_valid_input("Enter your choice (1-9): ", valid_choices)

            if choice == '1':
                slow_validInput.print_slow("You create a VFAT filesystem, enabling compatibility and versatility.")
                if create_fs.vfat_create() == False:
                    continue
                slow_validInput.print_slow("VFAT filesystem created successfully!\n")
                count += 1
                continue

            elif choice == '2':
                slow_validInput.print_slow("You create an EXT4 filesystem, balancing performance and reliability.")
                if create_fs.ext4_create() == False:
                    continue
                slow_validInput.print_slow("EXT4 filesystem created successfully!\n")
                count += 1
                continue

            elif choice == '3':
                slow_validInput.print_slow("You create an XFS filesystem, embracing scalability and resilience.")
                if create_fs.xfs_create() == False:
                    continue
                slow_validInput.print_slow("XFS filesystem created successfully!\n")
                count += 1
                continue

            elif choice == '4':
                slow_validInput.print_slow("You repair a damaged XFS filesystem, restoring data integrity.")
                if repair_fs.repair_xfs_fs() == False:
                    continue
                slow_validInput.print_slow("XFS filesystem repaired successfully!\n")
                count += 1
                continue

            elif choice == '5':
                slow_validInput.print_slow("You repair a corrupted EXT4 filesystem, salvaging valuable data.")
                if repair_fs.repair_ext4() == False:
                    continue
                slow_validInput.print_slow("EXT4 filesystem repaired successfully!\n")
                count += 1
                continue

            elif choice == '6':
                slow_validInput.print_slow("You repair a damaged VFAT filesystem, bringing it back to life.")
                if repair_fs.repair_vfat() == False:
                    continue
                slow_validInput.print_slow("VFAT filesystem repaired successfully!\n")
                count += 1
                continue

            elif choice == '7':
                slow_validInput.print_slow("You retrieve information about an XFS filesystem, exploring its attributes and characteristics.")
                if inspect_fs.xfs_info_command() == False:
                    continue
                slow_validInput.print_slow("XFS filesystem information retrieved successfully!\n")
                count += 1
                continue

            elif choice == '8':
                slow_validInput.print_slow("You inspect the properties of an EXT4 filesystem, gaining insights into its structure and layout.")
                if inspect_fs.inspect_ext4() == False:
                    continue
                slow_validInput.print_slow("EXT4 filesystem inspection completed successfully!\n")
                count += 1
                continue

            elif choice == '9':
                break

    except KeyboardInterrupt:
        print("\nExiting the task due to user interruption (Ctrl+C). Farewell!")
    except Exception as e:
        print("An error occurred:", e)

