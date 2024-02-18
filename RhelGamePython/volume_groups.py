import slow_validInput

def check_remove_physical_volume_command():
    """
    Prompt the user to input a command to remove a physical volume from an existing volume group on a Red Hat system.
    Check if the command is correct.
    If correct, display information about all the aspects of the command and allow the user to continue.
    If false, provide a hint and ask the user to try again.
    """
    correct_command = "vgreduce vg_name /dev/sdb1"
    hint = "Hint: Use 'vgreduce vg_name /dev/sdb1' to remove a physical volume from a volume group."
    quit_command = ["quit", "q"]

    try:
        slow_validInput.print_slow("\n\nAs you delve deeper into the labyrinth of the digital domain, you confront a task of utmost importance.\n")
        slow_validInput.print_slow("Before you lies the heart of a vast volume group, pulsating with the raw essence of storage.\n")
        slow_validInput.print_slow("Your mission is clear: to sever the ties that bind a physical volume to this collective entity,\n")
        slow_validInput.print_slow("unleashing its potential to wander the digital landscape once more.\n\n")

        while True:
            user_command = input("Enter the command to remove a physical volume from an existing volume group on a Red Hat system or type 'quit/q' to exit: ")
            
            # Check if the input matches the quit command
            if user_command.strip() == quit_command:
                print("Exiting the task. Farewell!")
                return False

            if user_command.strip() == correct_command:
                print("Command is correct. Here's information about the command:")
                print("- 'vgreduce': Command to remove a physical volume from an existing volume group")
                print("- 'vg_name': Name of the volume group from which to remove the physical volume")
                print("- '/dev/sdX': Path of the physical volume to remove from the volume group")
                print("\nOptions:")
                print("-a, --all\t\tRemove all physical volumes belonging to the specified volume group.")
                print("-f, --force\t\tForce removal without any prompt.")
                print("-v, --verbose\t\tProvide verbose output.")
                print("\nExamples:")
                print("vgreduce vg_data /dev/sdc1\t\t# Remove '/dev/sdc1' from the 'vg_data' volume group.")
                print("vgreduce -a vg_backup\t\t\t# Remove all physical volumes from 'vg_backup'.")
                print("vgreduce -f vg_home /dev/sdd1\t\t# Forcefully remove '/dev/sdd1' from 'vg_home'.")
                print("\nOutput Example:")
                print("  Removed `/dev/sdX` from volume group `vg_name`")
                print("\nYou can continue.")
                return True
            else:
                # If the input doesn't match, provide a hint
                print("Command is incorrect. Try again.")
                print(hint)
                continue
    
    except KeyboardInterrupt:
        print("\nExiting the task due to user interruption (Ctrl+C). Farewell!")
        return False
    except Exception as e:
        print("An error occurred while checking the command to remove a physical volume:", e)




def check_view_volume_groups_command():
    """
    Prompt the user to input a command to view volume groups on a Red Hat system.
    Check if the command is correct.
    If correct, display information about all the aspects of the command and allow the user to continue.
    If false, provide a hint and ask the user to try again.
    """
    correct_command = "vgs"
    hint = "Hint: Use 'vgs' to view volume groups."
    quit_command = ["quit", "q"]

    try:
        slow_validInput.print_slow("\n\nAs you traverse the digital landscape, you come across a vast repository of storage entities,\n\n")
        slow_validInput.print_slow("each bound together in enigmatic formations known as volume groups.\n\n")
        slow_validInput.print_slow("Their existence is veiled in mystery, yet their significance cannot be overstated.\n\n")
        slow_validInput.print_slow("It is imperative to gain insight into these collective entities to navigate the depths of the digital realm.\n\n")

        while True:
            user_command = input("Enter the command to view volume groups on a Red Hat system or type 'quit/q' to exit: ")
            
            # Check if the input matches any of the quit commands
            if user_command.strip() in quit_command:
                print("Exiting the task. Farewell!")
                return False

            if user_command.strip() == correct_command:
                print("Command is correct. Here's information about the command:")
                print("- 'vgs': Command to view volume groups")
                print("\nOptions:")
                print("--all\t\t\tDisplay all volume groups, including those with no physical volumes.")
                print("-o, --options\t\tDisplay only specified columns.")
                print("-v, --verbose\t\tProvide verbose output.")
                print("\nExamples:")
                print("vgs\t\t\t\t# Display basic information about all volume groups.")
                print("vgs --all\t\t\t# Display all volume groups, even empty ones.")
                print("vgs -o+lv_count\t\t\t# Display volume groups with the number of logical volumes.")
                print("\nOutput Example:")
                print("  VG     #PV #LV #SN Attr   VSize  VFree")
                print("  myvg   1   2   0  wz--n- 19.00g 9.00g")
                print("\nYou can continue.")
                return True
            else:
                # If the input doesn't match, provide a hint
                print("Command is incorrect. Try again.")
                print(hint)
                continue
    
    except KeyboardInterrupt:
        print("\nExiting the task due to user interruption (Ctrl+C). Farewell!")
        return False
    except Exception as e:
        print("An error occurred while checking the command to view volume groups:", e)




