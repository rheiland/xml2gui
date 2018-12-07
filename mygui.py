# Rf  https://www.python.org/dev/peps/pep-0008/
import ipywidgets as widgets
import xml.etree.ElementTree as ET  # https://docs.python.org/2/library/xml.etree.elementtree.html
import os
import glob
import shutil
import datetime
from pathlib import Path
from config import ConfigTab
#from cells import CellsTab
from user_params import UserTab
from svg import SVGTab
from substrates import SubstrateTab

# join_our_list = "(Join/ask questions at https://groups.google.com/forum/#!forum/physicell-users)\n"

debug_view = widgets.Output(layout={'border': '1px solid black'})

constWidth = '180px'
tab_height = '500px'
tab_layout = widgets.Layout(width='950px',   # border='2px solid black',
                            height=tab_height, overflow_y='scroll',)

# create the tabs, but don't display yet
config_tab = ConfigTab()
#cells = CellsTab()
user_tab = UserTab()

#full_filename = os.path.abspath('../config/PhysiCell_settings.xml')
full_xml_filename = os.path.abspath('myconfig.xml')
#print('full_xml_filename=',full_xml_filename)

tree = ET.parse(full_xml_filename)  # this file cannot be overwritten; part of tool distro
xml_root = tree.getroot()
svg = SVGTab()
sub = SubstrateTab()

#nanoHUB_flag = "home/nanohub" in os.environ['HOME']  # True/False (running on nanoHUB or not)
nanoHUB_flag = False

def read_config_cb(_b):
    with debug_view:
        print("read_config", read_config.value)
        # e.g.  "DEFAULT" -> read_config /Users/heiland/dev/pc4nanobio/data/nanobio_settings.xml
        #       "<time-stamp>" -> read_config /Users/heiland/.cache/pc4nanobio/pc4nanobio/59c60c0a402e4089b71b140689075f0b
        #       "t360.xml" -> read_config /Users/heiland/.local/share/pc4nanobio/t360.xml

    if read_config.value is None:  #rwh: happens when a Run just finishes and we update pulldown with the new cache dir??
        return

    if os.path.isdir(read_config.value):
        is_dir = True
#        config_file = os.path.join(read_config.value, 'config.xml')
        config_file = os.path.join(read_config.value, full_xml_filename)
    else:
        is_dir = False
        config_file = read_config.value

    fill_gui_params(config_file)  #rwh: should verify file exists!
    
    # update visualization tabs
    if is_dir:
        svg.update(read_config.value)
        sub.update(read_config.value)
    else:  # may want to distinguish "DEFAULT" from other saved .xml config files
        svg.update('')
        sub.update('')


def write_config_file(name):
    # Read in the default xml config file, just to get a valid 'root' to populate a new one
#    full_xml_filename = os.path.abspath('config.xml')
#    full_xml_filename = os.path.abspath(full_xml_filename)
    tree = ET.parse(full_xml_filename)  # this file cannot be overwritten; part of tool distro
    xml_root = tree.getroot()
    config_tab.fill_xml(xml_root)
    user_tab.fill_xml(xml_root)
    tree.write(name)

def get_config_files():
#    cf = {'DEFAULT': os.path.abspath('data/nanobio_settings.xml')}
#    cf = {'DEFAULT': os.path.abspath('config.xml')}
    cf = {'DEFAULT': full_xml_filename}
    dirname = os.path.expanduser('~/.local/share/pc4nanobio')
    try:
        os.makedirs(dirname)
    except:
        pass
    files = glob.glob("%s/*.xml" % dirname)
    # dict.update() will append any new (key,value) pairs
    cf.update(dict(zip(list(map(os.path.basename, files)), files)))

    if nanoHUB_flag:
        full_path = os.path.expanduser("~/data/results/.submit_cache/pc4nanobio")
    else:
        # local cache
        try:
            cachedir = os.environ['CACHEDIR']
            full_path = os.path.join(cachedir, "pc4nanobio")
        except:
            print("Exception in get_config_files")
            return cf

    dirs = [os.path.join(full_path, f) for f in os.listdir(full_path) if f != '.cache_table']
    with debug_view:
        print(dirs)

    # Get a list of sorted dirs, according to creation timestamp (newest -> oldest)
    sorted_dirs = sorted(dirs, key=os.path.getctime, reverse=True)
    with debug_view:
        print(sorted_dirs)
    sorted_dirs_dates = [str(datetime.datetime.fromtimestamp(os.path.getctime(x))) for x in sorted_dirs]
    cached_file_dict = dict(zip(sorted_dirs_dates, sorted_dirs))
    cf.update(cached_file_dict)
    with debug_view:
        print(cf)
    return cf

def fill_gui_params(config_file):
    tree = ET.parse(config_file)
    xml_root = tree.getroot()
    config_tab.fill_gui(xml_root)
    user_tab.fill_gui(xml_root)
    # cells.fill_gui(xml_root)

def update_plot_frames():
    max_frames = config_tab.get_num_svg_frames()
    svg.update_max_frames_expected(max_frames)

    max_frames = config_tab.get_num_substrate_frames()
    sub.update_max_frames_expected(max_frames)

def run_button_cb(s):
    with debug_view:
        print('run_sim_func')

#    new_config_file = "config.xml"
    new_config_file = full_xml_filename
    write_config_file(new_config_file)

    update_plot_frames()
#    read_config.index = 0   # reset Dropdown 'Load Config' to 'DEFAULT' when Run interactively
#    s.run(run_name, "--local ../bin/pc-nb config.xml")
#    os.system("../cancer_biorobots ../config/PhysiCell_settings.xml &")
    # cmd_str = "./myproj " + full_xml_filename + " &"
    # os.system(cmd_str)

run_button = widgets.Button(
#    description='Run',
    description='Write',
    button_style='success',  # 'success', 'info', 'warning', 'danger' or ''
    tooltip='Run simulation',
)
run_button.on_click(run_button_cb)

#titles = ['Basics', 'Substrates', 'Custom', 'Cell Plots', 'Substrate Plots']
titles = ['Basics', 'User Params', 'Cell Plots', 'Substrate Plots']
#tabs = widgets.Tab(children=[config_tab.tab, cells.tab, custom.tab, svg.tab, sub.tab],
tabs = widgets.Tab(children=[config_tab.tab, user_tab.tab, svg.tab, sub.tab],
                   _titles={i: t for i, t in enumerate(titles)},
                   layout=tab_layout)

#gui = widgets.VBox(children=[read_config, tabs, write_config_row, run_button.w])
gui = widgets.VBox(children=[tabs, run_button])
#fill_gui_params(read_config.options['DEFAULT'])
#fill_gui_params("../config/PhysiCell_settings.xml")
fill_gui_params(full_xml_filename)

# pass in (relative) directory where output data is located
#svg.update(read_config.value)
output_dir = "output"
svg.update(output_dir)
sub.update_dropdown_fields(output_dir)
sub.update(output_dir)
