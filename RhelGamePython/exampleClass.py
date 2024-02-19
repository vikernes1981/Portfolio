import slow_validInput
import partitions_filesystem
import uuid_mount
import label_mount

class ChallengeManager:
    def __init__(self, name, description, options, action_functions):
        self.name = name
        self.description = description
        self.options = options
        self.action_functions = action_functions
        self.count = 0
        self.valid_choices = [str(i) for i in range(1, len(options) + 1)]

    def start_challenge(self):
        try:
            slow_validInput.print_slow(f"\n\n{self.name}: {self.description}\n\n")
            slow_validInput.print_slow(self.description)

            while True:
                if self.count == len(self.options) - 1:
                    break
                self._display_options()

                choice = slow_validInput.get_valid_input("Enter your choice (1-{}): ".format(len(self.options)), self.valid_choices)

                if choice.isdigit():
                    choice_index = int(choice) - 1
                    action_function = self.action_functions[choice_index]
                    if not action_function():
                        continue
                    self.count += 1
                else:
                    slow_validInput.print_slow("Invalid choice. Please enter a number between 1 and {}.".format(len(self.options)))

        except Exception as e:
            print("An error occurred:", e)

    def _display_options(self):
        print("Options:")
        for idx, option in enumerate(self.options, start=1):
            print(f"{idx}. {option}")

def mount_by_uuid():
    if partitions_filesystem.create_ext4_on_lvm() and partitions_filesystem.check_uuid_command() \
            and uuid_mount.edit_fstab() and uuid_mount.provide_uuid_line() and uuid_mount.mount_partition():
        return True
    return False

def configure_by_label():
    if label_mount.check_e2label_tune2fs_command():
        return True
    return False

# Define the challenge
challenge = ChallengeManager(
    name="Configure File System Mounting with UUID or Label",
    description="Venture deeper into the digital wilderness and configure the system to mount file systems using either their UUIDs or labels.",
    options=["Mount File System by UUID", "Mount File System by Label", "Continue to next challenge"],
    action_functions=[mount_by_uuid, configure_by_label]
)

# Start the challenge
challenge.start_challenge()
