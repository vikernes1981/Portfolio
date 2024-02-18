### MOUNT WITH LABEL###


import slow_validInput

def check_e2label_tune2fs_command():
    """
    Prompt the user to input a command related to e2label and tune2fs on a Red Hat system.
    Check if the command is correct.
    If correct, ask the user if they want to perform an action related to e2label or tune2fs.
    Provide hints if the user gives a wrong answer.
    """
    correct_commands = ["e2label", "tune2fs"]
    hint = "Hint: Use 'e2label' or 'tune2fs' to perform actions related to filesystem labels."
    quit_command = ["quit", "q"]
    
    try:
        slow_validInput.print_slow("As you delve deeper into the realm of system administration, you find yourself in the heart of a Red Hat system.")
        slow_validInput.print_slow("Before you lies the command line interface, a gateway to the inner workings of the system.")
        slow_validInput.print_slow("You hear whispers of two powerful commands: 'e2label' and 'tune2fs', both capable of manipulating filesystem labels.\n")

        while True:
            user_command = input("Enter the command related to e2label or tune2fs on a Red Hat system: ")
            print("\n")

            if user_command.strip() in quit_command:
                print("Exiting the task. Farewell!")
                return False

            if user_command.strip() in correct_commands:
                print("Command is correct. You can continue.")
                action = input("Do you want to perform an action related to e2label or tune2fs? (e2label/tune2fs/no): ")
                if action.lower() == 'e2label':
                    user_input = input("Write the command to perform action with e2label: ")
                    if user_input.strip() == "e2label <device> <new_label>":
                        print("Action performed with e2label successfully.")
                        copy_to_fstab = input("Do you want to copy this label to the fstab? (yes/no): ")
                        if copy_to_fstab.lower() == 'yes':
                            user_input_fstab = input("Write the command to copy the label to fstab: ")
                            if user_input_fstab.strip() == "echo 'LABEL=<new_label> <mount_point> ext4 defaults 0 0' >> /etc/fstab":
                                print("Label copied to fstab successfully.")
                            else:
                                print("Wrong command. Try again.")
                                print("Hint: Use 'echo 'LABEL=<new_label> <mount_point> ext4 defaults 0 0' >> /etc/fstab' to copy the label to fstab.")
                    else:
                        print("Wrong command for e2label. Try again.")
                        print("Hint: Use 'e2label <device> <new_label>' to set a new label.")
                elif action.lower() == 'tune2fs':
                    user_input = input("Write the command to perform action with tune2fs: ")
                    if user_input.strip() == "tune2fs -L <new_label> <device>":
                        print("Action performed with tune2fs successfully.")
                        copy_to_fstab = input("Do you want to copy this label to the fstab? (yes/no): ")
                        if copy_to_fstab.lower() == 'yes':
                            user_input_fstab = input("Write the command to copy the label to fstab: ")
                            if user_input_fstab.strip() == "echo 'LABEL=<new_label> <mount_point> ext4 defaults 0 0' >> /etc/fstab":
                                print("Label copied to fstab successfully.")
                            else:
                                print("Wrong command. Try again.")
                                print("Hint: Use 'echo 'LABEL=<new_label> <mount_point> ext4 defaults 0 0' >> /etc/fstab' to copy the label to fstab.")
                    else:
                        print("Wrong command for tune2fs. Try again.")
                        print("Hint: Use 'tune2fs -L <new_label> <device>' to set a new label.")
                else:
                    print("No action performed.")
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
    hint = "Hint: Use 'e2label /dev/sdb1' or 'tune2fs -l /dev/sdb1' format."

    try:
        slow_validInput.print_slow("As you embark on your journey to discover the secrets of storage, you encounter a gateway to the realm of disk labels.")
        slow_validInput.print_slow("Before you lies a puzzle: the key to unveil the label of a disk or partition.")
        slow_validInput.print_slow("You must choose your path wisely, using the commands 'e2label' or 'tune2fs' to unlock the mystery.\n")

        while True:
            user_command = input("Enter the command to find the label associated with a disk or partition using e2label or tune2fs (e.g., 'e2label /dev/sdb1' or 'tune2fs -l /dev/sdb1') or type 'quit/q' to exit: ").strip()
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

