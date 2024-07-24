import instaloader
import os
import glob

def InstagramDownloader(url):
    loader = instaloader.Instaloader()
    shortcode = url.split('/')[-2]
    post = instaloader.Post.from_shortcode(loader.context, shortcode)
    loader.download_post(post, post.owner_username)
    patter = os.path.join(post.owner_username, "*.txt")
    video = os.path.join(post.owner_username, "*.mp4")
    txt_file = glob.glob(patter)
    video_file = glob.glob(video)
    return [txt_file[0], video_file[0], post.owner_username]

video = InstagramDownloader('https://www.instagram.com/p/C9FpLIssdFd/?utm_source=ig_web_copy_link')

print(video)