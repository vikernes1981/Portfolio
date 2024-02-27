import slow_validInput

class Challenge:
    def __init__(self, challenge_number, description, story, options):
        self.challenge_number = challenge_number
        self.description = description
        self.story = story
        self.options = options

    def execute(self):
        try:
            slow_validInput.print_slow("\n\nChallenge {}: {}\n\n".format(self.challenge_number, self.description))
            slow_validInput.print_slow(self.story)

            count = 0
            valid_choices = [str(i) for i in range(1, len(self.options) + 1)]

            while True:
                if count == len(self.options):
                    break
                print("Options:")
                for i, option in enumerate(self.options, 1):
                    print(f"{i}. {option['name']}")
                print(f"{len(self.options)+1}. Continue to next challenge\n")

                choice = slow_validInput.get_valid_input("Enter your choice (1-{}): ".format(len(self.options) + 1), valid_choices)

                if choice == str(len(self.options) + 1):
                    break

                selected_option = self.options[int(choice) - 1]
                slow_validInput.print_slow(selected_option['action'])

                if selected_option['function']() == False:
                    continue
                slow_validInput.print_slow("{} successfully!\n".format(selected_option['success_message']))
                count += 1
        except Exception as e:
            print("An error occurred:", e)




# You can define more challenges similarly

if __name__ == "__main__":
    challenge1.execute()




# Call the challenge function
# challenge_configure_boot()

def challenge_1_function():
    return partitions_filesystem.check_disk_space_command()

def challenge_2_function():
    return partitions_filesystem.check_uuid_command()

def challenge_3_function():
    return partitions_filesystem.check_disks_partitions_command()

def challenge_4_function():
    return partitions_filesystem.check_force_partition_check_command()


challenge1 = Challenge(
    challenge_number=1,
    description="Configure Local Storage",
    story=("Suddenly, a flashing icon appears on your display, accompanied by a blaring alert signal."
                   "You quickly access the message, recognizing the emblem of the Central Cybernetic Command."
                   "The message reads: 'Emergency protocol initiated. Urgent transmission incoming.'"
                   "With a sense of apprehension, you accept the transmission, bracing yourself for the impending mission."
                   "A holographic projection materializes before you, displaying the solemn face of a high-ranking officer from the Central Cybernetic Command."
                   "Their voice resonates with urgency as they address you directly:"
                   "'Agent Bishop, the stability of the entire cybernetic infrastructure is in jeopardy.'"
                   "'An anomaly has been detected in the system, one that threatens to disrupt the delicate balance of our digital world.'"
                   "'You, with your unparalleled expertise in Red Hat administration, are our last hope.'"
                   "'Your mission is multifaceted, encompassing system diagnostics, filesystem checks, and ensuring data integrity.'"
                   "Time is of the essence. The fate of humanity rests in your hands.'"
                   "You nod solemnly, understanding the gravity of the situation."
                   "With a determined resolve, you affirm your readiness to embark on the mission and restore stability to the cybernetic infrastructure."
                   "As you navigate through the digital landscape, the urgency of the mission weighs heavily on your mind."
                   "Every command you execute, every diagnostic tool you deploy, is a step towards ensuring the survival of humanity in the digital age."
                   "The fate of countless lives rests on your shoulders, and failure is not an option."),
    options=[
        {'name': 'List Disk Space', 'action': "You initiate the process to list disk space, a crucial step in understanding the resources available in this digital domain.", 'function': challenge_1_function, 'success_message': 'Disk space listed'},
        {'name': 'Get UUIDs', 'action': "With determination, you delve into the depths of the system, seeking to retrieve the UUIDs of the disks.", 'function': challenge_2_function, 'success_message': 'UUIDs retrieved'},
        {'name': 'List Disks and Partitions', 'action': "You navigate the intricate web of disks and partitions, unraveling their secrets one by one.", 'function': challenge_3_function, 'success_message': 'Disks and partitions listed'},
        {'name': 'Force Partition Check', 'action': "With unwavering resolve, you command a forceful partition check, ensuring the stability of the digital landscape.", 'function': challenge_4_function, 'success_message': 'Partition check forced'}
    ]
)