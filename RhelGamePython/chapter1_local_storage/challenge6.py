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
        slow_validInput.print_slow("As you delve deeper into storage configuration, you recognize the importance of reliable and consistent file system mounting.")
        slow_validInput.print_slow("Mounting file systems using UUIDs or labels ensures stability and resilience, even in dynamic storage environments.")
        slow_validInput.print_slow("To achieve this, you embark on a quest to configure file system mounting using UUIDs or labels.\n")
        slow_validInput.print_slow("With foresight and planning, you assess the file systems and their corresponding UUIDs or labels.")
        slow_validInput.print_slow("You consider factors such as file system types, mount points, and compatibility with the system.\n")
        slow_validInput.print_slow("Issuing commands to configure file system mounting with UUIDs or labels, you proceed meticulously.")
        slow_validInput.print_slow("As the commands execute, you ensure that each file system is mounted using its unique identifier or label, ensuring consistency and reliability.\n")

        count = 0
        valid_choices = ['1', '2', '3']

        while True:
            if count == 2:
                slow_validInput.print_slow("After the configuration completes, you verify the mounting configuration to confirm the successful implementation of UUIDs or labels.")
                slow_validInput.print_slow("You check for any errors or warnings, ensuring that file systems are mounted correctly and ready for use.\n")
                slow_validInput.print_slow("As your quest to configure file system mounting concludes, you reflect on the journey.")
                slow_validInput.print_slow("Through meticulous planning and execution, you've successfully implemented a reliable mounting configuration using UUIDs or labels.")
                slow_validInput.print_slow("With file systems mounted consistently and reliably, you're well-prepared to ensure stability and resilience in the Red Hat Odyssey.\n")
                break
            
            print("Options:")
            print("1. Mount File System by UUID")
            print("2. Mount File System by Label")
            print("3. Continue to next challenge\n")

            choice = slow_validInput.get_valid_input("Enter your choice (1-3): ", valid_choices)

            if choice == '1':
                slow_validInput.print_slow("As you delve deeper into storage management, you recognize the importance of robust and reliable partition mounting.")
                slow_validInput.print_slow("Mounting partitions using UUIDs ensures consistent and predictable behavior, even in dynamic storage environments.")
                slow_validInput.print_slow("To achieve this level of stability, you embark on a quest to mount partitions using their UUIDs.\n")
                slow_validInput.print_slow("With precision and attention to detail, you identify the partitions and their corresponding UUIDs.")
                slow_validInput.print_slow("You carefully verify the UUIDs to ensure accuracy and reliability in the mounting process.\n")
                slow_validInput.print_slow("Issuing commands to mount partitions using UUIDs, you proceed meticulously.")
                slow_validInput.print_slow("As the commands execute, you specify the UUIDs for each partition, ensuring consistent and reliable mounting.\n")
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
                slow_validInput.print_slow("After the mounting process completes, you verify the status of the mounted partitions to confirm successful implementation.")
                slow_validInput.print_slow("You check for any errors or warnings, ensuring that partitions are mounted correctly and accessible.\n")
                slow_validInput.print_slow("As your quest to mount partitions using UUID concludes, you reflect on the journey.")
                slow_validInput.print_slow("Through meticulous planning and execution, you've successfully implemented robust partition mounting using UUIDs.")
                slow_validInput.print_slow("With partitions mounted consistently and reliably, you're well-prepared to ensure stability and resilience in the Red Hat Odyssey.\n")
                slow_validInput.print_slow("File systems configured to mount by UUID successfully!\n")
                count += 1
                continue
            elif choice == '2':
                slow_validInput.print_slow("As you continue your exploration of storage management, you acknowledge the significance of flexible and intuitive partition mounting.")
                slow_validInput.print_slow("Mounting partitions using labels provides a human-readable and convenient approach to managing storage configurations.")
                slow_validInput.print_slow("To embrace this approach and enhance usability, you embark on a quest to mount partitions using their labels.\n")
                slow_validInput.print_slow("With careful consideration, you identify the partitions and assign descriptive labels to them.")
                slow_validInput.print_slow("You ensure that each label accurately reflects the purpose or contents of the corresponding partition.\n")
                slow_validInput.print_slow("Issuing commands to mount partitions using labels, you proceed with clarity and precision.")
                slow_validInput.print_slow("As the commands execute, you specify the labels for each partition, promoting intuitive and user-friendly storage management.\n")
                if label_mount.check_e2label_command() == False:
                    continue
                if label_mount.provide_label_line() == False:
                    continue
                slow_validInput.print_slow("After the mounting process completes, you verify the status of the mounted partitions to confirm successful implementation.")
                slow_validInput.print_slow("You check for any errors or warnings, ensuring that partitions are mounted correctly and accessible via their labels.\n")
                slow_validInput.print_slow("As your quest to mount partitions using labels concludes, you reflect on the journey.")
                slow_validInput.print_slow("Through thoughtful consideration and execution, you've embraced a user-friendly approach to partition mounting.")
                slow_validInput.print_slow("With partitions mounted intuitively and conveniently, you're well-prepared to optimize storage management in the Red Hat Odyssey.\n")
                slow_validInput.print_slow("File systems configured to mount by label successfully!\n")
                count += 1
                continue
            elif choice == '3':
                break
    except Exception as e:
        print("An error occurred:", e)
