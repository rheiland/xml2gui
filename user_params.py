 
# This file is auto-generated from a Python script that parses a PhysiCell configuration (.xml) file.
#
# Edit at your own risk.
#
import os
from ipywidgets import Label,Text,Checkbox,Button,HBox,VBox,FloatText,IntText,BoundedIntText,BoundedFloatText
    
class UserTab(object):

    def __init__(self):
        
        micron_units = Label('micron')   # use "option m" (Mac, for micro symbol)

        constWidth = '180px'
        tab_height = '500px'
        stepsize = 10

        style = {'description_width': '250px'}
        layout = {'width': '400px'}

        self.tumor_radius = FloatText(
          description='tumor_radius',
          step=0.02,
          style=style, layout=layout)

        self.oncoprotein_mean = FloatText(
          description='oncoprotein_mean',
          step=0.02,
          style=style, layout=layout)

        self.oncoprotein_sd = FloatText(
          description='oncoprotein_sd',
          step=0.02,
          style=style, layout=layout)

        self.oncoprotein_min = FloatText(
          description='oncoprotein_min',
          step=0.02,
          style=style, layout=layout)

        self.oncoprotein_max = FloatText(
          description='oncoprotein_max',
          step=0.02,
          style=style, layout=layout)

        self.random_seed = IntText(
          description='random_seed',
          step=1,
          style=style, layout=layout)

        self.tab = VBox([
          HBox([self.tumor_radius, Label('micron')]), 
          HBox([self.oncoprotein_mean, Label('')]), 
          HBox([self.oncoprotein_sd, Label('')]), 
          HBox([self.oncoprotein_min, Label('')]), 
          HBox([self.oncoprotein_max, Label('')]), 
          HBox([self.random_seed, Label('')]), 
        ])

    # Populate the GUI widgets with values from the XML
    def fill_gui(self, xml_root):
        uep = xml_root.find('.//user_parameters')  # find unique entry point into XML
        self.tumor_radius.value = float(uep.find('.//tumor_radius').text)
        self.oncoprotein_mean.value = float(uep.find('.//oncoprotein_mean').text)
        self.oncoprotein_sd.value = float(uep.find('.//oncoprotein_sd').text)
        self.oncoprotein_min.value = float(uep.find('.//oncoprotein_min').text)
        self.oncoprotein_max.value = float(uep.find('.//oncoprotein_max').text)
        self.random_seed.value = int(uep.find('.//random_seed').text)


    # Read values from the GUI widgets to enable editing XML
    def fill_xml(self, xml_root):
        uep = xml_root.find('.//user_parameters')  # find unique entry point into XML 
        uep.find('.//tumor_radius').text = str(self.tumor_radius.value)
        uep.find('.//oncoprotein_mean').text = str(self.oncoprotein_mean.value)
        uep.find('.//oncoprotein_sd').text = str(self.oncoprotein_sd.value)
        uep.find('.//oncoprotein_min').text = str(self.oncoprotein_min.value)
        uep.find('.//oncoprotein_max').text = str(self.oncoprotein_max.value)
        uep.find('.//random_seed').text = str(self.random_seed.value)
