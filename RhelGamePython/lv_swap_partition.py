
### LV SWAP PARTITION ###

import slow_validInput

def lv_swap_partition_creation():
    """
    Create a Logical Volume (LV) for swap partition.
    """
    correct_command = "lvcreate -L 2G -n swap_partition_name vg_name"
    correct_commands = {
        "mkswap": "mkswap /dev/vg_name/swap_partition_name",
        "swapon": "swapon /dev/vg_name/swap_partition_name",
        "swapoff": "swapoff /dev/vg_name/swap_partition_name",
        "umount": "umount /mnt"
    }
    quit_command = ["quit", "q"]

    try:
        slow_validInput.print_slow("As you journey deeper into the digital wilderness, you stumble upon a forgotten enclave nestled amidst the circuitry and data streams.")
        slow_validInput.print_slow("Within this hidden sanctuary, ancient texts whisper tales of a realm where memory transcends the limitations of physicality.")
        slow_validInput.print_slow("The air crackles with static energy as you approach a monolithic structure, its surface adorned with glyphs of arcane symbols.")
        slow_validInput.print_slow("A voice, resonating from the depths of the digital ether, beckons you to unlock the secrets of swap space – a realm where memory and magic intertwine.\n")
        slow_validInput.print_slow("You stand before the threshold of knowledge, tasked with the creation of a swap partition as a logical volume (LV).")
        slow_validInput.print_slow("This ethereal construct, forged from the fabric of the digital realm, is said to enhance the performance and stability of systems, serving as a conduit for the flow of virtual memory.\n")
        
        while True:
            user_command_lvcreate = input("Enter the command to create a swap partition as a logical volume: ")
            print("\n")
            if user_command_lvcreate.strip() == correct_command:
                print("Command is correct. Here's information about the command:")
                print("- 'lvcreate': Command to create a logical volume")
                print("- '-L 2G': Option to specify the size of the logical volume (2 gigabytes in this case)")
                print("- '-n swap_partition_name': Option to specify the name of the logical volume (swap_partition_name)")
                print("- 'vg_name': Name of the volume group to which the logical volume belongs")
                print("\nPurpose:")
                print("The 'lvcreate' command is used to create a logical volume within a volume group.")
                print("\nOptions:")
                print("- '-l, --extents': Specify the size of the logical volume in extents")
                print("- '-i, --stripes': Create a striped logical volume")
                print("- '-I, --stripesize': Specify the stripe size for a striped logical volume")
                print("\nExamples:")
                print("lvcreate -L 2G -n swap_partition_name vg_name\t# Create a logical volume named 'swap_partition_name' with size 2GB in volume group 'vg_name'.")
                print("lvcreate -l 100%FREE -n data_lv my_vg\t# Create a logical volume 'data_lv' using all available space in 'my_vg'.")
                print("\nOutput Example:")
                print("Logical volume swap_partition_name created.")
                print("\nYou can continue.")
                break
            else:
                print("Command is incorrect. Try again.")
                print("Hint: Use 'lvcreate -L 2G -n swap_partition_name vg_name' to create a swap partition as a logical volume.")
                continue

        while True:
            user_command_mkswap = input("Enter the command to format the logical volume as swap: ")
            print("\n")
            if user_command_mkswap.strip() == correct_commands["mkswap"]:
                print("Command is correct.")
                print("mkswap command formats the logical volume as swap.")
                print("\nPurpose:")
                print("The 'mkswap' command is used to set up a Linux swap area on a device or partition.")
                print("\nOptions:")
                print("- '-c, --check': Check the bad blocks before creating the swap area")
                print("- '-f, --force': Force to create the swap area")
                print("\nExamples:")
                print("mkswap /dev/vg_name/swap_partition_name\t# Format the logical volume 'swap_partition_name' as swap.")
                print("\nOutput Example:")
                print("Setting up swapspace version 1, size = 2097148 KiB")
                print("no label, UUID=97017f63-6db1-4d47-8f10-418c79126324")
                print("\nYou can continue.")
                break
            else:
                print("Command is incorrect. Try again.")
                print(f"Hint: Use '{correct_commands['mkswap']}' to format the logical volume as swap.")
                continue

        while True:
            user_command_swapon = input("Enter the command to activate the swap partition: ")
            print("\n")
            if user_command_swapon.strip() == correct_commands["swapon"]:
                print("Command is correct.")
                print("swapon command activates the swap partition.")
                print("\nPurpose:")
                print("The 'swapon' command is used to enable devices and files for paging and swapping.")
                print("\nOptions:")
                print("- '-s, --show': Display swap usage summary")
                print("- '-p, --priority': Set the priority of the swap area")
                print("- '-e, --early': Enable swap early during boot")
                print("\nExamples:")
                print("swapon /dev/vg_name/swap_partition_name\t# Activate the swap partition.")
                print("\nOutput Example:")
                print("NAME         TYPE      SIZE  USED PRIO")
                print("/dev/dm-1    partition   2G    0B   -2")
                print("\nYou can continue.")
                break
            else:
                print("Command is incorrect. Try again.")
                print(f"Hint: Use '{correct_commands['swapon']}' to activate the swap partition.")
                continue

        while True:
            user_command_swapoff = input("Enter the command to deactivate the swap partition: ")
            print("\n")
            if user_command_swapoff.strip() == correct_commands["swapoff"]:
                print("Command is correct.")
                print("swapoff command deactivates the swap partition.")
                print("\nPurpose:")
                print("The 'swapoff' command is used to disable devices and files from paging and swapping.")
                print("\nOptions:")
                print("- '-a, --all': Disable all swap areas.")
                print("\nExamples:")
                print("swapoff /dev/vg_name/swap_partition_name\t# Deactivate the swap partition.")
                print("\nOutput Example:")
                print("Swap partition /dev/vg_name/swap_partition_name was successfully deactivated.")
                print("\nYou can continue.")
                break
            else:
                print("Command is incorrect. Try again.")
                print(f"Hint: Use '{correct_commands['swapoff']}' to deactivate the swap partition.")
                continue

        while True:
            user_command_umount = input("Enter the command to unmount the swap partition: ")
            print("\n")
            if user_command_umount.strip() == correct_commands["umount"]:
                print("Command is correct.")
                print("umount command unmounts the swap partition.")
                print("\nPurpose:")
                print("The 'umount' command is used to unmount a currently mounted filesystem.")
                print("\nOptions:")
                print("- '-l, --lazy': Lazy unmount")
                print("- '-a, --all': Unmount all mountpoints mentioned in /etc/mtab")
                print("\nExamples:")
                print("umount /mnt\t# Unmount the mountpoint '/mnt'.")
                print("\nOutput Example:")
                print("The swap partition is unmounted successfully.")
                print("\nYou can continue.")
                break
            else:
                print("Command is incorrect. Try again.")
                print(f"Hint: Use '{correct_commands['umount']}' to unmount the swap partition.")
                continue  

    except KeyboardInterrupt:
        print("\nExiting the task due to user interruption (Ctrl+C). Farewell!")
        return False
    except Exception as e:
        print("An error occurred during LV swap partition creation:", e)
        return False


