from Data_Link_Layer.Data_Link_Layer_Decoder_RT import DataLinkLayerDecoderRT
from Data_Link_Layer.Data_Link_Layer_Encoder_RT import DataLinkLayerEncoderRT


class MessageLayerAnalyzerRT:

    lookup_memory = {"01": "AA", "02": "AB", "03": "AC", "04": "AD",
                     "05": "AE", "06": "AF", "07": "AG", "08": "AH",
                     "09": "AI", "0A": "AJ", "0B": "AK", "0C": "AL",
                     "0D": "AM", "0E": "AN", "0F": "AO", "10": "AP",
                     "11": "AQ", "12": "AR", "13": "AS", "14": "AT",
                     "15": "AU", "16": "AV", "17": "AW", "18": "AX",
                     "19": "AY", "1A": "AZ", "1B": "BA", "1C": "BB",
                     "1D": "BC", "1E": "BD", "1F": "BE"}

    def _construct_data_word(self, data_wd_part):
        data_part_frame = \
            DataLinkLayerEncoderRT().build_data_word(data_wd_part)
        # future implementation of checksum here
        return data_part_frame

    def _deconstruct_command_word(self, recd_command_frame):
        recd_command_word = \
            DataLinkLayerDecoderRT().decode_cmd_word(recd_command_frame)
        return recd_command_word

    def _deconstruct_data_word(self, recd_data_frame):
        recd_data_word = \
            DataLinkLayerDecoderRT().decode_data_word(recd_data_frame)
        return recd_data_word

    def _construct_status_word(self, rt_address):
        status_word_frame = \
            DataLinkLayerEncoderRT().build_status_word(rt_address)
        return status_word_frame

    def _analyze_command_word(self, cmd_word):
        rt_address = cmd_word[0:2]
        if not rt_address == "01":
            return 0
        else:
            tr_bit = cmd_word[2]
            if tr_bit == "R":
                return [self._construct_status_word(rt_address)]
            elif tr_bit == "T":
                communication_frames = list()
                communication_frames.append(
                    self._construct_status_word(rt_address))
                data_count = int(cmd_word[-2:], 16)
                for i in range(data_count):
                    communication_frames.append(
                        self._construct_data_word(
                            self.lookup_memory["{0:02x}".format(
                                int(cmd_word[3:5], 16)+i)].encode("hex")))
                return communication_frames

    def interprete_incoming_frame(self, incoming_frame):
        if incoming_frame[0:3] == "100":
            command_word = self._deconstruct_command_word(incoming_frame)
            return self._analyze_command_word(command_word)

        elif incoming_frame[0:3] == "001":
            data_word = self._deconstruct_data_word(incoming_frame)
            print(data_word.decode("hex"))
