### USE FDISK TO CREATE/DELETE/VIEW PARTITIONS ### 


def display_partitions():
    """
    Display information about disk partitions.
    """
    print("\nDisk /dev/sdb: 200 GiB, 214748364800 bytes, 419430400 sectors\n"
          "Units: sectors of 1 * 512 = 512 bytes\n"
          "Sector size (logical/physical): 512 bytes / 512 bytes\n"
          "I/O size (minimum/optimal): 512 bytes / 512 bytes\n"
          "Disklabel type: dos\n"
          "Disk identifier: 0x87654321\n\n"
          "Device     Boot   Start      End  Sectors  Size Id Type\n"
          "/dev/sdb1         2048  20971519  20969472   10G 83 Linux\n"
          "/dev/sdb2      20971520 20973567      2048     1M 8e Linux LVM\n")


def delete_partition():
    """
    Delete a partition.
    """
    print("\nDeleting a partition...")
    partition_to_delete = input("Enter the partition you want to delete: ")
    print(f"Partition {partition_to_delete} has been deleted.")


def create_partition():
    """
    Create a new partition.
    """
    print("\nCreating a new partition...")
    partition_number = input("Please enter the partition number (1-4, default 1): ")
    first_sector = input("Please enter the First sector (2048-41943006, default 2048): ")
    last_sector = input("Please enter the Last sector: ")
    
    # Handling default values
    if first_sector == "":
        first_sector = "2048"
    if last_sector == "":
        last_sector = "41943006"
        
    print(f"Partition {partition_number} has been created from sector {first_sector} to {last_sector}.")

def display_help():
    """
    Display a help menu for partition management.
    """
    print("\nHelp:\n"
          "\nGPT\n"
          " M   enter protective/hybrid MBR\n"
          "\nGeneric\n"
          " d   delete a partition\n"
          " F   list free unpartitioned space\n"
          " l   list known partition types\n"
          " n   add a new partition\n"
          " p   print the partition table\n"
          " t   change a partition type\n"
          " v   verify the partition table\n"
          " i   print information about a partition\n"
          "\nMisc\n"
          " m   print this menu\n"
          " x   extra functionality (experts only)\n"
          "\nScript\n"
          " I   load disk layout from sfdisk script file\n"
          " O   dump disk layout to sfdisk script file\n"
          "\nSave & Exit\n"
          " w   write table to disk and exit\n"
          " q   quit without saving changes\n"
          "\nCreate a new label\n"
          " g   create a new empty GPT partition table\n"
          " G   create a new empty SGI (IRIX) partition table\n"
          " o   create a new empty DOS partition table\n"
          " s   create a new empty Sun partition table\n\n"
          "Command (m for help):")



def simulate_fdisk_l():
    """
    Simulate the use of fdisk -l to show all physical disks.
    """
    print("Welcome to fdisk -l (show all physical disks)...\n")

    while True:
        user_input = input("Enter command (m for help): ")

        if user_input == 'fdisk -l':
            display_partitions()
        elif user_input.startswith('fdisk /dev/sdb'):
            print("\nWelcome to fdisk (util-linux 2.37.2).\n"
                  "Changes will remain in memory only, until you decide to write them.\n"
                  "Be careful before using the write command.\n"
                  "Command (m for help):")
        elif user_input == 'o':
            print("\nCreating a new empty DOS partition table...\n")
        elif user_input == 'p':
            display_partitions()
        elif user_input == 'w':
            print("\nWriting table to disk and exiting...\n")
            break
        elif user_input == 'q':
            print("\nExiting without saving changes...\n")
            break
        elif user_input == 'n':
            create_partition()
        elif user_input == 'd':
            delete_partition()
        elif user_input == 't':
            change_partition_type()
        elif user_input == 'm':
            display_help()
        else:
            print("Invalid command. Please try again.")

            if user_input not in ['m', 'fdisk -l', 'o', 'p', 'w', 'q', 'n', 'd', 't']:
                print("Unexpected input. Please try again or enter 'm' for help.")


