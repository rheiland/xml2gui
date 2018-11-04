# This script parses a PhysiCell configuration (.xml) file and generates a Jupyter (Python) module
# containing associated widgets for user parameters.
#
# Authors: Daniel Mishler, Tyler Zhang, and Eric Bower (undergraduates in ISE/SICE/IU); Randy Heiland
#
import sys
import xml.etree.ElementTree as ET

if (len(sys.argv) < 2):
    print("Usage: python " + sys.argv[0] + "<config-file.xml>")
    sys.exit(1)
config_file = sys.argv[1]

user_tab_header = """ 
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
"""

"""
        self.therapy_activation_time = BoundedFloatText(
            min=0.,
            max=100000000,
            step=stepsize,
            description='therapy_activation_time',
            style=style, layout=layout,
            # layout=Layout(width=constWidth),
        )
        self.save_interval_after_therapy_start = BoundedFloatText(
            min=0.,
            max=100000000,
            step=stepsize,
            description='save_interval_after_therapy_start',
            style=style, layout=layout,
        )

        label_blankline = Label('')

        self.tab = VBox([HBox([self.therapy_activation_time, Label('min')]), 
                         HBox([self.save_interval_after_therapy_start, Label('min')]), 
                         ])  
"""

fill_gui_str= """

    # Populate the GUI widgets with values from the XML
    def fill_gui(self, xml_root):
        uep = xml_root.find('.//user_parameters')  # find unique entry point into XML
"""

fill_xml_str= """

    # Read values from the GUI widgets to enable editing XML
    def fill_xml(self, xml_root):
        uep = xml_root.find('.//user_parameters')  # find unique entry point into XML 
"""

# Now parse a configuration file (.xml) and map the user parameters into GUI widgets
#tree = ET.parse('../config/PhysiCell_settings.xml')
tree = ET.parse(config_file)
root = tree.getroot()
uep = root.find('.//user_parameters')  # find unique entry point (uep) to user params
indent = "        "
indent2 = "          "
widgets = {"double":"FloatText", "int":"IntText", "string":"Text"}
type_cast = {"double":"float", "int":"int", "bool":"bool", "string":""}
vbox_str = "\n" + indent + "self.tab = VBox([\n"

for child in uep:
    print(child.tag, child.attrib)
    units_str = ""
    if 'units' in child.attrib.keys():
        if child.attrib['units'] != "dimensionless":
            units_str = child.attrib['units']
    if 'type' in child.attrib.keys():
#             self.therapy_activation_time = BoundedFloatText(
#            min=0., max=100000000, step=stepsize,
        full_name = "self." + child.tag
        if child.attrib['type'] not in widgets.keys():
            print("    *** Warning - Invalid type: " + child.attrib['type'])
        else:    
            # self.default_cell_speed = FloatText(
            #   description='default_cell_speed',
            #   step=0.02,
            #   style=style, layout=layout)
            user_tab_header += "\n" + indent + full_name + " = " + widgets[child.attrib['type']] + "(\n"
            user_tab_header += indent2 + "description='" + child.tag + "',\n"
            if child.attrib['type'] == "double":
                user_tab_header += indent2 + "step=0.02,\n"    # improve on this
            elif child.attrib['type'] == "int":
                user_tab_header += indent2 + "step=1,\n"
            user_tab_header += indent2 + "style=style, layout=layout)\n"

    #        self.tab = VBox([HBox([self.therapy_activation_time, Label('min')]), 
    #        vbox_str += indent2 + "HBox([" + full_name + ", Label('min')]), \n"
            vbox_str += indent2 + "HBox([" + full_name + ", Label('" + units_str + "')]), \n"

            # float, int, bool
    #        fill_gui_str += indent + full_name + ".value = float(uep.find('.//" + child.tag + "').text)\n"
            fill_gui_str += indent + full_name + ".value = " + type_cast[child.attrib['type']] + "(uep.find('.//" + child.tag + "').text)\n"
    #        self.therapy_activation_time.value = float(uep.find(".//therapy_activation_time").text)

            fill_xml_str += indent + "uep.find('.//" + child.tag + "').text = str("+ full_name + ".value)\n"
    #         uep.find(".//therapy_activation_time").text = str(self.therapy_activation_time.value)

vbox_str += indent + "])"

# Write the beginning of the Python module for the user parameters tab in the GUI
user_tab_file = "user_params.py"
print("\n ---> " + user_tab_file)
fp= open(user_tab_file, 'w')
fp.write(user_tab_header)
fp.write(vbox_str)
fp.write(fill_gui_str)
fp.write(fill_xml_str)
fp.close()