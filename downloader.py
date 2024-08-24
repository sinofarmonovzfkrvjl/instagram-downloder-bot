import instaloader
import os
import glob
import re

def InstagramVideoDownloader(url):
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

def InstagramStoryDownloader(url):
    L = instaloader.Instaloader()

    story_url = ''

    # Extract the shortcode from the URL
    shortcode = re.search(r'instagram\.com/stories/[^/]+/([^/?]+)', story_url).group(1)

    # Fetch the story using the shortcode
    try:
        post = instaloader.Post.from_shortcode(L.context, shortcode)
        L.download_post(post, target='stories')
        print("Story downloaded successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

    
