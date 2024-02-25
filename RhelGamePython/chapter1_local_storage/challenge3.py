import slow_validInput
import volume_groups

def challenge_3():
    """
    Third challenge: Conquer Volume Groups.
    """
    try:
        slow_validInput.print_slow("\n\nChallenge 3: Conquer Volume Groups\n\n")
        slow_validInput.print_slow("As you journey through the digital landscape of the Red Hat Odyssey, you encounter a multitude of challenges.")
        slow_validInput.print_slow("One of the most pressing tasks at hand is the optimization of system storage.")
        slow_validInput.print_slow("With the growth of data and the increasing demands on the system, efficient storage management is paramount.\n")
        slow_validInput.print_slow("You embark on a quest to explore storage management techniques, determined to enhance the system's capabilities.")
        slow_validInput.print_slow("Your journey begins with an exploration of logical volumes and volume groups, fundamental components of storage organization.\n")
        slow_validInput.print_slow("In your quest, you delve into the intricacies of logical volumes.")
        slow_validInput.print_slow("These logical volumes serve as flexible containers for data, allowing for dynamic allocation and resizing.")
        slow_validInput.print_slow("With careful planning and configuration, you create logical volumes tailored to the system's requirements, ensuring efficient storage utilization.\n")
    
        count = 0
        valid_choices = ['1', '2', '3', '4', '5', '6']

        while True:
            if count == 5:
                break
            
            print("Options:")
            print("1. Create Volume Group")
            print("2. Extend Volume Group")
            print("3. Remove Volume Group")
            print("4. View Volume Group")
            print("5. Remove a physical volume from an existing volume group")
            print("6. Continue to next challenge\n")

            choice = slow_validInput.get_valid_input("Enter your choice (1-6): ", valid_choices)

            if choice == '1':
                slow_validInput.print_slow("With determination in your heart, you lay the foundation for a new volume group, a beacon of order amidst the chaos of the digital realm.")
                if volume_groups.check_create_volume_group_command() == False:
                    continue
                slow_validInput.print_slow("Continuing your exploration, you turn your attention to volume groups.")
                slow_validInput.print_slow("Volume groups provide a higher level of organization by grouping logical volumes together, simplifying management and resource allocation.")
                slow_validInput.print_slow("With strategic grouping and careful management, you optimize the system's storage infrastructure, laying the foundation for future scalability.\n")
                slow_validInput.print_slow("Volume group created successfully!\n")
                count += 1
                continue
            elif choice == '2':
                slow_validInput.print_slow("With unwavering resolve, you extend the boundaries of a volume group, expanding its reach to encompass new territories.")
                if volume_groups.check_extend_volume_group_command() == False:
                    continue
                slow_validInput.print_slow("As your journey progresses, you encounter challenges related to storage capacity.")
                slow_validInput.print_slow("To address these challenges, you explore methods for expanding storage capacity.")
                slow_validInput.print_slow("Through the creation of new logical volumes and the extension of existing volumes, you effectively increase the system's storage resources, ensuring it can accommodate growing data needs.\n")
                slow_validInput.print_slow("Volume group extended successfully!\n")
                count += 1
                continue
            elif choice == '3':
                slow_validInput.print_slow("With courage guiding your hand, you dismantle a volume group, unravelling its structure to reveal the core of its existence.")
                if volume_groups.check_remove_volume_group_command() == False:
                    continue
                slow_validInput.print_slow("Continuing your exploration, you turn your attention to volume groups.")
                slow_validInput.print_slow("Volume groups provide a higher level of organization by grouping logical volumes together, simplifying management and resource allocation.")
                slow_validInput.print_slow("With strategic grouping and careful management, you optimize the system's storage infrastructure, laying the foundation for future scalability.\n")
                slow_validInput.print_slow("Volume group removed successfully!\n")
                count += 1
                continue
            elif choice == '4':
                slow_validInput.print_slow("With keen insight, you peer into the heart of a volume group, discerning its secrets and unlocking its potential.")
                if volume_groups.check_view_volume_groups_command() == False:
                    continue
                slow_validInput.print_slow("With the system's storage infrastructure optimized, you turn your focus to monitoring and optimization.")
                slow_validInput.print_slow("Regular monitoring of logical volumes and volume groups allows you to identify potential issues and optimize resource allocation.")
                slow_validInput.print_slow("Through continuous refinement and adjustment, you ensure the system remains resilient and responsive to changing demands.\n")
                slow_validInput.print_slow("Volume group viewed successfully!\n")
                count += 1
                continue
            elif choice == '5':
                slow_validInput.print_slow("With precision and care, you remove a physical volume from an existing volume group, reshaping its structure to suit your needs.")
                if volume_groups.check_remove_physical_volume_command() == False:
                    continue
                slow_validInput.print_slow("Physical volume removed successfully from the existing volume group!\n")
                count += 1
                continue
            elif choice == '6':
                slow_validInput.print_slow("As your quest for storage management concludes, you reflect on the journey.")
                slow_validInput.print_slow("Through exploration and experimentation, you've deepened your understanding of storage technologies and honed your skills in storage administration.")
                slow_validInput.print_slow("Armed with this knowledge, you stand ready to face future challenges, knowing that you can effectively manage and optimize the system's storage resources.\n")
                break
    except KeyboardInterrupt:
        print("\nExiting the program due to user interruption (Ctrl+C). Goodbye!")
    except Exception as e:
        print("An error occurred:", e)
