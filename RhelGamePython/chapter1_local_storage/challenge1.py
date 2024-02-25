import partitions_filesystem
import slow_validInput

def challenge_1():
    """
    First challenge: Configure Local Storage.
    """
    try:
        slow_validInput.print_slow("\n\nChallenge 1: Configure Local Storage\n\n")
# Introduction to the urgent mission
        slow_validInput.print_slow("Suddenly, a flashing icon appears on your display, accompanied by a blaring alert signal.")
        slow_validInput.print_slow("You quickly access the message, recognizing the emblem of the Central Cybernetic Command.")
        slow_validInput.print_slow("The message reads: 'Emergency protocol initiated. Urgent transmission incoming.'\n")
        slow_validInput.print_slow("With a sense of apprehension, you accept the transmission, bracing yourself for the impending mission.\n")
        slow_validInput.print_slow("A holographic projection materializes before you, displaying the solemn face of a high-ranking officer from the Central Cybernetic Command.")
        slow_validInput.print_slow("Their voice resonates with urgency as they address you directly:")
        slow_validInput.print_slow("'Agent Bishop, the stability of the entire cybernetic infrastructure is in jeopardy.'")
        slow_validInput.print_slow("'An anomaly has been detected in the system, one that threatens to disrupt the delicate balance of our digital world.'")
        slow_validInput.print_slow("'You, with your unparalleled expertise in Red Hat administration, are our last hope.'")
        slow_validInput.print_slow("'Your mission is multifaceted, encompassing system diagnostics, filesystem checks, and ensuring data integrity.'")
        slow_validInput.print_slow("'Time is of the essence. The fate of humanity rests in your hands.'\n")
        slow_validInput.print_slow("You nod solemnly, understanding the gravity of the situation.")
        slow_validInput.print_slow("With a determined resolve, you affirm your readiness to embark on the mission and restore stability to the cybernetic infrastructure.\n")
        slow_validInput.print_slow("As you navigate through the digital landscape, the urgency of the mission weighs heavily on your mind.")
        slow_validInput.print_slow("Every command you execute, every diagnostic tool you deploy, is a step towards ensuring the survival of humanity in the digital age.")
        slow_validInput.print_slow("The fate of countless lives rests on your shoulders, and failure is not an option.\n")

        count = 0
        valid_choices = ['1', '2', '3', '4', '5']

        while True:
            if count == 4:
                break
            print("Options:")
            print("1. List Disk Space")
            print("2. Get UUIDs")
            print("3. List Disks and Partitions")
            print("4. Force Partition Check")
            print("5. Continue to next challenge\n")

            choice = slow_validInput.get_valid_input("Enter your choice (1-5): ", valid_choices)

            if choice == '1':
                slow_validInput.print_slow("You initiate the process to list disk space, a crucial step in understanding the resources available in this digital domain.")
                if partitions_filesystem.check_disk_space_command() == False:
                    continue
                slow_validInput.print_slow("Disk space listed successfully!\n")
                count += 1
                continue

            elif choice == '2':
                slow_validInput.print_slow("With determination, you delve into the depths of the system, seeking to retrieve the UUIDs of the disks.")
                if partitions_filesystem.check_uuid_command() == False:
                    continue
                slow_validInput.print_slow("UUIDs retrieved successfully!\n")
                count += 1
                continue

            elif choice == '3':
                slow_validInput.print_slow("You navigate the intricate web of disks and partitions, unraveling their secrets one by one.")
                if partitions_filesystem.check_disks_partitions_command() == False:
                    continue
                slow_validInput.print_slow("Disks and partitions listed successfully!\n")
                count += 1
                continue

            elif choice == '4':
                slow_validInput.print_slow("With unwavering resolve, you command a forceful partition check, ensuring the stability of the digital landscape.")
                if partitions_filesystem.check_force_partition_check_command() == False:
                    continue
                slow_validInput.print_slow("Partition check forced successfully!\n")
                count += 1
                continue

            elif choice == '5':
                break
    except Exception as e:
        print("An error occurred:", e)
