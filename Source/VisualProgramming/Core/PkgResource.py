from pathlib import Path
from PySide6.QtCore import *


class PkgResource:
    RESOURCES_DIR = str(Path(__file__).parent.parent / "Resources" / "Styles")

    @classmethod
    def stylesheet(cls, fileName: str) -> str:
        if not fileName.lower().endswith(".qss"):
            fileName += ".qss"
        path = Path(cls.RESOURCES_DIR) / fileName
        file = QFile(path)
        file.open(QFile.OpenModeFlag.ReadOnly)
        return file.readAll().toStdString()
