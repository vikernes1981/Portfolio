import slow_validInput

def xfs_info_command():
    """
    Function to display information about an XFS filesystem using xfs_info.
    """
    try:
        slow_validInput.print_slow("\n\nChallenge: XFS Filesystem Information\n\n")
        slow_validInput.print_slow("As you embark on this challenge, you find yourself in the realm of filesystem management.")
        slow_validInput.print_slow("The task before you is to gather information about an XFS filesystem using xfs_info.")
        slow_validInput.print_slow("Your journey continues with the invocation of sacred commands, exploring filesystem details.\n")
        slow_validInput.print_slow("Choose wisely, for the fate of this digital domain lies in your hands.\n")
        slow_validInput.print_slow("Remember to use 'quit' or 'q' to exit at any time.\n")

        while True:
            user_input = input("Type the command to display XFS filesystem information: ")

            if user_input.strip().lower() in ['quit', 'q']:
                slow_validInput.print_slow("Exiting the task. Farewell!")
                return False

            elif user_input.strip() == "xfs_info /dev/vg1/lv1":
                slow_validInput.print_slow("Displaying information about XFS filesystem on '/dev/vg1/lv1'...")
                slow_validInput.print_slow("\nExplanation:")
                slow_validInput.print_slow("- 'xfs_info': Command to display information about XFS filesystem.")
                slow_validInput.print_slow("- '/dev/vg1/lv1': Device representing the XFS filesystem.")
                slow_validInput.print_slow("\nThe 'xfs_info' command is used to retrieve detailed information about an XFS filesystem.")
                slow_validInput.print_slow("It provides various details such as filesystem size, block size, inode size, mount options, and more.")
                return True

            else:
                slow_validInput.print_slow("Incorrect command. Please try again or type 'quit' to exit.")
                slow_validInput.print_slow("Hint: Use command like 'xfs_info /dev/vg1/lv1'.")
                continue

    except KeyboardInterrupt:
        slow_validInput.print_slow("\nExiting the program due to user interruption (Ctrl+C). Goodbye!")
        return False
    except Exception as e:
        slow_validInput.print_slow("An error occurred:", e)
        return False


def inspect_ext4():
    """
    Function to inspect an ext4 filesystem using dumpe2fs.
    """
    try:
        slow_validInput.print_slow("\n\nChallenge: Inspect ext4 Filesystem\n\n")
        slow_validInput.print_slow("As you embark on this challenge, you find yourself in the realm of filesystem management.")
        slow_validInput.print_slow("The task before you is to inspect an ext4 filesystem using dumpe2fs.")
        slow_validInput.print_slow("Your journey continues with the invocation of sacred commands, gathering insights into filesystem details.\n")
        slow_validInput.print_slow("Choose wisely, for the fate of this digital domain lies in your hands.\n")
        slow_validInput.print_slow("Remember to use 'quit' or 'q' to exit at any time.\n")

        while True:
            user_input = input("Type the command to inspect the ext4 filesystem: ")

            if user_input.strip().lower() in ['quit', 'q']:
                slow_validInput.print_slow("Exiting the task. Farewell!")
                return False

            elif user_input.strip() == "dumpe2fs /dev/vg1/lv1":
                slow_validInput.print_slow("Inspecting ext4 filesystem on '/dev/vg1/lv1'...")
                slow_validInput.print_slow("\nExplanation:")
                slow_validInput.print_slow("- 'dumpe2fs': Command to inspect ext4 filesystem.")
                slow_validInput.print_slow("- '/dev/vg1/lv1': Device representing the ext4 filesystem to be inspected.")
                slow_validInput.print_slow("\nThe 'dumpe2fs' command is used to display detailed information about an ext4 filesystem.")
                slow_validInput.print_slow("It provides insights into the filesystem's superblock, block groups, inodes, features, and usage statistics.")
                return True

            else:
                slow_validInput.print_slow("Incorrect command. Please try again or type 'quit' to exit.")
                slow_validInput.print_slow("Hint: Use command like 'dumpe2fs /dev/vg1/lv1'.")
                continue

    except KeyboardInterrupt:
        slow_validInput.print_slow("\nExiting the program due to user interruption (Ctrl+C). Goodbye!")
        return False
    except Exception as e:
        slow_validInput.print_slow("An error occurred:", e)
        return False
