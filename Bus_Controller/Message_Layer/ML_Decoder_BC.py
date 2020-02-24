from Data_Link_Layer.Data_Link_Layer_Decoder_BC import DataLinkLayerDecoderBC


class MessageLayerDecoderBC:

    def _deconstruct_status_word(self, recd_status_frame):
        recd_status_word = \
          DataLinkLayerDecoderBC().decode_status_word(recd_status_frame)

        return recd_status_word

    def _deconstruct_data_word(self, receive_data_frame):
        recd_data_word = \
          DataLinkLayerDecoderBC().decode_data_word(receive_data_frame)
        return recd_data_word

    def interprete_incoming_frame(self, received_frame):
        if received_frame[0:3] == "100":
            status_word = self._deconstruct_status_word(received_frame)
            return status_word
        elif received_frame[0:3] == "001":
            data_word = self._deconstruct_data_word(received_frame)
            # print(data_word)
            return data_word.decode("hex")
