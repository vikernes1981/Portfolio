import slow_validInput
import fdiskGuide

def challenge_5():
    """
    Fifth challenge: Master Partition Creation with fdisk.
    """
    try:
        slow_validInput.print_slow("\nChallenge 5: Master Partition Creation with fdisk\n\n")
        slow_validInput.print_slow("As you journey deeper into the digital labyrinth, you stumble upon an ancient terminal.")
        slow_validInput.print_slow("Its flickering screen bathed in the soft glow of bygone eras, whispers of legendary sysadmins echo in the air.")
        slow_validInput.print_slow("To progress further, you must demonstrate your mastery over disk partitioning using fdisk, a tool steeped in history and tradition.")
        slow_validInput.print_slow("With each keystroke, you weave a new chapter in the annals of sysadmin lore, leaving your mark upon the digital landscape.")
        slow_validInput.print_slow("Choose your actions wisely, for the partitions you create will shape the destiny of the digital realm, for better or for worse.\n")
    
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
                fdiskGuide.fdisk_guide()
                count += 1
                continue
            elif choice == '2':
                fdiskGuide.create_dos_partition_guide()
                count += 1
                continue
            elif choice == '3':
                fdiskGuide.create_lvm_partition_guide()
                count += 1
                continue
            elif choice == '4':
                fdiskGuide.create_swap_partition_guide()
                count += 1
                continue
            elif choice == '5':
                fdiskGuide.delete_partition_guide()
                count += 1
                continue
            elif choice == '6':
                break
    except Exception as e:
        print("An error occurred:", e)


