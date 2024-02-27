import slow_validInput

class CommandGenerator:
    def __init__(self, action, correct_command, hint, intro_text, outro_text, command_options=None, command_output=None):
        self.action = action
        self.correct_command = correct_command
        self.hint = hint
        self.intro_text = intro_text
        self.outro_text = outro_text
        self.command_options = command_options
        self.command_output = command_output

    def execute(self):
        try:
            slow_validInput.print_slow(self.intro_text)
            while True:
                user_input = input(f"Enter the command to {self.action} or type 'quit/q' to exit: ").strip()
                if user_input.lower() in ['quit', 'q']:
                    print("Exiting the program. Goodbye!")
                    return False
                elif user_input.strip() == self.correct_command:
                    self.handle_correct_command(user_input)
                    return True
                else:
                    print("Incorrect command. Please try again.")
                    print(self.hint)
                    continue
        except KeyboardInterrupt:
            print("\nExiting the program due to user interruption (Ctrl+C). Goodbye!")
            return False
        except Exception as e:
            print("An error occurred:", e)

    def handle_correct_command(self, user_input):
        print("\nCommand is correct. Here are the aspects of the command:")
        print("Command:", user_input)
        print("Purpose:", self.action.capitalize())
        if self.command_options:
            print("\nOptions:")
            for option in self.command_options:
                print(option)
        if self.command_output:
            print("\nOutput Example:")
            for output in self.command_output:
                print(output)
        slow_validInput.print_slow(self.outro_text)
        print("\nYou can continue with the game.")





# Example usage


intro_text = ("As you continue your journey through storage management, you encounter scenarios where certain storage devices need to be retired or replaced."
              "Removing physical volumes associated with these devices is crucial to maintain the integrity and efficiency of the storage infrastructure."
              "To address this, you embark on a quest to safely remove the designated physical volumes.\n"
              "With careful consideration, you assess the implications of removing the physical volumes."
              "You review the volume group configurations and ensure that removing the physical volumes will not compromise data integrity or system performance.\n"
              "Issuing commands to remove the physical volumes, you proceed cautiously, following best practices to minimize risks."
              "As the commands execute, you monitor the removal process, ensuring that each physical volume is detached safely.\n")

outro_text = (f"After the remove command completes, you verify the system's status to confirm the successful removal of the designated physical volumes."
              f"You check for any errors or warnings, ensuring that the storage infrastructure remains stable and operational."
              f"As your quest to remove physical volumes concludes, you reflect on the journey."
              f"Through careful planning and execution, you've successfully removed designated storage devices."
              f"With the physical volumes removed, you're poised to maintain the integrity and efficiency of the storage infrastructure.\n")

command_options = ["-f, --force\t\tForce removal of the physical volume.",
                   "-y, --yes\t\tAssume 'yes' as answer to all questions.",
                   "-v, --verbose\t\tProvide verbose output."]

command_output = ["Labels on physical volume \"/dev/sdb1\" successfully wiped."]

pv_remove_command =CommandGenerator.CommandGenerator(
    action="remove",
    correct_command="pvremove /dev/sdb1",
    hint="Hint: Use the 'pvremove' command followed by the device name to remove a physical volume (e.g., pvremove /dev/sdb1).",
    intro_text=intro_text,
    outro_text=outro_text,
    command_options=command_options,
    command_output=command_output
)

# pv_remove_command.execute()