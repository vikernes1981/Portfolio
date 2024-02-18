import partitions_filesystem
import slow_validInput

def challenge_1():
    """
    First challenge: Configure Local Storage.
    """
    try:
        slow_validInput.print_slow("Challenge 1: Configure Local Storage")
        slow_validInput.print_slow("As you traverse the virtual landscape, neon lights flicker, casting an ethereal glow over your surroundings.")
        slow_validInput.print_slow("Your journey leads you to a desolate outpost, a relic of a bygone era, where a solitary terminal awaits.")
        slow_validInput.print_slow("Approaching cautiously, you activate the terminal, and its ancient screen flickers to life, revealing a cryptic message:")
        slow_validInput.print_slow("'To proceed, you must shape the very essence of this digital world by configuring its local storage.'\n")
        slow_validInput.print_slow("Before you stretch arrays of data, their digital pulses echoing like the heartbeat of the cyber realm.")
        slow_validInput.print_slow("Your mission is clear: navigate the labyrinth of disks and partitions, harness the power of UUIDs, and ensure the integrity of the digital landscape.\n")
        slow_validInput.print_slow("Choose wisely, for the fate of this digital domain lies in your hands.\n")

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
                partitions_filesystem.check_disk_space_command()
                slow_validInput.print_slow("Disk space listed successfully!\n")
                count += 1
                continue

            elif choice == '2':
                slow_validInput.print_slow("With determination, you delve into the depths of the system, seeking to retrieve the UUIDs of the disks.")
                partitions_filesystem.check_uuid_command()
                slow_validInput.print_slow("UUIDs retrieved successfully!\n")
                count += 1
                continue

            elif choice == '3':
                slow_validInput.print_slow("You navigate the intricate web of disks and partitions, unraveling their secrets one by one.")
                partitions_filesystem.check_disks_partitions_command()
                slow_validInput.print_slow("Disks and partitions listed successfully!\n")
                count += 1
                continue

            elif choice == '4':
                slow_validInput.print_slow("With unwavering resolve, you command a forceful partition check, ensuring the stability of the digital landscape.")
                partitions_filesystem.check_force_partition_check_command()
                slow_validInput.print_slow("Partition check forced successfully!\n")
                count += 1
                continue

            elif choice == '5':
                break
    except Exception as e:
        print("An error occurred:", e)
