 
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

        self.initial_density_ecm = FloatText(
          description='initial_density_ecm',
          step=0.02,
          style=style, layout=layout)

        self.leader_adhesion = FloatText(
          description='leader_adhesion',
          step=0.02,
          style=style, layout=layout)

        self.follower_adhesion = FloatText(
          description='follower_adhesion',
          step=0.02,
          style=style, layout=layout)

        self.default_cell_speed = FloatText(
          description='default_cell_speed',
          step=0.02,
          style=style, layout=layout)

        self.tab = VBox([
          HBox([self.tumor_radius, Label('')]), 
          HBox([self.initial_density_ecm, Label('')]), 
          HBox([self.leader_adhesion, Label('')]), 
          HBox([self.follower_adhesion, Label('')]), 
          HBox([self.default_cell_speed, Label('')]), 
        ])

    # Populate the GUI widgets with values from the XML
    def fill_gui(self, xml_root):
        uep = xml_root.find('.//user_parameters')  # find unique entry point into XML
        self.tumor_radius.value = float(uep.find('.//tumor_radius').text)
        self.initial_density_ecm.value = float(uep.find('.//initial_density_ecm').text)
        self.leader_adhesion.value = float(uep.find('.//leader_adhesion').text)
        self.follower_adhesion.value = float(uep.find('.//follower_adhesion').text)
        self.default_cell_speed.value = float(uep.find('.//default_cell_speed').text)


    # Read values from the GUI widgets to enable editing XML
    def fill_xml(self, xml_root):
        uep = xml_root.find('.//user_parameters')  # find unique entry point into XML 
        uep.find('.//tumor_radius').text = str(self.tumor_radius.value)
        uep.find('.//initial_density_ecm').text = str(self.initial_density_ecm.value)
        uep.find('.//leader_adhesion').text = str(self.leader_adhesion.value)
        uep.find('.//follower_adhesion').text = str(self.follower_adhesion.value)
        uep.find('.//default_cell_speed').text = str(self.default_cell_speed.value)
