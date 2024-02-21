import slow_validInput

def check_e2label_command():
    """
    Prompt the user to input a command related to e2label on a Red Hat system.
    Check if the command is correct.
    If correct, ask the user if they want to perform an action related to e2label.
    Provide hints if the user gives a wrong answer.
    """

    label = "testlabel"
    device = "/dev/sdb1"
    mount_point = "/mnt"
    correct_command = "e2label /dev/sdb1 testlabel"
    hint = "Hint: Use 'e2label' to perform actions related to filesystem labels."
    hint1 = f"Hint: Use 'echo 'LABEL={label} {mount_point} ext4 defaults 0 0' >> /etc/fstab' to copy the label to fstab."
    quit_command = ["quit", "q"]
    
    try:
        slow_validInput.print_slow("As you delve deeper into the realm of system administration, you find yourself in the heart of a Red Hat system.")
        slow_validInput.print_slow("Before you lies the command line interface, a gateway to the inner workings of the system.")
        slow_validInput.print_slow("You hear whispers of a powerful command: 'e2label', capable of manipulating filesystem labels.\n")
        slow_validInput.print_slow(f"Your quest begins with the discovery of the following \nLabel: {label}\nDevice : {device}\nMount point : {mount_point}\n")
        
        while True:
            user_input = input("Write the command to set a new label to a device with e2label or type 'quit/q' to exit: ").strip()
            print("\n")

            if user_input.strip() in quit_command:
                print("Exiting the task. Farewell!")
                return False

            if user_input.strip() == correct_command:
                print("Action performed with e2label successfully.")
                return True
            else:
                print("Command is incorrect. Try again.")
                print(hint)
                continue
    except KeyboardInterrupt:
        print("\nExiting the task due to user interruption (Ctrl+C). Farewell!")
        return False
    except Exception as e:
        print("An error occurred:", e)


def get_label():
    """
    Prompt the user to input a command to find the label associated with a disk or partition using e2label or tune2fs.
    """
    correct_commands = ["e2label /dev/sdb1", "tune2fs -l /dev/sdb1"]
    quit_command = ["quit", "q"]
    hint = "Hint: Use 'e2label /dev/sdb1'."

    try:
        slow_validInput.print_slow("As you embark on your journey to discover the secrets of storage, you encounter a gateway to the realm of disk labels.")
        slow_validInput.print_slow("Before you lies a puzzle: the key to unveil the label of a disk or partition.")
        slow_validInput.print_slow("You must choose your path wisely, using the commands 'e2label' or 'tune2fs' to unlock the mystery.\n")

        while True:
            user_command = input("Enter the command to find the label associated with a disk or partition using e2label or tune2fs or type 'quit/q' to exit: ").strip()
            print("\n")

            if user_command.strip() in quit_command:
                print("Exiting the task. Farewell!")
                return False

            if any(user_command.startswith(cmd) for cmd in correct_commands):
                print("Command is correct. You can continue.")
                # Placeholder label
                label = "<dummy_label>"
                print(f"The label associated with the device is: {label}")
                return True
            else:
                print("Command is incorrect. Try again.")
                print(hint)
                continue

    except KeyboardInterrupt:
        print("\nExiting the task due to user interruption (Ctrl+C). Farewell!")
        return False
    except Exception as e:
        print("An error occurred:", e)
        return False


def provide_label_line():
    """
    Prompt the user to provide a line with the label.
    Check if the provided line is correct.
    If correct, inform the user that the line is valid.
    If false, provide a hint and ask the user to try again.
    """
    correct_label = "testlabel"
    correct_line = f'LABEL={correct_label} /mnt ext4 defaults 0 0'
    hint = f"Hint: Use 'LABEL={correct_label} /mnt ext4 defaults 0 0' to provide the label line."
    quit_commands = ["quit", "q"]
    mount_point = "/mnt"

    try:
        slow_validInput.print_slow("\n\nAs you journey through the digital wilderness, you stumble upon a mysterious path."
                                   "This path, known only to the wise, leads to the heart of the filesystem, where labels reside."
                                   "As you approach, the whispers of the ancients guide your steps, revealing a hidden truth:"
                                   "Each label holds the key to a realm of data, waiting to be unlocked by those who dare to seek."
                                   "With courage in your heart, you take a step forward, ready to embrace the challenge.\n\n"
                                   f"Your quest begins with the discovery of the following Label:\n {correct_label}\n and the Mount point :\n {mount_point}\n")

        while True:
            user_line = input("Enter the line with the Label, (type 'quit' or 'q' to exit): ")
            print("\n")
            if user_line.strip() in quit_commands:
                print("Exiting the task. Farewell!")
                return False

            if user_line.strip() == correct_line:
                slow_validInput.print_slow("Line is correct. Label line provided successfully.")
                print("Example:")
                print("LABEL=testlabel /mnt ext4 defaults 0 0")
                return True
            else:
                slow_validInput.print_slow("Line is incorrect. Try again.")
                print(hint)
                print("Example: LABEL=testlabel /mnt ext4 defaults 0 0")
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
