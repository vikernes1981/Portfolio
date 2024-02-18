import slow_validInput

### LIST, CREATE, DELETE PARTITIONS ON MBR AND GPT DISKS ###

def check_force_partition_check_command():
    """
    Prompt the user to input a command to force partition check on a Red Hat system.
    Check if the command is correct.
    If correct, display information about the command and allow the user to continue.
    If false, provide a hint and ask the user to try again.
    """
    correct_command = "partprobe"
    hint = "Hint: Use 'partprobe' to force partition check."
    quit_command = "quit"

    try:
        slow_validInput.print_slow("As you delve into the depths of system partitioning, you encounter the mystical 'partprobe' command,")
        slow_validInput.print_slow("a tool that holds the key to awakening the kernel to changes in your partition tables.\n")

        while True:
            user_command = input("Enter the command to force partition check on a Red Hat system: ")
            print("\n")
            if user_command.strip() == correct_command:
                print("Command acknowledged. Here's what you need to know about 'partprobe':")
                print("- 'partprobe': Command to force partition check")
                print("\nPurpose:")
                print("The 'partprobe' command informs the operating system kernel of partition table changes.")
                print("\nOptions:")
                print("Additional options can be provided with the command to modify its behavior.")
                print("- '-s, --summary': Display summary information after processing")
                print("\nExample Output:")
                print("Partition table updated.")
                print("\nYou can now proceed with your partitioning endeavors, enlightened by the power of 'partprobe'.")
                return True
            elif user_command.strip() == quit_command:
                print("Exiting the program. Goodbye!")
                return False
            else:
                print("Command unrecognized. Try again.")
                print(hint)
                continue
    except Exception as e:
        print("An error occurred during the 'partprobe' command execution:", e)



def check_disks_partitions_command():
    """
    Prompt the user to input a command to list disks and partitions on a Red Hat system.
    Check if the command is correct.
    If correct, display information about the command and allow the user to continue.
    If false, provide a hint and ask the user to try again.
    """
    correct_command = "lsblk"
    hint = "Hint: Use 'lsblk' to list disks and partitions."
    quit_command = "quit"

    try:
        slow_validInput.print_slow("As you journey through the labyrinth of system storage, you encounter the revered 'lsblk' command,")
        slow_validInput.print_slow("a mystical tool that unveils the secrets of disks and their partitions.\n")

        while True:
            user_command = input("Enter the command to list disks and partitions on a Red Hat system: ")
            print("\n")
            if user_command.strip() == correct_command:
                print("Command acknowledged. Here's what you need to know about 'lsblk':")
                print("- 'lsblk': Command to list disks and partitions")
                print("\nPurpose:")
                print("The 'lsblk' command displays information about block devices (disks) and their partitions.")
                print("\nOptions:")
                print("Additional options can be provided with the command to modify its behavior.")
                print("- '-a, --all': Include all devices (e.g., floppy, RAM disks)")
                print("- '-o, --output': Specify columns to display (e.g., 'lsblk -o NAME,SIZE,TYPE,MOUNTPOINT')")
                print("\nOutput Example:")
                print("""   NAME        MAJ:MIN RM   SIZE RO TYPE MOUNTPOINTS
                            loop0         7:0    0     4K  1 loop /snap/bare/5
                            loop1         7:1    0  55,7M  1 loop /snap/core18/2812
                            loop2         7:2    0  63,5M  1 loop /snap/core20/2015
                            loop3         7:3    0  63,9M  1 loop /snap/core20/2105
                            loop4         7:4    0  74,1M  1 loop /snap/core22/1033
                            loop5         7:5    0  74,2M  1 loop /snap/core22/1122
                            nvme0n1     259:0    0 238,5G  0 disk 
                            ├─nvme0n1p1 259:1    0   512M  0 part /boot/efi
                            └─nvme0n1p2 259:2    0   238G  0 part /var/snap/firefox/common/host-hunspell/\n""")
                print("\nYou can now proceed, armed with the knowledge bestowed upon you by 'lsblk'.")
                return True
            elif user_command.strip() == quit_command:
                print("Exiting the program. Goodbye!")
                return False
            else:
                print("Command unrecognized. Try again.")
                print(hint)
                continue
    except Exception as e:
        print("An error occurred during the 'lsblk' command execution:", e)



