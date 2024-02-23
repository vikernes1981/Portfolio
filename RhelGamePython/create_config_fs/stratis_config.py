import slow_validInput

def install_stratis():
    """
    Install Stratis, enable stratisd, and perform filesystem wipefs.
    """
    try:
        slow_validInput.print_slow("\n\nInstalling Stratis Storage Management:\n\n")
        slow_validInput.print_slow("Welcome to the Stratis installation process.")
        slow_validInput.print_slow("Stratis offers cutting-edge storage management capabilities for Linux systems.\n")
        slow_validInput.print_slow("As you embark on this installation journey, you prepare to unlock the potential of Stratis")
        slow_validInput.print_slow("and pave the way for streamlined storage operations.\n")
        slow_validInput.print_slow("Let us begin the installation:\n")
        slow_validInput.print_slow("You can quit at any time by typing 'quit' or 'q'.\n")

        correct_commands = [
            "dnf install -y stratis-cli stratisd",  # Installs Stratis packages
            "systemctl enable --now stratisd",  # Enables and starts Stratis daemon
            "wipefs -a /dev/sda",  # Erases filesystem signatures on /dev/sda
        ]

        quit_commands = ["quit", "q"]
        index = 0
        slow_validInput.print_slow("There are 3 commands you must give in the correct order!")
        while index < len(correct_commands):
            user_command = input(f"Enter the command: '{correct_commands[index]}' (type 'quit' or 'q' to exit): ")
            if user_command.strip().lower() in quit_commands:
                slow_validInput.print_slow("Exiting the installation. Farewell!")
                return False

            if user_command.strip() == correct_commands[index]:
                slow_validInput.print_slow("Executing the command...")
                # Here you can execute the command using subprocess or other methods
                slow_validInput.print_slow(f"Command '{correct_commands[index]}' executed successfully!\n")
                # slow_validInput.print_slow explanations for each command
                explanations = [
                    "Installs Stratis packages (stratis-cli and stratisd).",
                    "Enables and starts Stratis daemon.",
                    "Erases filesystem signatures on /dev/sda.",
                ]
                slow_validInput.print_slow(f"Explanation: {explanations[index]}\n")

                if index == 0:
                    slow_validInput.print_slow("The command resonates with power as you utter it aloud, invoking the installation process.")
                    slow_validInput.print_slow("Mystical energies swirl around you as Stratis packages are installed, their arcane capabilities now at your command.\n")
                    slow_validInput.print_slow("Stratis installed successfully!\n")
                    slow_validInput.print_slow("Output Example:")
                    slow_validInput.print_slow("  Installed:\n"
                                             "    stratis-cli.x86_64 0:2.4.3-1.el8\n"
                                             "    stratisd.x86_64 0:2.4.3-1.el8\n")
                index += 1
            else:
                slow_validInput.print_slow("Incorrect command. Try again.")
                slow_validInput.print_slow(f"Hint: Use '{correct_commands[index]}' to proceed.")
                continue

        slow_validInput.print_slow("Stratis installation completed successfully!\n")
        return True

    except KeyboardInterrupt:
        slow_validInput.print_slow("\nExiting the installation due to user interruption (Ctrl+C). Farewell!")
        return False
    except Exception as e:
        slow_validInput.print_slow("An error occurred:", e)
        return False


def create_stratis_snapshot():
    """
    Create a Stratis filesystem snapshot and perform related commands.
    """
    try:
        slow_validInput.print_slow("\n\nCreating Stratis Filesystem Snapshot:\n\n")
        slow_validInput.print_slow("Welcome to the Stratis filesystem snapshot creation process.")
        slow_validInput.print_slow("Stratis offers powerful storage management capabilities for Linux systems.\n")
        slow_validInput.print_slow("As you embark on this journey, you prepare to capture a snapshot")
        slow_validInput.print_slow("of an existing Stratis filesystem and perform related operations.\n")
        slow_validInput.print_slow("Let us begin the snapshot creation process:\n")
        slow_validInput.print_slow("You can quit at any time by typing 'quit' or 'q'.\n")

        correct_commands = [
            "stratis fs snapshot mypool myfs",  # Creates a snapshot of the 'myfs' filesystem in the 'mypool' pool
            "stratis fs list mypool",  # Lists all Stratis filesystems within the 'mypool' pool
            "stratis fs destroy-snapshot mypool myfs <snapshot>",  # Destroys the specified snapshot of 'myfs' filesystem in 'mypool' pool
        ]

        quit_commands = ["quit", "q"]
        index = 0
        slow_validInput.print_slow("There are 3 commands you must give in the correct order!")
        while index < len(correct_commands):
            user_command = input(f"Enter the command: '{correct_commands[index]}' (type 'quit' or 'q' to exit): ")
            if user_command.strip().lower() in quit_commands:
                slow_validInput.print_slow("Exiting the process. Farewell!")
                return False

            if user_command.strip() == correct_commands[index]:
                slow_validInput.print_slow("Executing the command...")
                # Here you can execute the command using subprocess or other methods
                slow_validInput.print_slow(f"Command '{correct_commands[index]}' executed successfully!\n")
                # slow_validInput.print_slow explanations for each command
                explanations = [
                    "Creates a snapshot of the 'myfs' filesystem in the 'mypool' pool.",
                    "Lists all Stratis filesystems within the 'mypool' pool.",
                    "Destroys the specified snapshot of 'myfs' filesystem in 'mypool' pool.",
                ]
                slow_validInput.print_slow(f"Explanation: {explanations[index]}\n")
                # Output examples for each command
                if index == 0:
                    slow_validInput.print_slow("Output Example:")
                    slow_validInput.print_slow("  Created snapshot 'snapshot_name' of filesystem 'myfs' in pool 'mypool'")
                elif index == 1:
                    slow_validInput.print_slow("Output Example:")
                    slow_validInput.print_slow("  Filesystem Name      Used      Total  Quota\n"
                                               "  myfs                2.5 GiB   10 GiB  None")
                elif index == 2:
                    slow_validInput.print_slow("Output Example:")
                    slow_validInput.print_slow("  Destroyed snapshot 'snapshot_name' of filesystem 'myfs' in pool 'mypool'")
                index += 1
            else:
                slow_validInput.print_slow("Incorrect command. Try again.")
                slow_validInput.print_slow(f"Hint: Use '{correct_commands[index]}' to proceed.")
                continue

        slow_validInput.print_slow("Stratis filesystem snapshot operations completed successfully!\n")
        return True

    except KeyboardInterrupt:
        slow_validInput.print_slow("\nExiting the process due to user interruption (Ctrl+C). Farewell!")
        return False
    except Exception as e:
        slow_validInput.print_slow("An error occurred:", e)
        return False

