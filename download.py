import re
from pytube import YouTube


from pytube import YouTube

def get_video_description(video_id):
    """Get video description for the given YouTube video id"""
    url = f'https://www.youtube.com/watch?v={video_id}'
    yt = YouTube(url)
    description = yt.description.strip()
    return description



def download_video(url):
    """Download YouTube video from the given URL"""
    yt = YouTube(url)
    video = yt.streams.get_highest_resolution()
    title = re.sub(r'[^\w\s]', '', yt.title)
    video_file = video.download(output_path='.', filename=title + '.mp4')
    description = get_video_description(yt.video_id)
    with open(f'{title}.txt', 'w', encoding='utf-8') as f:
        f.write(description)
    return video_file



if __name__ == '__main__':
    with open('download_list.txt', 'r') as f:
        urls = f.read().splitlines()

    for url in urls:
        try:
            video_file = download_video(url)
            print(f'Successfully downloaded {video_file}')
        except Exception as e:
            print(f'Error while downloading {url}: {e}')
