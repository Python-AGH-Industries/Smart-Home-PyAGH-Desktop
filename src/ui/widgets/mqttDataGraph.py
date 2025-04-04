from PyQt6.QtWidgets import QWidget, QVBoxLayout
import pyqtgraph as pg

class MqttDataGraph(QWidget):
    def __init__(self, leftLabel):
        super().__init__()
        self.plot_widget = pg.PlotWidget()

        self.plot_widget.setBackground("#f0f0f0")

        self.plot_widget.getAxis('left').setPen('k')  
        self.plot_widget.getAxis('left').setTextPen('k')  
        self.plot_widget.getAxis('bottom').setPen('k')  
        self.plot_widget.getAxis('bottom').setTextPen('k')

        self.plot_widget.setLabel('left', leftLabel, color='k')
        self.plot_widget.setLabel('bottom', 'Time', color='k')
        
        date_axis = pg.DateAxisItem(orientation='bottom')
        date_axis.setPen('k')  
        date_axis.setTextPen('k')  
        self.plot_widget.setAxisItems({'bottom': date_axis})

        self.plot_widget.setTitle(f"{leftLabel} vs Time", color='k', size='12pt')

        self.plot_widget.showGrid(x=True, y=True, alpha=0.2)

        self.timestamps = []
        self.values = []

        layout = QVBoxLayout(self)
        layout.addWidget(self.plot_widget)

    def drawGraph(self, data):
        self.values = [v for v, _ in data]
        self.timestamps = [t.timestamp() for _, t in data]
        self.plot_widget.clear()
        self.plot_widget.plot(self.timestamps, self.values, pen='r') 

    def changePenColor(self, color):
        self.plot_widget.clear()
        self.plot_widget.plot(self.timestamps, self.values, pen=color)

    def changeGraphBackground(self, color):
        self.plot_widget.setBackground(color)