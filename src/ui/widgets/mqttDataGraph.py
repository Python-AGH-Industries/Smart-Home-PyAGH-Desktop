from PyQt6.QtWidgets import QWidget, QVBoxLayout
import pyqtgraph as pg

class MqttDataGraph(QWidget):
    def __init__(self, leftLabel):
        super().__init__()
        self.plot_widget = pg.PlotWidget()

        self.plot_widget.setBackground("#ffffff")

        self.plot_widget.getAxis('left').setPen('w')  
        self.plot_widget.getAxis('left').setTextPen('w')  
        self.plot_widget.getAxis('bottom').setPen('w')  
        self.plot_widget.getAxis('bottom').setTextPen('w')

        self.plot_widget.setLabel('left', leftLabel, color='w')
        self.plot_widget.setLabel('bottom', 'Time', color='w')
        
        left_axis = self.plot_widget.getAxis('left')
        left_axis.setPen(pg.mkPen('w'))
        left_axis.setTextPen(pg.mkPen('w'))

        date_axis = pg.DateAxisItem(orientation='bottom')
        date_axis.setPen('w')  
        date_axis.setTextPen('w')  
        self.plot_widget.setAxisItems({'bottom': date_axis})

        self.plot_widget.setTitle(
            f"{leftLabel} vs Time",
            color='w',
            size='12pt'
        )

        self.plot_widget.showGrid(x=True, y=True, alpha=0.2)

        self.timestamps = []
        self.values = []

        layout = QVBoxLayout(self)
        layout.addWidget(self.plot_widget)

    def drawGraph(self, data):
        self.values = [v for v, _ in data]
        self.timestamps = [t.timestamp() for _, t in data]
        self.plot_widget.clear()
        self.plot_widget.plot(self.timestamps, self.values, pen='w') 

    def changePenColor(self, color):
        self.plot_widget.clear()
        self.plot_widget.plot(self.timestamps, self.values, pen=color)

    def changeGraphBackground(self, color):
        self.plot_widget.setBackground(color)