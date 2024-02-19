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
        print("\n\nAs you journey deeper into the digital wilderness, you encounter the remnants of an ancient infrastructure,"
              "where the essence of data is bound to physical vessels."
              "These vessels, known as physical volumes, serve as the conduits through which raw data flows,"
              "each bearing the weight of countless digital experiences."
              "In your quest to reshape the digital landscape, you must learn to wield the power to unbind these vessels,"
              "freeing the data within to seek new paths and purpose."
              "The voice of the elders echoes in your mind, guiding your hand as you prepare to undertake this sacred task.\n")
        
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
                print("Labels on physical volume \"/dev/sdb1\" successfully wiped.")
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
        print("\n\nAs you journey deeper into the digital wilderness, you encounter a realm where the fabric of reality is"
              "woven from the essence of raw data."
              "In this ethereal domain, the seeds of creation are sown through the act of transformation – the forging"
              "of physical volumes that serve as the building blocks of digital landscapes."
              "With each command uttered, you shape the destiny of this realm, imbuing it with the potential to host"
              "countless experiences and narratives.\n")
        
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
                print("Physical volume \"/dev/sdb1\" successfully created")
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
        print("\n\nAs you traverse the vast expanse of the digital realm, you come upon a repository of knowledge hidden"
              "beneath layers of code and data."
              "In this sacred archive, the essence of creation is laid bare, manifested in the form of physical volumes"
              "that serve as the bedrock of digital existence."
              "Through the lens of perception, you peer into the depths of this repository, seeking to unravel the"
              "mysteries that lie within.\n")
        
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
                print("PV UUID               eARbpM-M43p-5vMz-hTtM-6F9m-3l6N-AgXYBv")

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
