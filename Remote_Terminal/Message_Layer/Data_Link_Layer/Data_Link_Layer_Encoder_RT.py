class DataLinkLayerEncoderRT:

    message_error_bit = '0'
    instrumentation_bit = '0'
    service_request_bit = '0'
    reserved_bits = '000'
    brdcst_received_bit = '0'
    busy_bit = '0'
    subsystem_flag_bit = '0'
    dynamic_bus_control_accpt_bit = '0'
    terminal_flag_bit = '1'
    parity_bit = '1'

    def __char_check(self, character):
        if not str.isdigit(character):
            print("Invalid address bits")
            return False
        elif int(character) != 0 and int(character) != 1:
            print("Invalid address bits 1")
            return False
        else:
            return True

    def build_status_word(self, rt_address):
        try:
            if len(rt_address) != 2:
                raise Exception("Invalid RT address")
            # Check for foradcast from the command word
            # if Subaddress is 0x1f no need to send status word
            status_word_frame = '100'

            # Following 2 characters represent 5 bit RT Address.
            # Input is HEX. So, first HEX character represent a single bit
            # While the next HEX character represents 4 bits in the frame
            # So, char1 can either be 0 and 1 and char2 can be 0x0-0xF
            char1 = rt_address[0]
            if not self.__char_check(char1):
                exit()
            status_word_frame = status_word_frame + char1

            char2 = rt_address[1]
            status_word_frame = status_word_frame + \
                '{0:04b}'.format(int(char2, 16))

            # rest of the bits are static in this case and will be appended
            # in the final message.
            # The specific functionality can be implemented for each bit
            # separately

            status_word_frame = status_word_frame + self.message_error_bit \
                + self.instrumentation_bit \
                + self.service_request_bit \
                + self.reserved_bits \
                + self.brdcst_received_bit \
                + self.busy_bit \
                + self.subsystem_flag_bit \
                + self.dynamic_bus_control_accpt_bit \
                + self.terminal_flag_bit \
                + self.parity_bit

            # print(status_word_frame)

            return status_word_frame
        except Exception as ex:
            print("Exception while encoding a status word on RT.")
            print("    Exception: {}".format(str(ex)))

    """
        This function takes hex input and converts it into 20 bit binary
        frame including 3 bit sync and 1 bit parity. So, it will take only
        4 hex at a time. Hex are sent in string format.
    """

    def build_data_word(self, data_word):
        try:
            if len(data_word) > 4:
                raise Exception("Invalid data input. Only 4 hex characters are allowed in data word frame")  # noqa

            # Following 3 bits represent sync bits
            # Data word has negative sync hence the value 001

            data_word_frame = '001'

            # Following 4 characters in data words are
            # converted into 4 bit binary
            # and added to the data word frame
            for character in data_word:
                data_word_frame = data_word_frame + \
                    '{0:04b}'.format(int(character, 16))

            # 1 bit parity is added at the end of the frame
            data_word_frame = data_word_frame + '1'

            # print(data_word_frame)

            return(data_word_frame)
        except Exception as ex:
            print("Exception while building a data word on BC")
            print("    Exception: {}".format(str(ex)))
