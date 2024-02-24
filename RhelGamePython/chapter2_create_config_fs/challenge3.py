import slow_validInput
import autofs_client

def configure_autofs_server_client_nfs():
    """
    Challenge: Configure Autofs on Server and Client sides and Install NFS.
    """
    try:
        slow_validInput.print_slow("\n\nChallenge: Configure Autofs on Server and Client sides and Install NFS\n\n")
        slow_validInput.print_slow("Welcome to the Autofs and NFS configuration challenge.")
        slow_validInput.print_slow("Embark on a journey to streamline file access and enable seamless sharing across your network.\n")
        slow_validInput.print_slow("You can quit at any time by typing 'quit' or 'q'.\n")

        count = 0
        valid_choices = ['1', '2', '3', '4']

        while True:
            if count == 7:
                break
            print("Options:")
            print("1. Configure Autofs on Server side")
            print("2. Configure Autofs on Client side")
            print("3. Install NFS")
            print("4. Continue to next challenge\n")

            choice = slow_validInput.get_valid_input("Enter your choice (1-4): ", valid_choices)

            if choice == '1':
                slow_validInput.print_slow("You begin by configuring Autofs on the server side, enabling dynamic file mounting for remote access.")
                if autofs_client.configure_autofs_server() == False:
                    continue
                slow_validInput.print_slow("Autofs configured successfully on the server side!\n")
                count += 1
                continue

            elif choice == '2':
                slow_validInput.print_slow("You proceed to configure Autofs on the client side, simplifying access to remote files with dynamic mounting.")
                if autofs_client.configure_autofs_client() == False:
                    continue
                slow_validInput.print_slow("Autofs configured successfully on the client side!\n")
                count += 1
                continue

            elif choice == '3':
                slow_validInput.print_slow("You install NFS, laying the groundwork for efficient file sharing and network communication.")
                if autofs_client.install_nfs() == False:
                    continue
                slow_validInput.print_slow("NFS installed successfully!\n")
                count += 1
                continue

            elif choice == '4':
                break

    except KeyboardInterrupt:
        print("\nExiting the task due to user interruption (Ctrl+C). Farewell!")
    except Exception as e:
        print("An error occurred:", e)


