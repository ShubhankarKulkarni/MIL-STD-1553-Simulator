
# from Bus_Controller.Data_Link_Layer_Encoder_BC import DataLinkLayerEncoderBC
# from Remote_Terminal.Data_Link_Layer_Decoder_RT import DataLinkLayerDecoderRT

# from Remote_Terminal.Data_Link_Layer_Encoder_RT import DataLinkLayerEncoderRT
# from Bus_Controller.Data_Link_Layer_Decoder_BC import DataLinkLayerDecoderBC

# from Remote_Terminal.Mode_Code_Analyzer import ModeCodeAnalyzer

# from Bus_Controller.Message_Layer.ML_Encoder_BC import MessageLayerEncoderBC
# from Bus_Controller.Message_Layer.ML_Decoder_BC import MessageLayerDecoderBC
# from Remote_Terminal.Message_Layer.ML_Analyzer_RT \
#     import MessageLayerAnalyzerRT
# from Bus_Controller.Physical_Layer_Emulation.Communication_Socket_BC \
#     import BC_Sender
from Bus_Controller.BC_Simulator import Bus_Controller
from Remote_Terminal.RT_Simulator import Remote_Terminal
import threading
import time

global bc_listener_thread
global rt_listener_thread

if __name__ == "__main__":
    # cmd_wd_frame = DataLinkLayerEncoderBC().build_cmd_word("01R041F")
    # DataLinkLayerDecoderRT().decode_cmd_word(cmd_wd_frame)

    # status_wd_frame = DataLinkLayerEncoderRT().build_status_word("1F")
    # status_wd = DataLinkLayerDecoderBC().decode_status_word(status_wd_frame)

    # data_wd_frame_BC = DataLinkLayerEncoderBC().build_data_word("ABCD")
    # data_wd_frame_RT = DataLinkLayerEncoderRT().build_data_word("123F")

    # data_word_BC = \
    # DataLinkLayerDecoderBC().decode_data_word(data_wd_frame_BC)

    # ModeCodeAnalyzer().analyze_mode_code("01T1F02")

    # print(MessageLayerEncoderBC().send_message_to_RT(
    #     "01", "11", "SOme message"))
    # print(MessageLayerEncoderBC().receive_message_from_RT("01", "01", "02"))
    # print(
    # MessageLayerAnalyzerRT().interprete_incoming_frame(
    #     "00100001010001001101")
    # print(MessageLayerDecoderBC().interprete_incoming_frame(
    #         "10000001000000000011"))
    # BC_Sender().send_message("10000001000000000011")

    try:
        # bc_listener_thread = threading.Thread(
        #     target=Bus_Controller().start_listener)
        # bc_listener_thread.start()
        # rt_listener_thread = threading.Thread(
        #     target=Remote_Terminal().start_listener)
        # rt_listener_thread.start()

        # time.sleep(5)

        Bus_Controller().send_data_to_rt("01", "11", "Some Message")
        Bus_Controller().receive_data_from_rt("01", "01", "07")

    except KeyboardInterrupt:
        exit()
