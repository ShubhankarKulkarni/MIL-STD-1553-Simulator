class ModeCodeAnalyzer:

    command_word = ""
    one_data_word_required = False
    broadcast_command_allowed = False

    def __check_if_mode_code(self, sub_address):
        if sub_address == '00' or sub_address == '1f':
            return True
        else:
            return False

    def analyze_mode_code(self, cmd_word):
        self.command_word = cmd_word
        if not self.__check_if_mode_code(cmd_word[3:5].lower()):
            print("Command word does not contain Mode Code.")
            return
        mode_code_function_name = 'mode_code_0x' + cmd_word[-2:].lower()
        mode_code_function = getattr(
            self, mode_code_function_name, lambda: "Invalid Mode Code")
        return mode_code_function()

    def mode_code_0x00(self):
        print("This mode code (0x00) is: \n  Dynamic Bus Control")
        if not self.command_word[2] == "T":
            print("Invalid Command Word as this Mode Code needs T/R bit set")
        self.one_data_word_required = False
        self.broadcast_command_allowed = False

    def mode_code_0x01(self):
        print("This mode code (0x01) is: \n  Synchronize")
        if not self.command_word[2] == "T":
            print("Invalid Command Word as this Mode Code needs T/R bit set")
        self.one_data_word_required = False
        self.broadcast_command_allowed = True

    def mode_code_0x02(self):
        print("This mode code (0x02) is: \n  Transmit Status Word")
        if not self.command_word[2] == "T":
            print("Invalid Command Word as this Mode Code needs T/R bit set")
        self.one_data_word_required = False
        self.broadcast_command_allowed = False

    def mode_code_0x03(self):
        print("This mode code (0x03) is: \n  Initiate Self Test")
        if not self.command_word[2] == "T":
            print("Invalid Command Word as this Mode Code needs T/R bit set")
        self.one_data_word_required = False
        self.broadcast_command_allowed = True

    def mode_code_0x04(self):
        print("This mode code (0x04) is: \n  Transmitter Shutdown")
        if not self.command_word[2] == "T":
            print("Invalid Command Word as this Mode Code needs T/R bit set")
        self.one_data_word_required = False
        self.broadcast_command_allowed = True

    def mode_code_0x05(self):
        print("This mode code (0x05) is: \n  Override Transmitter Shutdown")
        if not self.command_word[2] == "T":
            print("Invalid Command Word as this Mode Code needs T/R bit set")
        self.one_data_word_required = False
        self.broadcast_command_allowed = True

    def mode_code_0x06(self):
        print("This mode code (0x06) is: \n  Inhibit Terminal Flag")
        if not self.command_word[2] == "T":
            print("Invalid Command Word as this Mode Code needs T/R bit set")
        self.one_data_word_required = False
        self.broadcast_command_allowed = True

    def mode_code_0x07(self):
        print("This mode code (0x07) is: \n  Override Inhibit Terminal Flag")
        if not self.command_word[2] == "T":
            print("Invalid Command Word as this Mode Code needs T/R bit set")
        self.one_data_word_required = False
        self.broadcast_command_allowed = True

    def mode_code_0x08(self):
        print("This mode code (0x08) is: \n  Reset Remote Terminal")
        if not self.command_word[2] == "T":
            print("Invalid Command Word as this Mode Code needs T/R bit set")
        self.one_data_word_required = False
        self.broadcast_command_allowed = True

    def mode_code_0x09(self):
        print("This mode code (0x09) is: \n  Reserved")
        if not self.command_word[2] == "T":
            print("Invalid Command Word as this Mode Code needs T/R bit set")
        self.one_data_word_required = False

    def mode_code_0x0a(self):
        print("This mode code (0x0A) is: \n  Reserved")
        if not self.command_word[2] == "T":
            print("Invalid Command Word as this Mode Code needs T/R bit set")
        self.one_data_word_required = False

    def mode_code_0x0b(self):
        print("This mode code (0x0B) is: \n  Reserved")
        if not self.command_word[2] == "T":
            print("Invalid Command Word as this Mode Code needs T/R bit set")
        self.one_data_word_required = False

    def mode_code_0x0c(self):
        print("This mode code (0x0C) is: \n  Reserved")
        if not self.command_word[2] == "T":
            print("Invalid Command Word as this Mode Code needs T/R bit set")
        self.one_data_word_required = False

    def mode_code_0x0d(self):
        print("This mode code (0x0D) is: \n  Reserved")
        if not self.command_word[2] == "T":
            print("Invalid Command Word as this Mode Code needs T/R bit set")
        self.one_data_word_required = False

    def mode_code_0x0e(self):
        print("This mode code (0x0E) is: \n  Reserved")
        if not self.command_word[2] == "T":
            print("Invalid Command Word as this Mode Code needs T/R bit set")
        self.one_data_word_required = False

    def mode_code_0x0f(self):
        print("This mode code (0x0F) is: \n  Reserved")
        if not self.command_word[2] == "T":
            print("Invalid Command Word as this Mode Code needs T/R bit set")
        self.one_data_word_required = False

    def mode_code_0x10(self):
        print("This mode code (0x10) is: \n  Transmit Vector Word")
        if not self.command_word[2] == "T":
            print("Invalid Command Word as this Mode Code needs T/R bit set")
        self.one_data_word_required = True
        self.broadcast_command_allowed = False

    def mode_code_0x11(self):
        print("This mode code (0x11) is: \n  Synchronize (w/data)")
        if not self.command_word[2] == "R":
            print("Invalid Cmd Word as this Mode Code needs T/R bit set to 0")
        self.one_data_word_required = True
        self.broadcast_command_allowed = True

    def mode_code_0x12(self):
        print("This mode code (0x12) is: \n  Transmit Last Command Word")
        if not self.command_word[2] == "T":
            print("Invalid Command Word as this Mode Code needs T/R bit set")
        self.one_data_word_required = True
        self.broadcast_command_allowed = False

    def mode_code_0x13(self):
        print("This mode code (0x13) is: \n  Transmit BIT Word")
        if not self.command_word[2] == "T":
            print("Invalid Command Word as this Mode Code needs T/R bit set")
        self.one_data_word_required = True
        self.broadcast_command_allowed = False

    def mode_code_0x14(self):
        print("This mode code (0x14) is: \n  Selected Transmitter Shutdown")
        if not self.command_word[2] == "R":
            print("Invalid Cmd Word as the Mode Code needs T/R bit set to 0")
        self.one_data_word_required = True
        self.broadcast_command_allowed = True

    def mode_code_0x15(self):
        print("This mode code (0x15) is:")
        print("  Override Selected Transmitter Shutdown")
        if not self.command_word[2] == "R":
            print("Invalid Cmd Word as this Mode Code needs T/R bit set to 0")
        self.one_data_word_required = True
        self.broadcast_command_allowed = True

    def mode_code_0x16(self):
        print("This mode code (0x16) is: \n  Reserved")
        self.one_data_word_required = True

    def mode_code_0x17(self):
        print("This mode code (0x17) is: \n  Reserved")
        self.one_data_word_required = True

    def mode_code_0x18(self):
        print("This mode code (0x18) is: \n  Reserved")
        self.one_data_word_required = True

    def mode_code_0x19(self):
        print("This mode code (0x19) is: \n  Reserved")
        self.one_data_word_required = True

    def mode_code_0x1a(self):
        print("This mode code (0x1A) is: \n  Reserved")
        self.one_data_word_required = True

    def mode_code_0x1b(self):
        print("This mode code (0x1B) is: \n  Reserved")
        self.one_data_word_required = True

    def mode_code_0x1c(self):
        print("This mode code (0x1C) is: \n  Reserved")
        self.one_data_word_required = True

    def mode_code_0x1d(self):
        print("This mode code (0x1D) is: \n  Reserved")
        self.one_data_word_required = True

    def mode_code_0x1e(self):
        print("This mode code (0x1E) is: \n  Reserved")
        self.one_data_word_required = True

    def mode_code_0x1f(self):
        print("This mode code (0x1F) is: \n  Reserved")
        self.one_data_word_required = True
