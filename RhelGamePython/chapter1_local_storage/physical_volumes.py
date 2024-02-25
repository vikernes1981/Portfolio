### VIEW, CREATE, REMOVE PHYSICAL VOLUMES ###

def remove_physical_volume():
    """
    Prompt the user to input a command to remove a physical volume on a Red Hat system.
    Check if the command is correct and display information about its aspects and additional options if it is.
    If the command is incorrect, prompt the user to try again and provide a hint.
    """
    # Define the correct command and hint
    correct_command = "pvremove /dev/sdb1"
    hint = "Hint: Use the 'pvremove' command followed by the device name to remove a physical volume (e.g., pvremove /dev/sdb1)."
    quit_command = ["quit", "q"]

    try:
        slow_validInput.print_slow("As you continue your journey through storage management, you encounter scenarios where certain storage devices need to be retired or replaced.")
        slow_validInput.print_slow("Removing physical volumes associated with these devices is crucial to maintain the integrity and efficiency of the storage infrastructure.")
        slow_validInput.print_slow("To address this, you embark on a quest to safely remove the designated physical volumes.\n")
        slow_validInput.print_slow("With careful consideration, you assess the implications of removing the physical volumes.")
        slow_validInput.print_slow("You review the volume group configurations and ensure that removing the physical volumes will not compromise data integrity or system performance.\n")
        slow_validInput.print_slow("Issuing commands to remove the physical volumes, you proceed cautiously, following best practices to minimize risks.")
        slow_validInput.print_slow("As the commands execute, you monitor the removal process, ensuring that each physical volume is detached safely.\n")
        
        while True:
            # Prompt the user for input
            user_input = input("Enter the command to remove a physical volume or type 'quit/q' to exit: ")

            # Check if the input matches any of the quit commands
            if user_input.strip() in quit_command:
                print("Exiting the program. Goodbye!")
                return False

            # Check if the input matches the correct command
            if user_input.strip() == correct_command:
                print("\nCommand is correct. Here are the aspects of the command:")
                print("Command:", user_input)
                print("Purpose: Remove a physical volume.")
                print("\nOptions:")
                print("-f, --force\t\tForce removal of the physical volume.")
                print("-y, --yes\t\tAssume 'yes' as answer to all questions.")
                print("-v, --verbose\t\tProvide verbose output.")
                print("\nOutput Example:")
                print("Labels on physical volume \"/dev/sdb1\" successfully wiped.\n")
                slow_validInput.print_slow("After the removal completes, you verify the system's status to confirm the successful removal of the designated physical volumes.")
                slow_validInput.print_slow("You check for any errors or warnings, ensuring that the storage infrastructure remains stable and operational.\n")
                slow_validInput.print_slow("As your quest to remove physical volumes concludes, you reflect on the journey.")
                slow_validInput.print_slow("Through careful planning and execution, you've successfully retired or replaced designated storage devices.")
                slow_validInput.print_slow("With the physical volumes removed, you're poised to maintain the integrity and efficiency of the storage infrastructure in the Red Hat Odyssey.\n")
                print("\nYou can continue with the game.")
                return True
            else:
                # If the input doesn't match, provide a hint
                print("Incorrect command. Please try again.")
                print(hint)
                continue
    except KeyboardInterrupt:
        print("\nExiting the program due to user interruption (Ctrl+C). Goodbye!")
        return False
    except Exception as e:
        print("An error occurred during the removal of the physical volume:", e)







def create_physical_volume():
    """
    Prompt the user to input a command to create a physical volume on a Red Hat system.
    Check if the command is correct and display information about its aspects if it is.
    If the command is incorrect, prompt the user to try again and provide a hint.
    """
    # Define the correct command and hint
    correct_command = "pvcreate /dev/sdb1"
    hint = "Hint: Use the 'pvcreate' command followed by the device name to create a physical volume (e.g., pvcreate /dev/sdb1)."
    quit_command = ["quit", "q"]

    try:
        slow_validInput.print_slow("As you delve deeper into storage management, you recognize the need to prepare additional storage devices for integration into the system.")
        slow_validInput.print_slow("Creating physical volumes is the first step in incorporating new storage devices into the storage infrastructure.")
        slow_validInput.print_slow("To expand the system's storage capacity and flexibility, you embark on a quest to create physical volumes.\n")
        slow_validInput.print_slow("With determination, you assess the available storage devices and select those to be designated as physical volumes.")
        slow_validInput.print_slow("You consider factors such as device type, capacity, and compatibility with the system.\n")
        slow_validInput.print_slow("Issuing commands to create physical volumes, you proceed with precision, specifying the parameters for each volume.")
        slow_validInput.print_slow("As the commands execute, you observe the creation process, ensuring that each physical volume is initialized successfully.\n")
        
        while True:
            # Prompt the user for input
            user_input = input("Enter the command to create a physical volume or type 'quit/q' to exit: ")

            # Check if the input matches any of the quit commands
            if user_input.strip() in quit_command:
                print("Exiting the program. Goodbye!")
                return False

            # Check if the input matches the correct command
            if user_input.strip() == correct_command:
                print("\nCommand is correct. Here are the aspects of the command:")
                print("Command:", user_input)
                print("Purpose: Create a physical volume.")
                print("\nOptions:")
                print("-v, --verbose\t\tProvide verbose output.")
                print("-ff, --force\t\tForce initialization of device.")
                print("-M, --metadatatype\tSet metadata format.")
                print("\nOutput Example:")
                print("Physical volume \"/dev/sdb1\" successfully created\n")
                slow_validInput.print_slow("After the creation completes, you verify the system's status to confirm the successful establishment of the physical volumes.")
                slow_validInput.print_slow("You check for any errors or warnings, ensuring that the newly created physical volumes are ready for use.\n")
                slow_validInput.print_slow("As your quest to create physical volumes concludes, you reflect on the journey.")
                slow_validInput.print_slow("Through careful planning and execution, you've successfully prepared additional storage devices for integration into the system.")
                slow_validInput.print_slow("With the physical volumes created, you're well-positioned to expand the system's storage capacity and adapt to evolving data requirements in the Red Hat Odyssey.\n")
                print("\nYou can continue with the game.")
                return True
            else:
                # If the input doesn't match, provide a hint
                print("Incorrect command. Please try again.")
                print(hint)
                continue
    except KeyboardInterrupt:
        print("\nExiting the task due to user interruption (Ctrl+C). Farewell!")
        return False
    except Exception as e:
        print("An error occurred during the creation of the physical volume:", e)






