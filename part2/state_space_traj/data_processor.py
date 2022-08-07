from scipy.io.matlab import loadmat
import pandas as pd

def start_job():
    dat = loadmat("../../downloads/MasterPython_CodeAndData/stateSpaceTrajectories/ALMdata.mat")
    print(dat.keys())
    print(dat)
    #df = pd

if __name__ == "__main__":
    start_job()