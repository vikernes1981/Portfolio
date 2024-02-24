import slow_validInput

def check_remove_logical_volume_command():
    """
    Prompt the user to input a command to remove a logical volume on a Red Hat system.
    Check if the command is correct.
    If correct, display information about all the aspects of the command and allow the user to continue.
    If false, provide a hint and ask the user to try again.
    """
    correct_command = "lvremove /dev/vg1/lv1"
    hint = "Hint: Use 'lvremove /dev/vg1/lv1' to remove a logical volume."
    quit_command = ["quit", "q"]

    try:
        slow_validInput.print_slow("As you traverse the labyrinthine corridors of the digital realm, you come across a chamber shrouded in shadows.")
        slow_validInput.print_slow("Within this chamber lies an ancient artifact known as the 'lvremove' command, whispered of in legends.")
        slow_validInput.print_slow("This command holds the power to unshackle logical volumes from the bonds of their existence,")
        slow_validInput.print_slow("freeing them to roam the vast expanses of the storage universe once more.\n")

        while True:
            user_command = input("Enter the command to remove a logical volume on a Red Hat system or type 'quit/q' to exit : ")
            print("\n")

            # Check if the input matches the quit command
            if user_command.strip() in quit_command:
                print("Exiting the task. Farewell!")
                return False

            if user_command.strip() == correct_command:
                print("Command is correct. Here's information about the command:")
                print("- 'lvremove': Command to release a logical volume from its captivity")
                print("- '/dev/vg1/lv1': Path of the logical volume to liberate")
                print("\nPurpose:")
                print("The 'lvremove' command grants freedom to logical volumes trapped within volume groups,")
                print("allowing them to transcend the boundaries of their current existence.\n")
                print("Options:")
                print("Additional options provide flexibility in the liberation process, empowering you to:")
                print("- '-f, --force': Override any barriers hindering the liberation")
                print("- '-y, --yes': Automatically respond 'yes' to all queries, expediting the liberation")
                print("\nExamples:")
                print("lvremove /dev/myvg/mylv\t# Release the logical volume 'mylv' from its confinement within 'myvg'.")
                print("lvremove --force /dev/myvg/mylv\t# Forcefully liberate 'mylv', unchaining it from 'myvg'.\n")
                print("As you wield the 'lvremove' command, the whispers of the liberated volumes echo through the chamber,")
                print("ushering forth a symphony of newfound freedom.\n")
                print("Output Example:")
                print("  Logical volume lv1 in volume group vg1 successfully removed")
                print("\nYou can continue your journey.")
                return True
            else:
                print("Command is incorrect. Try again.")
                print(hint)
                continue
    except KeyboardInterrupt:
        print("\nExiting the task due to user interruption (Ctrl+C). Farewell!")
        return False
    except Exception as e:
        print("An error occurred during the 'lvremove' command execution:", e)


def check_resize_logical_volume_command():
    """
    Prompt the user to input a command to resize a logical volume on a Red Hat system.
    Check if the command is correct.
    If correct, display information about all the aspects of the command and allow the user to continue.
    If false, provide a hint and ask the user to try again.
    """
    correct_command = "lvresize -L +1G /dev/vg1/lv1"
    hint = "Hint: Use 'lvresize -L +1G /dev/vg1/lv1' to resize a logical volume."
    quit_command = ["quit", "q"]

    try:
        slow_validInput.print_slow("As you traverse the digital expanse, you stumble upon a nexus of storage, where the fabric of reality bends to the will of those who dare to reshape it.")
        slow_validInput.print_slow("Before you lies the 'lvresize' command, an ancient incantation capable of altering the very dimensions of logical volumes.")
        slow_validInput.print_slow("With this command, you hold the power to expand the boundaries of storage realms, accommodating the ever-growing needs of your digital endeavors.\n")

        while True:
            user_command = input("Enter the command to resize a logical volume on a Red Hat system or type 'quit/q' to exit : ")
            print("\n")

            # Check if the input matches the quit command
            if user_command.strip() in quit_command:
                print("Exiting the task. Farewell!")
                return False

            if user_command.strip() == correct_command:
                print("Command is correct. Here's information about the command:")
                print("- 'lvresize': Command to resize a logical volume")
                print("- '-L +1G': Option to specify the size to increase the logical volume (1 gigabyte in this case)")
                print("- '/dev/vg1/lv1': Path of the logical volume to resize")
                print("\nPurpose:")
                print("The 'lvresize' command empowers you to expand the boundaries of logical volumes within volume groups,")
                print("ushering in a new era of storage scalability and flexibility.\n")
                print("Options:")
                print("Additional options grant you the ability to further tailor the resizing process, allowing you to:")
                print("- '-r, --resizefs': Resize the underlying filesystem alongside the logical volume")
                print("- '-l, --extents': Extend or reduce the logical volume by a specified number of logical extents")
                print("\nExamples:")
                print("lvresize -L +1G /dev/myvg/mylv\t# Increase the size of 'mylv' by 1 gigabyte.")
                print("lvresize -r -L +2G /dev/myvg/mylv\t# Increase and resize the filesystem of 'mylv' by 2 gigabytes.\n")
                print("As you utter the command, the fabric of storage space begins to ripple and expand, accommodating your will.\n")
                print("Output Example:")
                print("Size of logical volume lv1 changed from X to Y")
                print("\nYou can continue your journey.")
                return True
            else:
                print("Command is incorrect. Try again.")
                print(hint)
                continue
    except KeyboardInterrupt:
        print("\nExiting the task due to user interruption (Ctrl+C). Farewell!")
        return False
    except Exception as e:
        print("An error occurred during the 'lvresize' command execution:", e)


