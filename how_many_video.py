import os
import subprocess

# DIR_PATH = r"C:\Users\User\myvideos"
# FFPROBE_PATH = r"C:\Users\a_may\Downloads\ffmpeg-master-latest-win64-gpl\bin\ffprobe.exe"

DIR_PATH = r""
FFPROBE_PATH = r""


def get_length_of_video(filename):
    duration = subprocess.check_output(
        [FFPROBE_PATH, '-i', filename, '-show_entries', 'format=duration', '-v', 'quiet', '-of', 'csv=p=0'])
    return float(duration.strip())


def convert_seconds_to_hms(seconds):
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    seconds = seconds % 60
    return hours, minutes, seconds


if __name__ == '__main__':

    if not DIR_PATH:
        DIR_PATH = input("Введите корневую папку с видосами (пример:  C:\\Users\\myvideos)\n-> ")
    if not FFPROBE_PATH:
        FFPROBE_PATH = input(
            "Введите путь к ffprobe.exe (пример: C:\\ffmpeg-master-latest-win64-gpl\\bin\\ffprobe.exe\n-> ")

    dir_file_name_of_path = os.walk(DIR_PATH)

    total_videos = 0
    total_waste_time = 0

    for elem in dir_file_name_of_path:
        for has_vid in elem[-1]:
            if ".mp4" in has_vid:
                full_path_of_video = elem[0] + "\\" + has_vid
                get_length = get_length_of_video(full_path_of_video)
                total_waste_time += get_length
                total_videos += 1

    hours, minutes, seconds = convert_seconds_to_hms(total_waste_time)
    print(
        f'В указанной директории {total_videos} видос(-ов), общей продолжительностью {hours} часов {minutes} минут {seconds:.2f} секунд.')
