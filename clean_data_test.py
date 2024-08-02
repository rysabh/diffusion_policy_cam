import math
import numpy as np
import pandas as pd
import re
import os
import matplotlib.pyplot as plt
# from scipy.spatial.transform import Rotation
from matplotlib.backends.backend_pdf import PdfPages
import submodules.robomath as rm
import submodules.robomath_addon as rma
import submodules.motive_file_cleaner as mfc
import warnings 
warnings.filterwarnings("ignore")

print("..........")

# dir_path = '/home/cam/Documents/diffusion_policy_cam/diffusion_pipline/data_chisel_task/raw_traj/'
# save_path = '/home/cam/Documents/diffusion_policy_cam/diffusion_pipline/data_chisel_task/cleaned_traj/'

# for file in os.listdir(dir_path):
#     if file.endswith(".csv"):
#         path = os.path.join(dir_path, file)
#         # print(path)
#         mfc.motive_chizel_task_cleaner(
#             csv_path = path, save_path=save_path
#         )

cross_ref_limit = 3
Body_type = 'rb'
tolerance_sheet = [0.02, 0.02, 0.02]
tolerance_gripper = [0.005, 0.06, 0.005]

_params = {
    'RigidBody': {'len':7,
                'dof': ['X', 'Y', 'Z', 'w', 'x', 'y', 'z']},
    'Marker': {'len':3,
                'dof': ['X', 'Y', 'Z']}
}


Marker_OI = ['A1', 'A2', 'A3', 'A4', 'A5', 'B1', 'B2', 'B3', 'B4', 'B5', 'C1', 'C2', 'C3', 'C4', 'C5', 'D1', 'D2', 'D3', 'D4', 'D5', 'E1', 'E2', 'E3', 'E4', 'E5']
gripper_marker_name = ['GS']
RigidBody_OI = ['battery', 'chisel', 'gripper']
REF_FRAME = 100


dir_path = '/home/cam/Documents/raj/diffusion_policy_cam/no-sync/turn_table_chisel/tilt_25/raw_traj/'
save_path = '/home/cam/Documents/raj/diffusion_policy_cam/no-sync/turn_table_chisel/tilt_25/test_cleaned/'

B_MOIs = mfc._get_marker_limit(dir_path, RigidBody_OI ,Body_type, 'battery', REF_FRAME, tolerance_sheet, Marker_OI, cross_ref_limit)
G_MOIs = mfc._get_marker_limit(dir_path, RigidBody_OI ,Body_type, 'gripper', REF_FRAME, tolerance_gripper, gripper_marker_name, cross_ref_limit)

    

dir_path = '/home/cam/Documents/raj/diffusion_policy_cam/no-sync/turn_table_chisel/tilt_25/raw_traj/'
save_path = '/home/cam/Documents/raj/diffusion_policy_cam/no-sync/turn_table_chisel/tilt_25/test_cleaned/'

for file in os.listdir(dir_path):

    csv_path = os.path.join(dir_path, file)
    save_file = re.sub(r'\.csv', '_cleaned.csv', file)
    file_path = os.path.join(save_path, save_file)

    mfc.motive_chizel_task_cleaner(csv_path=csv_path, save_path=file_path, RigidBody_OI = RigidBody_OI, Marker_OI = Marker_OI, _params = _params, REF_FRAME = REF_FRAME, B_MOIs = B_MOIs)