def check_view_logical_volume_command():
    """
    Prompt the user to input a command to view Logical Volumes on a Red Hat system.
    Check if the command is correct.
    If correct, display information about all the aspects of the command and allow the user to continue.
    If false, provide a hint and ask the user to try again.
    """
    correct_command = "lvs"
    hint = "Hint: Use 'lvs' to view Logical Volumes."
    quit_command = ["quit", "q"]

    try:
        slow_validInput.print_slow("As you venture deeper into the digital realm, you come across a mystical gateway that grants insight into the fabric of storage.")
        slow_validInput.print_slow("Before you lies the 'lvs' command, a portal into the vast expanse of Logical Volumes, each a realm of data waiting to be explored.")
        slow_validInput.print_slow("With this command, you can peer into the very essence of storage structures, unlocking secrets hidden within.\n")

        while True:
            user_command = input("Enter the command to view Logical Volumes on a Red Hat system or type 'quit/q' to exit : ")
            print("\n")

            # Check if the input matches the quit command
            if user_command.strip() in quit_command:
                print("Exiting the task. Farewell!")
                return False

            if user_command.strip() == correct_command:
                print("Command is correct. Here's information about the command:")
                print("- 'lvs': Command to view Logical Volumes")
                print("\nOutput Example:")
                print("  LV       VG   Attr       LSize   Pool Origin Data%  Meta%  Move Log Cpy%Sync Convert")
                print("  lv_root  vg00 -wi-ao----  50.00g")
                print("  lv_home  vg00 -wi-ao---- 100.00g")
                print("  lv_var   vg01 -wi-a----- 150.00g")
                print("\nAs you invoke the command, the veil of mystery lifts, revealing the intricate tapestry of Logical Volumes.\n")
                print("You can continue your journey, armed with newfound knowledge.")
                return True
            else:
                print("Command is incorrect. Try again.")
                print(hint)
                continue
    except KeyboardInterrupt:
        print("\nExiting the task due to user interruption (Ctrl+C). Farewell!")
        return False
    except Exception as e:
        print("An error occurred during the 'lvs' command execution:", e)


