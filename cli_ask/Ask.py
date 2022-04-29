class Ask:

    def __init__(self, options: list):
        self.options = options

    def ask(self, query_ask: str):
        print(query_ask)
        options_structure = self.__build_dict()
        user_input = input()
        return options_structure[user_input]

    def __build_dict(self) -> dict:
        option_number = 1
        options_structure = {}
        for option in self.options:
            print(str(option_number) + ". " + option)
            options_structure[str(option_number)] = option
            option_number += 1
        return options_structure