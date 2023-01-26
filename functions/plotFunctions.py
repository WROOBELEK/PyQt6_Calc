
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure
import numpy as np
from sympy.parsing.sympy_parser import parse_expr
from sympy import symbols
import os

class PlotCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=8, height=8):
        """
        Initializes the PlotCanvas (FigureCanvasQTAgg) and sets the figure size.
        """
        fig = Figure(figsize=(width, height))
        self.axes = fig.add_subplot(111)
        super(PlotCanvas, self).__init__(fig)

    def updatePlot(self, text, startX, endX, startY, endY, derivative1, derivative2):
        """
        Updates the plot with the given parameters. Has a try-except block to catch any errors caused by passing wrong expression.
        Params:
            text (str) - expression to plot
            startX (number) - start of x axis
            endX (number) - end of x axis
            startY (number) - start of y axis
            endY (number) - end of y axis
            derivative1 (bool) - whether to plot the first derivative
            derivative2 (bool) - whether to plot the second derivative
        """
        try:
            self.axes.cla()
            x = np.arange(int(startX), int(endX), 0.1)
            self.axes.set_title('f(x) = ' + text)
            self.axes.set_xlabel('x')
            self.axes.set_ylabel('f(x)')
            self.axes.set_xlim([int(startX), int(endX)])
            self.axes.set_ylim([int(startY), int(endY)])
            self.axes.axhline(y=0, color='k', linestyle='--', linewidth=0.2)
            self.axes.axvline(x=0, color='k', linestyle='--', linewidth=0.2)

            for old, new in self.replacements.items():
                text = text.replace(old, new)

            x_sym = symbols('x')
            f_der = parse_expr(text)
            
            if derivative1:
                try:
                    self.axes.plot(x, eval(str(f_der.diff(x_sym))), 'r-')
                except:
                    pass
            if derivative2:
                try:
                    self.axes.plot(x, eval(str(f_der.diff(x_sym).diff(x_sym))), 'g-')
                except:
                    pass
            self.axes.plot(x, eval(text), 'b-')
            self.draw()
        except:
            pass


    replacements = {
            'sin' : 'np.sin',
            'cos' : 'np.cos',
            'tan' : 'np.tan', 
            'tn' : 'np.tan',
            'exp': 'np.exp',
            'sqrt': 'np.sqrt',
            '^': '**',
        }

    def savePlot(self):
        """
        Saves the plot to the results folder.
        """
        if not os.path.isdir('./results'):
            os.mkdir('./results')
        self.figure.savefig('./results/plot.png')