def check_uuid_command():
    """
    Prompt the user to input a command to get UUIDs on a Red Hat system.
    Check if the command is correct.
    If correct, ask the user if they want to copy the UUID to fstab.
    If yes, prompt the user to write the command to copy the UUID to fstab.
    Provide a hint if the user gives a wrong answer to copying to fstab.
    """
    correct_command = "blkid"
    hint = "Hint: Use 'blkid' to get UUIDs."
    quit_command = "quit"

    try:
        slow_validInput.print_slow("As you traverse through the labyrinth of system storage, you stumble upon the enigmatic 'blkid' command,")
        slow_validInput.print_slow("a tool said to hold the key to unraveling the mystical UUIDs of your system's devices.\n")

        while True:
            user_command = input("Enter the command to get UUIDs on a Red Hat system: ")
            print("\n")
            if user_command.strip() == correct_command:
                print("Command is correct. You can continue.")
                copy_to_fstab = input("Do you want to copy this UUID to the fstab? (yes/no): ")
                if copy_to_fstab.lower() == 'yes':
                    user_input = input("Write the command to copy the UUID to fstab: ")
                    if user_input.strip() == "blkid -s UUID -o value >> /etc/fstab":
                        print("UUID copied to fstab successfully.")
                    else:
                        print("Wrong command. Try again.")
                        print("Hint: Use 'blkid -s UUID -o value >> /etc/fstab' to copy the UUID to fstab.")
                        continue
                else:
                    print("UUID not copied to fstab.")
                return True
            elif user_command.strip() == quit_command:
                print("Exiting the program. Goodbye!")
                return False
            else:
                print("Command is incorrect. Try again.")
                print(hint)
                print("Options: Additional options can be used with blkid command to specify the type of devices or output format.")
                print("Example with options: blkid -t TYPE=ext4 -o list")
                continue
    except Exception as e:
        print("An error occurred during the command execution:", e)



def check_disk_space_command():
    """
    Ask the user to input a command to list disk space on a Red Hat system.
    Check if the command is correct.
    If correct, allow the user to continue. If false, provide a hint and ask the user to try again.
    """
    correct_command = "df -h"
    hint = "Hint: Use 'df -h' to list disk space."
    quit_command = "quit"

    try:
        slow_validInput.print_slow("As you embark on a journey through the vast expanse of storage, you come across the venerable 'df' command,")
        slow_validInput.print_slow("a tool whispered to reveal the secrets of disk space allocation.\n")

        while True:
            user_command = input("Enter the command to list disk space on a Red Hat system: ")
            print("\n")
            if user_command.strip() == correct_command:
                print("Command is correct. You can continue.")
                print("Output Example:")
                print("""Filesystem                        Size  Used Avail Use% Mounted on
                        tmpfs                             773M  2,1M  770M   1% /run
                        /dev/nvme0n1p2                    234G   60G  163G  27% /
                        tmpfs                             3,8G  2,8M  3,8G   1% /dev/shm
                        tmpfs                             5,0M  4,0K  5,0M   1% /run/lock
                        /dev/nvme0n1p1                    511M  6,1M  505M   2% /boot/efi
                        192.168.0.245:/home/user/nfs  457G   55G  379G  13% /home/user1/nfs-share
                        tmpfs                             773M  1,7M  771M   1% /run/user/1000\n""")
                print("Command is correct. You can continue.")
                return True
            elif user_command.strip() == quit_command:
                print("Exiting the program. Goodbye!")
                return False
            else:
                print("Command is incorrect. Try again.")
                print(hint)
                print("Options: Additional options can be used with df command to display disk space in different formats or include specific filesystems.")
                print("Example with options: df -Th /dev/sda1")
                continue
    except Exception as e:
        print("An error occurred during the command execution:", e)


### CREATE FILESYSTEM



def create_ext4_on_lvm():
    """
    Prompt the user to provide the command to create an ext4 file system on a logical volume.
    Check if the command is correct.
    If correct, inform the user that the command is successful.
    If false, provide a hint and ask the user to try again.
    """
    correct_command = "mkfs.ext4 /dev/lvm_group/lvm_volume"
    hint = "Hint: Use 'mkfs.ext4 /dev/lvm_group/lvm_volume' to create an ext4 file system."
    quit_command = "quit"

    try:
        slow_validInput.print_slow("As you navigate through the intricate world of storage, you stumble upon the venerable 'mkfs.ext4' command,")
        slow_validInput.print_slow("a tool whispered to wield the power of file system creation on logical volumes.\n")

        while True:
            user_command = input("Enter the command to create an ext4 file system on a logical volume: ")
            print("\n")
            if user_command.strip() == correct_command:
                print("Command is correct. Ext4 file system created successfully.")
                print("Output Example:")
                print("mke2fs 1.45.6 (20-Mar-2020)")
                print("Creating filesystem with 26214400 4k blocks and 6553600 inodes")
                print("Filesystem UUID: a0d28a15-ef32-4e63-8a26-0e9eac794a10")
                print("Superblock backups stored on blocks: ")
                print("        32768, 98304, 163840, 229376, 294912, 819200, 884736, 1605632, 2654208,")
                print("        4096000, 7962624, 11239424, 20480000, 23887872")

                return True
            elif user_command.strip() == quit_command:
                print("Exiting the program. Goodbye!")
                return False
            else:
                print("Command is incorrect. Try again.")
                print(hint)
                print("Options: Additional options can be used with mkfs.ext4 command to specify file system features or reserve space.")
                print("Options: -L, --label <label> Specify the volume label.")
                print("         -E, --reserved <percent> Specify the percentage of the filesystem reserved for the super-user.")
                print("         -m, --mmp        Enable Multi-Mount Protection.")
                continue
    except Exception as e:
        print("An error occurred during the command execution:", e)