def check_remove_volume_group_command():
    """
    Prompt the user to input a command to remove a volume group on a Red Hat system.
    Check if the command is correct.
    If correct, display information about all the aspects of the command and allow the user to continue.
    If false, provide a hint and ask the user to try again.
    """
    correct_command = "vgremove vg_name"
    hint = "Hint: Use 'vgremove vg_name' to remove a volume group."
    quit_command = ["quit", "q"]

    try:
        slow_validInput.print_slow("\n\nAs you navigate the labyrinth of storage infrastructure, you encounter a dormant\n\n")
        slow_validInput.print_slow("volume group, its purpose fulfilled or perhaps forgotten.\n\n")
        slow_validInput.print_slow("In your quest to streamline resources, you must now decide the fate of this\n\n")
        slow_validInput.print_slow("vestige of storage hierarchy, whether to preserve its legacy or consign it to oblivion.\n\n")

        while True:
            user_command = input("Enter the command to remove a volume group on a Red Hat system: ")
            print("\n")
            if user_command.strip() in quit_command:
                print("Exiting the task. Farewell!")
                return False

            if user_command.strip() == correct_command:
                print("Command is correct. Here's information about the command:")
                print("- 'vgremove': Command to remove a volume group")
                print("- 'vg_name': Name of the volume group to remove")
                print("\nOutput Example:")
                print("  Volume group 'vg_name' successfully removed")
                print("\nYou can continue.")
                return True
            else:
                print("Command is incorrect. Try again.")
                print(hint)
                continue
    
    except Exception as e:
        print("An error occurred while checking the command to remove a volume group:", e)



def check_extend_volume_group_command():
    """
    Prompt the user to input a command to extend a volume group on a Red Hat system.
    Check if the command is correct.
    If correct, display information about all the aspects of the command and allow the user to continue.
    If false, provide a hint and ask the user to try again.
    """
    correct_command = "vgextend vg_name /dev/sdX"
    hint = "Hint: Use 'vgextend vg_name /dev/sdX' to extend a volume group."
    quit_command = ["quit", "q"]

    try:
        slow_validInput.print_slow("\n\nAs you journey through the digital expanse, you encounter the limits of storage space,\n\n")
        slow_validInput.print_slow("threatening to impede your progress in the realm of data.\n\n")
        slow_validInput.print_slow("In your quest for expansion, you stumble upon a method to extend the boundaries of\n\n")
        slow_validInput.print_slow("volume groups, unlocking access to untapped reservoirs of storage potential.\n\n")

        while True:
            user_command = input("Enter the command to extend a volume group on a Red Hat system or type 'quit/q' to exit: ")
            print("\n")
            if user_command.strip() in quit_command:
                print("Exiting the task. Farewell!")
                return False

            if user_command.strip() == correct_command:
                print("Command is correct. Here's information about the command:")
                print("- 'vgextend': Command to extend a volume group")
                print("- 'vg_name': Name of the volume group to extend")
                print("- '/dev/sdX': Path of the physical volume(s) to add to the volume group")
                print("\nOptions:")
                print("-v, --verbose\t\tProvide verbose output.")
                print("\nExamples:")
                print("vgextend my_vg /dev/sdb1\t# Extend the volume group 'my_vg' by adding the physical volume '/dev/sdb1'.")
                print("vgextend -v my_vg /dev/sdb1 /dev/sdc1\t# Extend 'my_vg' with verbose output.")
                print("\nOutput Example:")
                print("  Volume group 'vg_name' successfully extended")
                print("\nYou can continue.")
                return True
            else:
                print("Command is incorrect. Try again.")
                print(hint)
                continue
    
    except Exception as e:
        print("An error occurred while checking the command to extend a volume group:", e)


def check_create_volume_group_command():
    """
    Prompt the user to input a command to create a volume group on a Red Hat system.
    Check if the command is correct.
    If correct, display information about all the aspects of the command and allow the user to continue.
    If false, provide a hint and ask the user to try again.
    """
    correct_command = "vgcreate vg_name /dev/sdX"
    hint = "Hint: Use 'vgcreate vg_name /dev/sdX' to create a volume group."
    quit_command = ["quit", "q"]

    try:
        slow_validInput.print_slow("\n\nAs you traverse the vast expanse of storage realms, you stumble upon an opportunity\n\n")
        slow_validInput.print_slow("to forge a new volume group, a crucible of data where disparate entities unite as one.\n\n")
        slow_validInput.print_slow("Embrace this chance to shape the fabric of storage, to weave a tapestry of cohesion\n\n")

        while True:
            user_command = input("Enter the command to create a volume group on a Red Hat system or type 'quit/q' to exit: ")
            print("\n")
            if user_command.strip() in quit_command:
                print("Exiting the task. Farewell!")
                return False

            if user_command.strip() == correct_command:
                print("Command is correct. Here's information about the command:")
                print("- 'vgcreate': Command to create a volume group")
                print("- 'vg_name': Name of the volume group to create")
                print("- '/dev/sdX': Path of the physical volume(s) to include in the volume group")
                print("\nOptions:")
                print("-v, --verbose\t\tProvide verbose output.")
                print("\nExamples:")
                print("vgcreate my_vg /dev/sdb1\t# Create a new volume group 'my_vg' with the physical volume '/dev/sdb1'.")
                print("vgcreate -v my_vg /dev/sdb1 /dev/sdc1\t# Create 'my_vg' with verbose output.")
                print("\nOutput Example:")
                print("  Volume group 'vg_name' successfully created")
                print("\nYou can continue.")
                return True
            else:
                print("Command is incorrect. Try again.")
                print(hint)
                continue
    
    except Exception as e:
        print("An error occurred while checking the command to create a volume group:", e)
