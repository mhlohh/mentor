import os 
import shutil
import datetime
import schedule
import time

source_dir = "/Users/muhsilnr/Desktop"
desitnation_dir = "/Users/muhsilnr/codespace/mentor/internship/backup "

def copy_folder_to_dierctory(source,dest):
    today = datetime.date.today()
    dest_dir = os.path.join(dest,str(today))
    
    try:
        shutil.copytree(source,dest_dir)
        print(f"Folder copied to:{dest_dir}")
    except FileExistsError:
        print(f"Folder already exist in {dest}")

schedule.every().day.at("18:55").do(lambda: copy_folder_to_dierctory(source_dir,desitnation_dir))

while True:
    schedule.run_pending()
    time.sleep(60)