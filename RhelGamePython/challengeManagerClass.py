import slow_validInput  # Importing the slow_validInput module for printing messages slowly

class ChallengeManager:
    def __init__(self, name, description, story, options, action_functions):
        # Constructor method to initialize the ChallengeManager class
        self.name = name  # Assigning the name of the challenge
        self.description = description  # Assigning the description of the challenge
        self.story = story  # Assigning the story of the challenge
        self.options = options  # Assigning the list of options available in the challenge
        self.action_functions = action_functions  # Assigning the list of action functions corresponding to each option
        self.count = 0  # Initializing a count variable to track the progress of the challenge
        self.valid_choices = [str(i) for i in range(1, len(options) + 1)]  # Generating a list of valid choices for the user input

    def start_challenge(self):
        # Method to start the challenge
        try:
            slow_validInput.print_slow(f"\n\n{self.name}: {self.description}\n\n")  # Printing the name and description of the challenge
            slow_validInput.print_slow(self.story)  # Printing the story of the challenge

            while True:  # Starting an infinite loop to continue the challenge until it's completed or terminated
                if self.count == len(self.options) - 1:  # Checking if all options have been completed
                    break  # Exiting the loop if all options have been completed
                self._display_options()  # Calling a private method to display the available options to the user

                choice = slow_validInput.get_valid_input("Enter your choice (1-{}): ".format(len(self.options)), self.valid_choices)  # Getting user input for the chosen option

                if choice.isdigit():  # Checking if the user input is a valid digit
                    choice_index = int(choice) - 1  # Converting the user input to an index
                    action_function = self.action_functions[choice_index]  # Getting the action function corresponding to the chosen option
                    if not action_function():  # Calling the action function and checking if it returns False
                        continue  # Skipping to the next iteration of the loop if the action function returns False
                    self.count += 1  # Incrementing the count variable to track progress
                else:
                    slow_validInput.print_slow("Invalid choice. Please enter a number between 1 and {}.".format(len(self.options)))  # Printing an error message for invalid input

        except Exception as e:
            print("An error occurred:", e)  # Handling exceptions and printing an error message

    def _display_options(self):
        # Private method to display the available options to the user
        print("Options:")  # Printing a header for the list of options
        for idx, option in enumerate(self.options, start=1):  # Looping through each option and its index
            print(f"{idx}. {option}")  # Printing the index and option text