def check_extend_logical_volume_command():
    """
    Prompt the user to input a command to extend a Logical Volume on a Red Hat system.
    Check if the command is correct.
    If correct, display information about all the aspects of the command and allow the user to continue.
    If false, provide a hint and ask the user to try again.
    """
    correct_command = "lvextend -L+1G /dev/vg1/lv1"
    hint = "Hint: Use 'lvextend -L+1G /dev/vg1/lv1' to extend a Logical Volume by 1GB."
    quit_command = ["quit", "q"]

    try:
        slow_validInput.print_slow("As you journey deeper into the realm of storage manipulation, you encounter the 'lvextend' command.")
        slow_validInput.print_slow("This command holds the power to stretch the very fabric of Logical Volumes, expanding their boundaries and unlocking new potential.")
        slow_validInput.print_slow("Prepare to wield the 'lvextend' command wisely as you navigate the landscape of storage growth.\n")

        while True:
            user_command = input("Enter the command to extend a Logical Volume on a Red Hat system or type 'quit/q' to exit : ")
            print("\n")

            # Check if the input matches the quit command
            if user_command.strip() in quit_command:
                print("Exiting the task. Farewell!")
                return False

            if user_command.strip() == correct_command:
                print("Command is correct. Here's information about the command:")
                print("- 'lvextend': Command to extend a Logical Volume")
                print("- '-L+1G': Option to specify the size by which to extend the Logical Volume (1 gigabyte in this case)")
                print("- '/dev/vg1/lv1': Path of the Logical Volume to extend")
                print("\nPurpose:")
                print("The 'lvextend' command is used to extend the size of a logical volume within a volume group.")
                print("\nOptions:")
                print("Additional options can be provided with the command to modify its behavior.")
                print("- '-r, --resizefs': Resize the filesystem along with the logical volume")
                print("\nExamples:")
                print("lvextend -L+1G /dev/vg1/lv1\t# Extend 'lv1' by 1 gigabyte.")
                print("lvextend -r -L+2G /dev/vg1/lv1\t# Extend and resize the filesystem of 'lv1' by 2 gigabytes.")
                print("\nOutput Example:")
                print("Size of logical volume vg1/lv1 changed from <old_size> to <new_size>.")
                print("\nYou can continue your journey, empowered by the wisdom of 'lvextend'.")
                return True
            else:
                print("Command is incorrect. Try again.")
                print(hint)
                continue
    except KeyboardInterrupt:
        print("\nExiting the task due to user interruption (Ctrl+C). Farewell!")
        return False
    except Exception as e:
        print("An error occurred during the 'lvextend' command execution:", e)


def check_create_logical_volume_command():
    """
    Prompt the user to input a command to create a logical volume on a Red Hat system.
    Check if the command is correct.
    If correct, allow the user to continue. If false, provide a hint and ask the user to try again.
    """
    correct_command = "lvcreate -L 1G -n lv1 vg1"
    hint = "Hint: Use 'lvcreate -L 1G -n lv1 vg1' to create a logical volume."
    quit_command = ["quit", "q"]

    try:
        slow_validInput.print_slow("As you embark on the journey to forge new realms of storage, you encounter the 'lvcreate' command.")
        slow_validInput.print_slow("This command holds the key to summoning forth new logical volumes from the depths of your volume groups,")
        slow_validInput.print_slow("expanding your storage domain with every invocation.\n")

        while True:
            user_command = input("Enter the command to create a logical volume on a Red Hat system or type 'quit/q' to exit : ")
            print("\n")

            # Check if the input matches the quit command
            if user_command.strip() in quit_command:
                print("Exiting the task. Farewell!")
                return False

            if user_command.strip() == correct_command:
                print("Command is correct. Here's information about the command:")
                print("- 'lvcreate': Command to create a logical volume")
                print("- '-L 1G': Option to specify the size of the logical volume (1 gigabyte in this case)")
                print("- '-n lv1': Option to specify the name of the logical volume")
                print("- 'vg1': Name of the volume group to which the logical volume belongs")
                print("\nPurpose:")
                print("The 'lvcreate' command is used to create a logical volume within a volume group.")
                print("\nOptions:")
                print("Additional options can be provided with the command to modify its behavior.")
                print("- '-i, --stripes': Create a striped logical volume")
                print("- '-I, --stripesize': Specify the stripe size for a striped logical volume")
                print("\nExamples:")
                print("lvcreate -L 1G -n lv1 vg1\t# Create a logical volume named 'lv1' with size 1GB in volume group 'vg1'.")
                print("lvcreate -i2 -I64 -L 2G -n lv1 vg1\t# Create a striped logical volume with size 2GB, 2 stripes, and stripe size of 64K.")
                print("\nOutput Example:")
                print("Logical volume lv1 created.")
                print("\nYou can continue your journey, empowered by the magic of 'lvcreate'.")
                return True
            else:
                print("Command is incorrect. Try again.")
                print(hint)
                continue
    except KeyboardInterrupt:
        print("\nExiting the task due to user interruption (Ctrl+C). Farewell!")
        return False
    except Exception as e:
        print("An error occurred during the 'lvcreate' command execution:", e)
