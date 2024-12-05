from PySide6.QtMultimedia import QMediaDevices
from typing import List


class AudioService:
    instance = None

    def __new__(cls):
        if not cls.instance:
            cls.instance = super(AudioService, cls).__new__(cls)
        return cls.instance

    def get_sound_outputs(self) -> List[str]:
        return [device.description() for device in QMediaDevices.audioOutputs()]
