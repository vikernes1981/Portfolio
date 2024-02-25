import slow_validInput
import fdiskGuide

def challenge_5():
    """
    Fifth challenge: Master Partition Creation with fdisk.
    """
    try:
        slow_validInput.print_slow("\n\nChallenge 5: Master Partition Creation with fdisk\n\n")
        slow_validInput.print_slow("As you further explore storage management, you realize the need to partition available storage space to organize data effectively.")
        slow_validInput.print_slow("Partitioning allows for better utilization of storage resources and facilitates the management of data.")
        slow_validInput.print_slow("To accomplish this task, you embark on a quest to create partitions using the fdisk utility.\n")
        slow_validInput.print_slow("With determination, you assess the storage devices available for partitioning and the desired partition layout.")
        slow_validInput.print_slow("You consider factors such as partition sizes, types, and mount points, ensuring a well-organized storage structure.\n")
        slow_validInput.print_slow("Issuing commands to launch fdisk and create partitions, you proceed methodically, specifying the parameters for each partition.")
        slow_validInput.print_slow("As the commands execute, you carefully define the partition layout, adhering to best practices for storage management.\n")
    
        count = 0
        valid_choices = ['1', '2', '3', '4', '5', '6']

        while True:
            if count == 5:
                break
            
            # Add more options as needed
            print("Options:")
            print("1. View fdisk Guide")
            print("2. Create DOS Partition Guide")
            print("3. Create LVM Partition Guide")
            print("4. Create Swap Partition Guide")
            print("5. Delete Partition Guide")
            print("6. Continue to next challenge\n")

            choice = slow_validInput.get_valid_input("Enter your choice (1-6): ", valid_choices)
            if choice == '1':
                if fdiskGuide.fdisk_guide() == False:
                    continue
                count += 1
                continue
            elif choice == '2':
                if fdiskGuide.create_dos_partition_guide() == False:
                    continue
                count += 1
                continue
            elif choice == '3':
                if fdiskGuide.create_lvm_partition_guide() == False:
                    continue
                count += 1
                continue
            elif choice == '4':
                if fdiskGuide.create_swap_partition_guide() == False:
                    continue
                count += 1
                continue
            elif choice == '5':
                if fdiskGuide.delete_partition_guide() == False:
                    continue
                count += 1
                continue
            elif choice == '6':
                slow_validInput.print_slow("After the partition creation completes, you verify the partition configuration to confirm the successful creation of the desired partitions.")
                slow_validInput.print_slow("You check for any errors or warnings, ensuring that the partition layout aligns with the intended storage structure.\n")
                slow_validInput.print_slow("As your quest to create partitions with fdisk concludes, you reflect on the journey.")
                slow_validInput.print_slow("Through careful planning and execution, you've successfully partitioned available storage space.")
                slow_validInput.print_slow("With the partitions in place, you're well-equipped to organize data effectively and optimize storage management in the Red Hat Odyssey.\n")
                break
    except Exception as e:
        print("An error occurred:", e)


