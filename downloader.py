import instaloader
import os
import glob

def InstagramDownloader(url):
    L = instaloader.Instaloader()
    post_url = url
    shortcode = post_url.split('/')[-2]
    post = instaloader.Post.from_shortcode(L.context, shortcode)
    L.download_post(post, target=post.owner_username)
    pattern = os.path.join(post.owner_username, '*.txt')
    video = os.path.join(post.owner_username, '*mp4')
    txt_file = glob.glob(pattern)
    video_file = glob.glob(video)
    return [txt_file[0], video_file, post.owner_username]

video = InstagramDownloader("https://www.instagram.com/reel/C9zZgMmuMkS/?utm_source=ig_web_copy_link")

print(video[0])

os.system(f"start {video[1][0]}")