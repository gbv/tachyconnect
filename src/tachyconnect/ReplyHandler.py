from PyQt5.QtCore import pyqtSignal, QObject

class ReplyHandler(QObject):
    fall_back_signal = pyqtSignal(tuple)
    has_fall_back = False
    signals = {}
    command_map = {}
    
    def __init__(self, fall_back = None) -> None:
        super().__init__()
        if fall_back:
            self.fall_back_signal.connect(fall_back)
            self.has_fall_back = True

    
    def register_command(self, label, signal_name):
        self.command_map[label] = self.signals[signal_name]

    def add_connection(self, signal, signal_name, slot):
        self.signals[signal_name].connect(slot)

    def disconnect_all(self):
        for signal in self.signals.values():
            signal.disconnect()
        self.fall_back_signal.disconnect()

    def handle(self, request, reply):
        print(request)
        print(reply)
        signal = self.signals.get(request['message'].label)
        if signal:
            return True
        if self.has_fall_back:
            self.fall_back_signal.emit((request, reply))
            return request, reply
        return False