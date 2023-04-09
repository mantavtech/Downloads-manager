import os, shutil, zipfile, rarfile, py7zr
from datetime import datetime

now = datetime.now()
year = now.strftime('%y')

#define source & target folders
source_dir = os.path.join(os.environ['userprofile'], 'Downloads')
target_folder_images = os.path.join(os.environ['userprofile'], 'Desktop', 'organised-downloads', f'{year}_images')
target_folder_videos = os.path.join(os.environ['userprofile'], 'Desktop', 'organised-downloads', f'{year}_videos')
target_folder_documents = os.path.join(os.environ['userprofile'], 'Desktop', 'organised-downloads', f'{year}_documents')
target_folder_audio = os.path.join(os.environ['userprofile'], 'Desktop', 'organised-downloads', f'{year}_audio')
target_folder_archive = os.path.join(os.environ['userprofile'], 'Desktop', 'organised-downloads', f'{year}_compressed_files')
target_folder_other = os.path.join(os.environ['userprofile'], 'Desktop', 'organised-downloads', f'{year}_other_files')
target_folder_exe = os.path.join(os.environ['userprofile'], 'Desktop', 'organised-downloads', f'{year}_exe')
target_folder_folder = os.path.join(os.environ['userprofile'], 'Desktop', 'organised-downloads', f'{year}_folder')

# Create target folders if they do not exist
for folder in [target_folder_images, target_folder_videos, target_folder_documents, target_folder_audio, target_folder_archive, target_folder_other, target_folder_exe, target_folder_folder]:
    if not os.path.exists(folder):
        os.makedirs(folder)


# Loop through the files in the source directory
file_names = os.listdir(source_dir)
for file_name in file_names:
    # folder
    file_path = os.path.join(source_dir, file_name)
    if os.path.isdir(file_path):
        shutil.move(os.path.join(source_dir, file_name), target_folder_folder)
    # Videos
    elif file_name.lower().endswith(('.mp4', '.mov', '.webm', '.mkv', '.avi', '.wmv', '.hevc', '.h265')):
        shutil.move(os.path.join(source_dir, file_name), target_folder_videos)
    # Images
    elif file_name.lower().endswith(('.jpg', '.jpeg', '.png', '.webp', '.svg', '.bmp', '.tiff', '.tif', '.raw')):
        shutil.move(os.path.join(source_dir, file_name), target_folder_images)
    # Documents
    elif file_name.lower().endswith(('.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.txt', '.rtf')):
        shutil.move(os.path.join(source_dir, file_name), target_folder_documents)
    # Archives
    elif file_name.lower().endswith(('.zip', '.rar', '.7z')):
        shutil.move(os.path.join(source_dir, file_name), target_folder_archive)
    # exe
    elif file_name.lower().endswith('.exe'):
        shutil.move(os.path.join(source_dir, file_name), target_folder_exe)

        
    # Other files
    else:
        shutil.move(os.path.join(source_dir, file_name), target_folder_other)
