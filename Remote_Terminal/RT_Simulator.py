from Message_Layer.ML_Analyzer_RT import MessageLayerAnalyzerRT
from Physical_Layer_Emulation.Communication_Socket_RT import RT_Listener
from Physical_Layer_Emulation.Communication_Socket_RT import RT_Sender
import threading
import time


class Remote_Terminal:

    def _send_data_to_bc(self, frames):
        for frame in frames:
            RT_Sender().send_message(bytes(frame))
            time.sleep(1)

    def _handle_incoming_frame(self, frame):
        frames = \
            MessageLayerAnalyzerRT().interprete_incoming_frame(frame)
        if frames:
            self._send_data_to_bc(frames)

    def start_listener(self):
        listener = RT_Listener()
        listener_thread = threading.Thread(
            target=listener.start_listening)
        listener_thread.start()
        while True:
            if not len(listener.data_received) == 0:
                # threading.Thread(
                #     target=self._handle_incoming_frame,
                #     args=(listener.data_received,)).start()
                self._handle_incoming_frame(listener.data_received[0])
                listener.data_received.pop(0)


if __name__ == "__main__":
    rt_listener_thread = threading.Thread(
        target=Remote_Terminal().start_listener)
    rt_listener_thread.start()
