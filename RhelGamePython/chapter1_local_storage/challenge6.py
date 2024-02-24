import slow_validInput
import partitions_filesystem
import uuid_mount
import label_mount


def challenge_6():
    """
    Sixth challenge: Configure File System Mounting with UUID or Label.
    """
    try:
        slow_validInput.print_slow("\n\nChallenge 6: Configure File System Mounting with UUID or Label\n\n")
        slow_validInput.print_slow("As you venture deeper into the digital wilderness, you encounter a critical task awaiting your expertise.")
        slow_validInput.print_slow("The system's ability to mount file systems at boot is essential for its functionality and resilience.")
        slow_validInput.print_slow("In this challenge, you must configure the system to mount file systems using either their UUIDs or labels.")
        slow_validInput.print_slow("Choose your actions wisely, for the stability and performance of the system depend on your decisions.\n")

        count = 0
        valid_choices = ['1', '2', '3']

        while True:
            if count == 2:
                break
            
            print("Options:")
            print("1. Mount File System by UUID")
            print("2. Mount File System by Label")
            print("3. Continue to next challenge\n")

            choice = slow_validInput.get_valid_input("Enter your choice (1-3): ", valid_choices)

            if choice == '1':
                slow_validInput.print_slow("With precision and care, you configure the system to mount file systems by their UUIDs, ensuring a reliable boot process.")
                if partitions_filesystem.create_ext4_on_lvm() == False:
                    continue
                if partitions_filesystem.check_uuid_command() == False:
                    continue
                if uuid_mount.edit_fstab() == False:
                    continue
                if uuid_mount.provide_uuid_line() == False:
                    continue
                if uuid_mount.mount_partition() == False:
                    continue
                slow_validInput.print_slow("File systems configured to mount by UUID successfully!\n")
                count += 1
                continue
            elif choice == '2':
                slow_validInput.print_slow("With attention to detail, you set up the system to mount file systems by their labels, simplifying maintenance and management.")
                if label_mount.check_e2label_command() == False:
                    continue
                if label_mount.provide_label_line() == False:
                    continue
                slow_validInput.print_slow("File systems configured to mount by label successfully!\n")
                count += 1
                continue
            elif choice == '3':
                break
    except Exception as e:
        print("An error occurred:", e)
