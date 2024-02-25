import slow_validInput
import physical_volumes

def challenge_4():
    """
    Fourth challenge: Uncover Disk Secrets.
    """
    try:
        slow_validInput.print_slow("As you journey further into the depths of storage management, you recognize the importance of understanding the physical layer of storage.")
        slow_validInput.print_slow("Physical volumes serve as the foundation upon which logical volumes and volume groups are built.")
        slow_validInput.print_slow("To gain a comprehensive understanding of the system's storage infrastructure, you embark on a quest to explore physical volumes.\n")
        slow_validInput.print_slow("With curiosity as your guide, you delve into the intricacies of physical volumes.")
        slow_validInput.print_slow("You examine the available physical storage devices, assessing their characteristics and properties.\n")
    
        count = 0
        valid_choices = ['1', '2', '3', '4']

        while True:
            if count == 3:
                break
            
            # Add more options as needed
            print("Options:")
            print("1. View Physical Volumes")
            print("2. Create Physical Volume")
            print("3. Remove Physical Volume")
            print("4. Continue to next challenge\n")

            choice = slow_validInput.get_valid_input("Enter your choice (1-4): ", valid_choices)
            if choice == '1':
                slow_validInput.print_slow("With a sense of anticipation, you peer into the darkness of the hidden chambers, revealing the physical volumes that lie within.")
                if physical_volumes.view_physical_volumes() == False:
                    continue
                slow_validInput.print_slow("Issuing commands to view the details of physical volumes, you meticulously review the information presented.")
                slow_validInput.print_slow("You observe attributes such as size, usage, and health status, gaining valuable insights into the underlying storage hardware.\n")
                slow_validInput.print_slow("Physical volumes viewed successfully!")
                count += 1
                continue
            elif choice == '2':
                slow_validInput.print_slow("With determination in your heart, you forge a new path forward, creating a physical volume from the raw materials of the digital realm.")
                if physical_volumes.create_physical_volume() == False:
                    continue
                slow_validInput.print_slow("Armed with knowledge of physical volumes, you consider strategies for optimizing storage performance and reliability.")
                slow_validInput.print_slow("You explore techniques such as load balancing and redundancy, ensuring that storage resources are utilized efficiently and resiliently.\n")
                slow_validInput.print_slow("Physical volume created successfully!")
                count += 1
                continue
            elif choice == '3':
                slow_validInput.print_slow("With resolve guiding your hand, you remove a physical volume, untangling its threads from the fabric of the digital universe.")
                if physical_volumes.remove_physical_volume() == False:
                    continue
                slow_validInput.print_slow("Physical volume removed successfully!")
                count += 1
                continue
            elif choice == '4':
                slow_validInput.print_slow("As your quest to explore physical volumes concludes, you reflect on the journey.")
                slow_validInput.print_slow("Through exploration and analysis, you've gained a deeper understanding of the system's storage infrastructure.")
                slow_validInput.print_slow("With this knowledge, you're better equipped to optimize storage resources and ensure the system's resilience in the Red Hat Odyssey.\n")
                break
    except Exception as e:
        print("An error occurred:", e)
