import os
from PySide6.QtCore import QSettings
from app.enums.ThemesEnum import ThemesEnum
from app.resources import resource_path


class ThemesController:
    def __init__(self, app):
        self.__app = app
        self.__themes = (
            resource_path("themes", "default.qss"),
            resource_path("themes", "aurora.qss"),
            resource_path("themes", "darcula.qss"),
            resource_path("themes", "sakura.qss"),
            resource_path("themes", "neon.qss")
        )

        self.__settings = QSettings("DanielPlusPlus", "SQL_Generator_From_Diagram")

        savedThemeName = self.__settings.value("theme", ThemesEnum.DEFAULT.name)
        try:
            saved_theme = ThemesEnum[savedThemeName]
        except KeyError:
            saved_theme = ThemesEnum.DEFAULT

        self.changeTheme(saved_theme)

    def changeTheme(self, ThemeEn):
        index = ThemeEn.value - 1
        if index < 0 or index >= len(self.__themes):
            return

        theme_path = self.__themes[index]
        if not os.path.exists(theme_path):
            return

        with open(theme_path, "r", encoding="utf-8") as theme:
            qss = theme.read()

        self.__app.setStyleSheet(qss)
        self.__settings.setValue("theme", ThemeEn.name)

