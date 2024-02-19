### MOUNT WITH UUID ###

import slow_validInput

def provide_uuid_line():
    """
    Prompt the user to provide a line with the UUID.
    Check if the provided line is correct.
    If correct, inform the user that the line is valid.
    If false, provide a hint and ask the user to try again.
    """
    correct_uuid = "966cd40a-0aab-464b-b930-7909fefea8db"
    correct_line = f'UUID={correct_uuid} /mnt ext4 defaults 0 0'
    hint = f"Hint: Use 'UUID={correct_uuid} /mnt ext4 defaults 0 0' to provide the UUID line."
    quit_commands = ["quit", "q"]
    mount_point = "/mnt"

    try:
        slow_validInput.print_slow("\n\nAs you journey through the digital wilderness, you stumble upon a mysterious path."
                                   "This path, known only to the wise, leads to the heart of the filesystem, where UUIDs reside."
                                   "As you approach, the whispers of the ancients guide your steps, revealing a hidden truth:"
                                   "Each UUID holds the key to a realm of data, waiting to be unlocked by those who dare to seek."
                                   "With courage in your heart, you take a step forward, ready to embrace the challenge.\n\n"
                                   f"Your quest begins with the discovery of the following UUID:\n {correct_uuid}\n and the Mount point :\n {mount_point}\n")

        while True:
            user_line = input("Enter the line with the UUID,(type 'quit' or 'q' to exit): ")
            print("\n")
            if user_line.strip() in quit_commands:
                print("Exiting the task. Farewell!")
                return False

            if user_line.strip() == correct_line:
                slow_validInput.print_slow("Line is correct. UUID line provided successfully.")
                print("Example:")
                print("UUID=966cd40a-0aab-464b-b930-7909fefea8db /mnt ext4 defaults 0 0")
                return True
            else:
                slow_validInput.print_slow("Line is incorrect. Try again.")
                print(hint)
                print("Example: UUID=966cd40a-0aab-464b-b930-7909fefea8db /mnt ext4 defaults 0 0")
                print("Options: Additional options can be specified in the /etc/fstab file for mounting.")
                print("Options: 'defaults' typically includes options for read/write access and other standard settings.")
                print("         '0 0' specifies filesystem check and order of dumping.")
                continue
    except KeyboardInterrupt:
        print("\nExiting the program due to user interruption (Ctrl+C). Farewell!")
        return False
    except Exception as e:
        print("An error occurred:", e)
        return False








# NA TO FTIAKSW ,TELEIWS LATHOSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS







def edit_fstab():
    """
    Prompt the user to edit the fstab file.
    """
    hint = "Hint: The fstab file is typically located in the /etc directory."
    quit_commands = ["quit", "q"]

    try:
        while True:
            edit_command = input("Navigate to fstab file or edit it directly using vim (type 'quit' or 'q' to exit): ")

            if edit_command.strip() in quit_commands:
                print("Exiting the program. Goodbye!")
                return False

            if "cd /etc/" in edit_command:
                print("Correct! Now you're in the directory containing the fstab file.")
                vim_command = input("How would you edit the fstab file using vim? ")
                if "vim" in vim_command and "fstab" in vim_command:
                    print("Correct! You're now editing the fstab file.")
                    break
                else:
                    print("Incorrect. Try again with 'vim fstab' or 'vim /etc/fstab'.")
            elif "vim" in edit_command and ("fstab" in edit_command or "/etc/fstab" in edit_command):
                print("Correct! You're now editing the fstab file.")
                break
            else:
                print("Incorrect. " + hint)
    except KeyboardInterrupt:
        print("\nExiting the program due to user interruption (Ctrl+C). Goodbye!")
        return False
    except Exception as e:
        print("An error occurred:", e)
        return False


def mount_partition():
    """
    Prompt the user to mount a partition.
    """
    hint = "Hint: Use the 'mount' command to mount a partition. You can specify the mount point with '/mnt'. To mount all filesystems specified in fstab, use 'mount -a'."
    quit_command = ["quit", "q"]

    try:
        slow_validInput.print_slow("\n\nAs you stand at the threshold of system integration, a pivotal moment awaits - the mounting of partitions."
                                   "With each mount, disparate realms converge, ushering forth a unified system."
                                   "The command 'mount' serves as your beacon in this journey, guiding you to new horizons.\n")
        
        while True:
            mount_command = input("How would you mount a partition? ")

            if mount_command.strip() in quit_command:
                slow_validInput.print_slow("Exiting the task. Farewell!")
                return False

            if mount_command.strip() in ["mount /mnt", "mount -a"]:
                slow_validInput.print_slow("Correct! The partition has been mounted.")
                break
            else:
                slow_validInput.print_slow("Incorrect. " + hint)

        # Additional examples and options
        slow_validInput.print_slow("\nAdditional examples and options:")
        slow_validInput.print_slow("- 'mount /dev/sdb1 /mnt': Mounts the partition /dev/sdb1 to the /mnt directory.")
        slow_validInput.print_slow("- 'mount -o remount /mnt': Remounts the /mnt directory with the options specified in /etc/fstab.")
        slow_validInput.print_slow("- 'mount -t ext4 /dev/sdc1 /data': Mounts the partition /dev/sdc1 to the /data directory with the ext4 filesystem type.")

    except KeyboardInterrupt:
        print("\nExiting the program due to user interruption (Ctrl+C). Farewell!")
        return False
    except Exception as e:
        print("An error occurred:", e)
        return False