import slow_validInput

def install_nfs():
    """
    Install NFS (Network File System) on Red Hat.
    """
    try:
        slow_validInput.print_slow("\n\nInstalling NFS (Network File System):\n\n")
        slow_validInput.print_slow("As you prepare to establish connections across the network plains,")
        slow_validInput.print_slow("you encounter the gateway to networked storage - NFS (Network File System).")
        slow_validInput.print_slow("NFS beckons you with promises of seamless file sharing and access,")
        slow_validInput.print_slow("its pathways reaching far and wide across the digital landscape.\n")
        slow_validInput.print_slow("But first, you must invoke the sacred command to install NFS and its allies,\n")
        slow_validInput.print_slow("You can quit at any time by typing 'quit' or 'q'.\n")

        correct_command = "yum install -y nfs-utils"
        quit_commands = ["quit", "q"]

        while True:
            user_command = input("Enter the command to install NFS (type 'quit' or 'q' to exit): ")
            if user_command.strip() in quit_commands:
                slow_validInput.print_slow("Exiting the task. Farewell!")
                return False

            if user_command.strip() == correct_command:
                slow_validInput.print_slow("The command resonates with power as you utter it aloud, invoking the installation process.")
                slow_validInput.print_slow("Mystical energies swirl around you as NFS utilities are installed,")
                slow_validInput.print_slow("their capabilities now at your command.\n")
                slow_validInput.print_slow("NFS installed successfully!\n")
                slow_validInput.print_slow("Output Example:")
                slow_validInput.print_slow("  Installed:\n"
                      "    nfs-utils.x86_64\n")
                return True
            else:
                slow_validInput.print_slow("Incorrect command. Try again.")
                slow_validInput.print_slow("Hint: Use 'yum install -y nfs-utils' to install NFS.")
                continue
    except KeyboardInterrupt:
        slow_validInput.print_slow("\nExiting the task due to user interruption (Ctrl+C). Farewell!")
        return False
    except Exception as e:
        slow_validInput.print_slow("An error occurred:", e)
        return False
