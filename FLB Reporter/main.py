from openpyxl import load_workbook
import pandas as pd
from os.path import isfile, join
from os import listdir
def create_report():
    #create a list of DFs that contain each sites' attendance log
    log_files = get_files_from_dir('Logs')
    logs = []
    for log in log_files:
        logs.append(pd.read_csv(log))
        
    #create a DF with registration data
    reg_file = get_files_from_dir('Reg_Data')[0]
        
    #create a excel_FLB object
    #for each attend_DF:
        #new_enroll = Filter reg_df on names from attend_DF
        #reformat to match formatting of FLB report
        #Add names and enroll_data to excel_FLB.sheet('Enrollment')
        #parse data from attendance log to add ones and zeros to each month

def get_files_from_dir(dir):
    file_list = [f for f in listdir(dir) if isfile(join(dir, f))]
    return file_list

if __name__ == '__main__':
    create_report()
