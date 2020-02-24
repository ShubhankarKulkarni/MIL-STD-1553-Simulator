class DataLinkLayerDecoderRT:

    def decode_cmd_word(self, cmd_word_frame):
        try:
            # 3 bits Sync and 1 bit parity bit are ignored for decoding
            # as it does not affect any data that is necessary
            cmd_word = ''

            # Next 5 bits represents RT address and in the follwing steps,
            # It is converted into back to hex and then string to show
            # on 1553 display
            cmd_word = cmd_word + cmd_word_frame[3]

            addr_char = cmd_word_frame[4:8]
            cmd_word = cmd_word + str(hex(int(addr_char, 2)))[2:]

            # Next bit represent the operating mode i.e transmission or
            # reception. It is converted back to string for display
            tr_char = cmd_word_frame[8]
            if tr_char == '0':
                tr_char = 'R'
            if tr_char == '1':
                tr_char = 'T'
            cmd_word = cmd_word + tr_char

            # Next 5 bits represent the Subaddress or mode code representator
            # 1st bit is taken as is because it will either be 0 or 1
            # next 4 bits are converted to hex and 0x representation is
            # discarded
            # for 1553 display.
            cmd_word = cmd_word + cmd_word_frame[9]

            subaddr_char = cmd_word_frame[10:14]
            cmd_word = cmd_word + str(hex(int(subaddr_char, 2)))[2:]

            # chars = cmd_word_frame[9] + str(hex(int(subaddr_char,2)))[2:]

            # Next 5 bits represents number of data words or mode code based on
            # the value of last 5 bits. If last 5 bits
            # are 0x00 or 0x1f then next
            # 5 bits will be considered as mode codes.
            cmd_word = cmd_word + cmd_word_frame[14]

            word_char = cmd_word_frame[15:19]
            cmd_word = cmd_word + str(hex(int(word_char, 2)))[2:]

            # print(cmd_word)

            return cmd_word
        except Exception as ex:
            print("Exception while decoding a command word from on RT")
            print("    Exception:{}".format(str(ex)))

    def decode_data_word(self, data_word_frame):
        try:
            # 3 bits Sync and 1 bit parity bit are ignored for decoding
            # as it does not affect any data that is necessary
            data_word = ''

            for i in range(3, len(data_word_frame)-4, 4):
                data_set = data_word_frame[i:i+4]
                data_word = data_word + str(hex(int(data_set, 2)))[2:]
            # print(data_word)
            return data_word
        except Exception as ex:
            print("Exception while decoding a data word from on RT")
            print("Exception:{}".format(str(ex)))
