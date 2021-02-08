import cx_Freeze
from cx_Freeze import *

includefiles = ['billing.ico','Login.png','software.py']
base = None
if sys.platform == "win32":
    base = "win32GUI"

shortcut_table = [
    ("DesktopShortcut", # Shortcut
     "DesktopFolder", # Directory_
     "Billing software", # Name
     "TARGETDIR", # Component_
     "[TARGETDIR]\ Billing software.exe", # Target
     None, # Arguments
     None, # Description
     None, # Hotkey
     None, # Icon
     None, # IconIndex
     None, # ShowCmd
     "TARGETDIR", # wkDir
     )
]
msi_data = {"Shortcut": shortcut_table}

#Change some default MSI options and specify the use of the above defined tables
bdist_msi_options = {'data': msi_data}
setup(
    version="0.3",
    description="Billing Software vol2",
    author="Deep Bhatt",
    name="Billing software",
    options={'build_exe': {'include_files': includefiles}, "build_msi": bdist_msi_options, },
    executables=[
          Executable(
              script="Billing_system.py",
              base=base,
              icon='billing.ico',
          )
    ]
)
