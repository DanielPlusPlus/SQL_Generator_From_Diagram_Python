from PySide6.QtWidgets import QToolBar
from PySide6.QtGui import QAction, QIcon
from PySide6.QtCore import QSize
from app.resources import resource_path


class ToolBarView(QToolBar):
    def __init__(self, ParentWindow):
        super().__init__(u"Tools", ParentWindow)

    def setupUI(self):
        self.setIconSize(QSize(48, 48))

        self.actionCreateTable = QAction(QIcon(resource_path("icons", "table.png")), u"Create Table", self)
        self.addAction(self.actionCreateTable)

        self.actionCreate_1_1_Rel = QAction(QIcon(resource_path("icons", "1_1_rel.png")), u"Create 1:1 Relationship", self)
        self.addAction(self.actionCreate_1_1_Rel)

        self.actionCreate_1_n_Rel = QAction(QIcon(resource_path("icons", "1_n_rel.png")), u"Create 1:n Relationship", self)
        self.addAction(self.actionCreate_1_n_Rel)

        self.actionCreate_n_n_Rel = QAction(QIcon(resource_path("icons", "n_n_rel.png")), u"Create n:n Relationship", self)
        self.addAction(self.actionCreate_n_n_Rel)

        self.actionCreateInheritance = QAction(QIcon(resource_path("icons", "inheritance.png")),
                                               u"Create Inheritance Relationship", self)
        self.addAction(self.actionCreateInheritance)

        self.actionExportDiagram = QAction(QIcon(resource_path("icons", "saveDiagram.png")), u"Export Diagram", self)
        self.addAction(self.actionExportDiagram)

        self.actionGenerateSQL = QAction(QIcon(resource_path("icons", "generateSQL.png")), u"Generate SQL Code", self)
        self.addAction(self.actionGenerateSQL)
