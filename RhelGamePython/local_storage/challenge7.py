import slow_validInput
import lv_swap_partition

def challenge_7():
    """
    Seventh challenge: Creation of LV Swap Partition.
    """
    try:
        slow_validInput.print_slow("\n\nChallenge 7: Creation of LV Swap Partition\n\n")
        slow_validInput.print_slow("As you delve deeper into the digital wilderness, you encounter a challenge that tests your mastery over memory management.")
        slow_validInput.print_slow("In this part, you must create a Logical Volume (LV) for swap partition, harnessing the power of abstraction to enhance system performance and stability.\n")
        slow_validInput.print_slow("Choose your actions wisely, for the fate of the digital wilderness hangs in the balance.\n")

        count = 0
        valid_choices = ['1', '2', '3']

        while True:
            if count == 2:
                break
            
            print("Options:")
            print("1. Create LV Swap Partition")
            print("2. Mount swap partition permanently")
            print("3. Continue to finish the game\n")

            choice = slow_validInput.get_valid_input("Enter your choice (1-2): ", valid_choices)

            if choice == '1':
                if lv_swap_partition.lv_swap_partition_creation() == False:
                    continue
                print("Well done,you created a LV Swap partition!")
                count += 1
            elif choice == '2':
                if lv_swap_partition.provide_swap_label_line() == False:
                    continue
                print("Well done,swap is permanently mounted!")
                count += 1
            elif choice == '3':
                break
    except Exception as e:
        print("An error occurred during Challenge 7:", e)