from Data_Link_Layer.Data_Link_Layer_Encoder_BC import DataLinkLayerEncoderBC


class MessageLayerEncoderBC:

    def construct_command_word(
            self, rt_address, tr_bit, sub_address, data_word_count):
        command_word = ''
        if not len(rt_address) > 2:
            command_word = command_word + rt_address

        if (not len(tr_bit) > 1) and tr_bit.isalpha():
            command_word = command_word + tr_bit

        if not len(sub_address) > 2:
            command_word = command_word + sub_address

        if not len(data_word_count) > 2:
            command_word = command_word + data_word_count

        if len(command_word) < 7 or len(command_word) > 7:
            raise Exception(
                "Invalid data input. Command word format does not match.")
        command_frame = \
            DataLinkLayerEncoderBC().build_cmd_word(command_word)
        return command_frame

    def construct_data_word(self, data_wd_part):
        data_part_frame = \
            DataLinkLayerEncoderBC().build_data_word(data_wd_part)
        # future implementation of checksum here

        return data_part_frame

    def send_message_to_RT(
            self, rt_address, sub_addres_or_mode_code, message):
        communication_frames = list()
        data_word_characters = list()
        message = message + "." if(len(message) % 2 != 0) else message
        for i in range(0, len(message)-1, 2):
            data_word_characters.append(message[i:i+2])
            communication_frames.append(
                self.construct_data_word(message[i:i+2].encode("hex")))
        data_word_count = '{0:02}'.format(len(data_word_characters))
        communication_frames.insert(0, self.construct_command_word(
            rt_address, "R", sub_addres_or_mode_code, data_word_count))
        return communication_frames

    def receive_message_from_RT(
            self, rt_address, sub_addres_or_mode_code, data_word_count):
        communication_frames = list()
        communication_frames.append(
            self.construct_command_word(
                rt_address, "T", sub_addres_or_mode_code, data_word_count))
        return communication_frames
