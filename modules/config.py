import os
import pathlib
from modules.controls import *

def GetCMPMVS():
    # current_dir = get_from_control_reference("current_dir")
    # CMPMVS = current_dir / "Software" / "CMPMVS" / "CMPMVS.exe"
    # CMPMVS = f'/Software/CMPMVS/CMPMVS.exe'
    current_path = os.path.abspath(os.path.dirname(__file__))
    parent_dir = os.path.dirname(current_path)
    CMPMVS = os.path.join(parent_dir, "Software", "CMPMVS").replace("\\", "/")
    return CMPMVS
def GetVisualSFM():
    current_dir = get_from_control_reference("current_dir")
    # VisualSFM = current_dir / "Software" / "VisualSFM" / "VisualSFM.exe"
    VisualSFM = f'/Software/VisualSFM/VisualSFM.exe'
    return VisualSFM
def GetPrematchingSiftGPU():
    current_dir = get_from_control_reference("current_dir")
    prematchingSiftGPU = current_dir / "Software" / "CMPMVS" / "prematchingSiftGPU.exe"
    return prematchingSiftGPU