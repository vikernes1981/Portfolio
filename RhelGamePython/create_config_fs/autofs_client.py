import slow_validInput

def configure_autofs_server():
    """
    Install and configure autofs for NFS server on Red Hat.
    """
    try:
        slow_validInput.print_slow("\n\nConfiguring autofs for NFS Server:\n\n")
        slow_validInput.print_slow("As you prepare to automate the mounting of NFS shares,")
        slow_validInput.print_slow("you encounter the gatekeeper of dynamic mounting - autofs.")
        slow_validInput.print_slow("Autofs beckons you with promises of on-demand mounting and unmounting,")
        slow_validInput.print_slow("its mechanisms seamlessly integrating NFS shares into your system.\n")
        slow_validInput.print_slow("But first, you must invoke the sacred commands to install and configure autofs,\n")
        slow_validInput.print_slow("You can quit at any time by typing 'quit' or 'q'.\n")

        # Define the correct commands in the specified order
        correct_commands = [
            'echo "/home/nfsServer ClientIP/24(rw,no_root_squash,no_subtree_check)" >> /etc/exports',  # Appends NFS export configuration to /etc/exports
            "systemctl restart nfs-server.service",  # Restarts NFS server to apply changes in /etc/exports
            "exportfs -a",  # Exports all directories listed in /etc/exports
            "showmount -e localhost"  # Shows NFS shares exported by the localhost
        ]

        quit_commands = ["quit", "q"]
        index = 0
        slow_validInput.print_slow("There are 4 commands you must give in the correct order!")
        while index < len(correct_commands):
            user_command = input(f"Enter the command: '{index + 1}' (type 'quit' or 'q' to exit): ")
            if user_command.strip() in quit_commands:
                slow_validInput.print_slow("Exiting the task. Farewell!")
                return False

            if user_command.strip() == correct_commands[index]:
                slow_validInput.print_slow("Executing the command...")
                # Here you can execute the command using subprocess or other methods
                slow_validInput.print_slow(f"Command '{correct_commands[index]}' executed successfully!\n")
                # slow_validInput.print_slow explanations for each command
                if index == 0:
                    slow_validInput.print_slow("The 'echo' command appends the specified NFS export configuration to /etc/exports.")
                    slow_validInput.print_slow("This configuration allows the NFS server to share the directory '/home/nfsServer' with the IP address 'ClientIP'.")
                elif index == 1:
                    slow_validInput.print_slow("The 'systemctl restart nfs-server.service' command restarts the NFS server service.")
                    slow_validInput.print_slow("This is done to apply the changes made to the NFS exports file (/etc/exports).")
                elif index == 2:
                    slow_validInput.print_slow("The 'exportfs -a' command exports all directories listed in /etc/exports.")
                    slow_validInput.print_slow("This makes the NFS shares available for mounting by remote clients.")
                elif index == 3:
                    slow_validInput.print_slow("The 'showmount -e localhost' command displays the NFS shares exported by the localhost.")
                    slow_validInput.print_slow("This confirms that the NFS server is successfully exporting the specified directories.")
                    
                index += 1
            else:
                slow_validInput.print_slow("Incorrect command. Try again.")
                slow_validInput.print_slow(f"Hint: Use '{correct_commands[index]}' to proceed.")
                continue

        slow_validInput.print_slow("Autofs installation and configuration completed successfully!\n")
        return True

    except KeyboardInterrupt:
        slow_validInput.print_slow("\nExiting the task due to user interruption (Ctrl+C). Farewell!")
        return False
    except Exception as e:
        slow_validInput.print_slow("An error occurred:", e)
        return False



def configure_autofs_client():
    """
    Configure autofs on the client side.
    """
    try:
        slow_validInput.print_slow("\n\nConfiguring autofs for NFS Client:\n\n")
        slow_validInput.print_slow("As you prepare to automate the mounting of NFS shares on the client side,")
        slow_validInput.print_slow("you encounter the gatekeeper of dynamic mounting - autofs.")
        slow_validInput.print_slow("Autofs promises to dynamically mount NFS shares on demand, simplifying access to remote files.\n")
        slow_validInput.print_slow("To proceed, follow the steps below to configure autofs on your system:\n")
        slow_validInput.print_slow("You can quit at any time by typing 'quit' or 'q'.\n")

        correct_commands = [
            "yum install -y autofs",  # Installs autofs package
            "mkdir autofs",  # Creates a directory to mount the NFS shares
            "echo 'autofs    /etc/auto.sharedfs    --timeout=30' >> /etc/auto.master",  # Adds autofs configuration to /etc/auto.master
            "cp /etc/auto.misc /etc/auto.sharedfs",  # Copies the default autofs configuration file
            "echo 'nfsServer -fstype=nfs    ServerIP:/home/user1/nfsServer' >> /etc/auto.sharedfs",  # Adds NFS share configuration to /etc/auto.sharedfs
            "systemctl restart autofs.service",  # Restarts autofs service to apply changes
            "ls /autofs"  # Checks if the directory to be created is mounted
        ]

        quit_commands = ["quit", "q"]
        count = 0
        slow_validInput.print_slow("There are 7 commands you must give in the correct order!")
        while count < len(correct_commands):
            user_command = input(f"Enter the command: '{count + 1}' (type 'quit' or 'q' to exit): ")
            if user_command.strip() in quit_commands:
                slow_validInput.print_slow("Exiting the task. Farewell!")
                return False

            if user_command.strip() == correct_commands[count]:
                slow_validInput.print_slow("Executing the command...")
                slow_validInput.print_slow(f"Command '{correct_commands[count]}' executed successfully!\n")
                # slow_validInput.print_slow explanations for each command
                explanations = [
                    "The 'yum install -y autofs' command installs the autofs package.",
                    "The 'mkdir autofs' command creates a directory to mount the NFS shares.",
                    "The 'echo' command adds autofs configuration to /etc/auto.master.",
                    "The 'cp' command copies the default autofs configuration file to /etc/auto.sharedfs.",
                    "The 'echo' command adds NFS share configuration to /etc/auto.sharedfs.",
                    "The 'systemctl restart autofs' command restarts the autofs service to apply changes.",
                    "The 'ls /autofs' command checks if the directory to be created is mounted.",
                ]
                slow_validInput.print_slow(f"Explanation: {explanations[count]}\n")
                count += 1
            else:
                slow_validInput.print_slow("Incorrect command. Try again.")
                slow_validInput.print_slow(f"Hint: Use '{correct_commands[count]}' to proceed.")
                continue

        slow_validInput.print_slow("Autofs configuration on the client side completed successfully!\n")
        return True

    except KeyboardInterrupt:
        slow_validInput.print_slow("\nExiting the task due to user interruption (Ctrl+C). Farewell!")
        return False
    except Exception as e:
        slow_validInput.print_slow("An error occurred:", e)
        return False


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
