import slow_validInput

def repair_xfs_fs():
    """
    Function to repair an XFS filesystem using xfs_repair.
    """
    try:
        slow_validInput.print_slow("\n\nChallenge: Repair XFS Filesystem\n\n")
        slow_validInput.print_slow("As you embark on this challenge, you find yourself in the realm of filesystem management.")
        slow_validInput.print_slow("The task before you is to repair an XFS filesystem using xfs_repair.")
        slow_validInput.print_slow("Your journey continues with the invocation of sacred commands, restoring filesystem consistency.\n")
        slow_validInput.print_slow("Choose wisely, for the fate of this digital domain lies in your hands.\n")
        slow_validInput.print_slow("Remember to use 'quit' or 'q' to exit at any time.\n")

        while True:
            user_input = input("Type the command to repair the XFS filesystem: ")

            if user_input.strip().lower() in ['quit', 'q']:
                slow_validInput.print_slow("Exiting the task. Farewell!")
                return False

            elif user_input.strip() == "xfs_repair /dev/vg1/lv1":
                slow_validInput.print_slow("Repairing XFS filesystem on '/dev/vg1/lv1'...")
                slow_validInput.print_slow("\nExplanation:")
                slow_validInput.print_slow("- 'xfs_repair': Command to repair XFS filesystem.")
                slow_validInput.print_slow("- '/dev/vg1/lv1': Device representing the XFS filesystem to be repaired.")
                slow_validInput.print_slow("\nThe 'xfs_repair' command is used to repair inconsistencies in an XFS filesystem.")
                slow_validInput.print_slow("It scans the filesystem for errors and attempts to fix them to restore filesystem consistency.")
                slow_validInput.print_slow("\nNote: It's recommended to run xfs_repair on an unmounted filesystem to avoid data corruption.")
                slow_validInput.print_slow("Make sure to unmount the filesystem before proceeding with the repair.")
                return True

            else:
                slow_validInput.print_slow("Incorrect command. Please try again or type 'quit' to exit.")
                slow_validInput.print_slow("Hint: Use command like 'xfs_repair /dev/vg1/lv1'.")
                continue

    except KeyboardInterrupt:
        slow_validInput.print_slow("\nExiting the program due to user interruption (Ctrl+C). Goodbye!")
        return False
    except Exception as e:
        slow_validInput.print_slow("An error occurred:", e)
        return False


def repair_ext4():
    """
    Function to repair an unmounted ext4 filesystem consistency.
    """
    try:
        slow_validInput.print_slow("\n\nChallenge: Repair ext4 Filesystem Consistency\n\n")
        slow_validInput.print_slow("As you embark on this challenge, you find yourself in the realm of filesystem management.")
        slow_validInput.print_slow("The task before you is to repair an unmounted ext4 filesystem consistency.")
        slow_validInput.print_slow("Your journey continues with the invocation of sacred commands, ensuring filesystem integrity with expertise.\n")
        slow_validInput.print_slow("Choose wisely, for the fate of this digital domain lies in your hands.\n")
        slow_validInput.print_slow("Remember to use 'quit' or 'q' to exit at any time.\n")

        while True:
            user_input = input("Type the command to repair ext4 filesystem consistency: ")

            if user_input.strip().lower() in ['quit', 'q']:
                slow_validInput.print_slow("Exiting the task. Farewell!")
                return False

            elif user_input.strip() == "fsck.ext4 /dev/vg1/lv1":
                slow_validInput.print_slow("Repairing ext4 filesystem consistency on '/dev/vg1/lv1'...")
                slow_validInput.print_slow("\nExplanation:")
                slow_validInput.print_slow("- 'fsck.ext4': Command to repair an ext4 filesystem.")
                slow_validInput.print_slow("- '/dev/vg1/lv1': Device representing the ext4 filesystem to be repaired.")
                slow_validInput.print_slow("\nThe 'fsck.ext4' command is used to check and repair an ext4 filesystem consistency.")
                slow_validInput.print_slow("It is important to ensure filesystem integrity for data reliability.")
                return True

            else:
                slow_validInput.print_slow("Incorrect command. Please try again or type 'quit' to exit.")
                slow_validInput.print_slow("Hint: Use command like 'fsck.ext4 /dev/vg1/lv1'.")
                continue

    except KeyboardInterrupt:
        slow_validInput.print_slow("\nExiting the program due to user interruption (Ctrl+C). Goodbye!")
        return False
    except Exception as e:
        slow_validInput.print_slow("An error occurred:", e)
        return False


def repair_vfat():
    """
    Function to repair an unmounted FAT filesystem consistency.
    """
    try:
        slow_validInput.print_slow("\n\nChallenge: Repair FAT Filesystem Consistency\n\n")
        slow_validInput.print_slow("As you embark on this challenge, you find yourself in the realm of filesystem management.")
        slow_validInput.print_slow("The task before you is to repair an unmounted FAT filesystem consistency.")
        slow_validInput.print_slow("Your journey continues with the invocation of sacred commands, ensuring filesystem integrity with expertise.\n")
        slow_validInput.print_slow("Choose wisely, for the fate of this digital domain lies in your hands.\n")
        slow_validInput.print_slow("Remember to use 'quit' or 'q' to exit at any time.\n")

        while True:
            user_input = input("Type the command to repair FAT filesystem consistency: ")

            if user_input.strip().lower() in ['quit', 'q']:
                slow_validInput.print_slow("Exiting the task. Farewell!")
                return False

            elif user_input.strip() == "fsck.vfat /dev/vg1/lv1":
                slow_validInput.print_slow("Repairing FAT filesystem consistency on '/dev/vg1/lv1'...")
                slow_validInput.print_slow("\nExplanation:")
                slow_validInput.print_slow("- 'fsck.vfat': Command to repair a FAT filesystem.")
                slow_validInput.print_slow("- '/dev/vg1/lv1': Device representing the FAT filesystem to be repaired.")
                slow_validInput.print_slow("\nThe 'fsck.vfat' command is used to check and repair a FAT filesystem consistency.")
                slow_validInput.print_slow("It is important to ensure filesystem integrity for data reliability.")
                return True

            else:
                slow_validInput.print_slow("Incorrect command. Please try again or type 'quit' to exit.")
                slow_validInput.print_slow("Hint: Use command like 'fsck.vfat /dev/vg1/lv1'.")
                continue

    except KeyboardInterrupt:
        slow_validInput.print_slow("\nExiting the program due to user interruption (Ctrl+C). Goodbye!")
        return False
    except Exception as e:
        slow_validInput.print_slow("An error occurred:", e)
        return False