def view_physical_volumes():
    """
    Prompt the user to input a command to view physical volumes on a Red Hat system.
    Check if the command is correct and display information about its aspects if it is.
    If the command is incorrect, prompt the user to try again and provide a hint.
    """
    # Define the correct command and hint
    correct_command = "pvdisplay"
    hint = "Hint: Use the 'pvdisplay' command to view physical volumes."
    quit_command = ["quit", "q"]

    try:
        slow_validInput.print_slow("As you delve deeper into storage management, you recognize the importance of gaining insights into the physical layer of storage.")
        slow_validInput.print_slow("Understanding the properties and status of physical volumes is essential for maintaining and optimizing storage infrastructure.")
        slow_validInput.print_slow("To this end, you embark on a quest to view and analyze the physical volumes present in the system.\n")
        slow_validInput.print_slow("With curiosity as your guide, you navigate through the system's storage devices, seeking information on physical volumes.")
        slow_validInput.print_slow("You issue commands to view the details of all physical volumes, eager to gain insights into their configurations and health.\n")
        slow_validInput.print_slow("As the commands execute, you meticulously review the information presented for each physical volume.")
        slow_validInput.print_slow("You observe attributes such as size, usage, and health status, gaining valuable insights into the underlying storage hardware.\n")
        
        while True:
            # Prompt the user for input
            user_input = input("Enter the command to view physical volumes or type 'quit/q' to exit: ")

            # Check if the input matches any of the quit commands
            if user_input.strip() in quit_command:
                print("Exiting the program. Goodbye!")
                return False

            # Check if the input matches the correct command
            if user_input.strip() == correct_command:
                print("\nCommand is correct. Here are the aspects of the command:")
                print("Command:", user_input)
                print("Purpose: View information about physical volumes.")
                print("\nOptions:")
                print("-v, --verbose\t\tProvide verbose output.")
                print("-C, --colon\t\tUse colon separators.")
                print("-m, --maps\t\tDisplay physical volume extent maps.")
                print("\nOutput Example:")
                print("PV Name               /dev/sdb1")
                print("VG Name               vg00")
                print("PV Size               <931.51 GiB / not usable 0")
                print("Allocatable           yes")
                print("PE Size               4.00 MiB")
                print("Total PE              238466")
                print("Free PE               138466")
                print("Allocated PE          100000")
                print("PV UUID               eARbpM-M43p-5vMz-hTtM-6F9m-3l6N-AgXYBv\n")
                slow_validInput.print_slow("Armed with knowledge of physical volumes, you analyze the system's storage utilization and identify areas for optimization.")
                slow_validInput.print_slow("You consider factors such as capacity, usage patterns, and performance requirements, devising strategies to enhance storage efficiency.\n")
                slow_validInput.print_slow("As your quest to view physical volumes concludes, you reflect on the journey.")
                slow_validInput.print_slow("Through exploration and analysis, you've gained valuable insights into the system's storage infrastructure.")
                slow_validInput.print_slow("With this knowledge, you're better equipped to optimize storage resources and ensure the system's resilience in the Red Hat Odyssey.\n")

                print("\nYou can continue with the game.")
                return True
            else:
                # If the input doesn't match, provide a hint
                print("Incorrect command. Please try again.")
                print(hint)
                continue
    except KeyboardInterrupt:
        print("\nExiting the task due to user interruption (Ctrl+C). Farewell!")
        return False
    except Exception as e:
        print("An error occurred while viewing physical volumes:", e)
