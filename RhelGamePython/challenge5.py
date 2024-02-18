import slow_validInput

def challenge_5():
    """
    Fifth challenge: Master Partition Creation with fdisk.
    """
    try:
        slow_validInput.print_slow("Challenge 5: Master Partition Creation with fdisk")
        slow_validInput.print_slow("As you journey deeper into the digital labyrinth, you stumble upon an ancient terminal.")
        slow_validInput.print_slow("Its flickering screen bathed in the soft glow of bygone eras, whispers of legendary sysadmins echo in the air.\n")
        slow_validInput.print_slow("To progress further, you must demonstrate your mastery over disk partitioning using fdisk, a tool steeped in history and tradition.\n")
        slow_validInput.print_slow("With each keystroke, you weave a new chapter in the annals of sysadmin lore, leaving your mark upon the digital landscape.\n")
        slow_validInput.print_slow("Choose your actions wisely, for the partitions you create will shape the destiny of the digital realm, for better or for worse.\n")
    
        count = 0
        valid_choices = ['1', '2', '3', '4']

        while True:
            if count == 3:
                break
            
            # Add more options as needed
            print("Options:")
            print("1. View Partition Table")
            print("2. Create New Partition")
            print("3. Delete Partition")
            print("4. Continue to next challenge\n")

            choice = slow_validInput.get_valid_input("Enter your choice (1-4): ", valid_choices)
            if choice == '1':
                slow_validInput.print_slow("With reverence, you gaze upon the ancient terminal, deciphering the partition table that lies before you.")
                fdiskSim.simulate_fdisk_l()
                slow_validInput.print_slow("Partition table viewed successfully!")
                continue
            elif choice == '2':
                slow_validInput.print_slow("With determination in your heart, you carve out a new partition, etching its boundaries into the fabric of the digital realm.")
                fdiskSim.simulate_fdisk_l()
                slow_validInput.print_slow("New partition created successfully!")
                continue
            elif choice == '3':
                slow_validInput.print_slow("With resolve guiding your hand, you remove a partition, reclaiming its space for the greater good of the digital landscape.")
                fdiskSim.simulate_fdisk_l()
                slow_validInput.print_slow("Partition deleted successfully!")
                continue
            elif choice == '4':
                break
    except Exception as e:
        print("An error occurred:", e)
