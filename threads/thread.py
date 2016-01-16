#! /usr/bin/env python3


"""
This module contains tools for retrieving, monitoring, formatting and managing managing threads.
"""


class Thread:
    """
    Plain data object used to group together a dictionary containing all posts and
    images images in a forum thread.
    """
    def __init__(self, posts: {}, images:{}, url:str):
        self._posts = posts
        self._images = images
        self._url = url

        self.set_update_time()

    def get_url(self)->str:
        return self._url

    def get_update_time(self)->int:
        return self._update_time

    def set_update_time(self):
        self._update_time = 0 #FIXME: set to now

    def get_all_posts(self, from_time = 0, to_time = 0)->{}:
        return self._posts

    def get_images(self, post: str, from_time = 0, to_time = 0)->{}:
        return self._images

    def add_image(self, image):
        self._images.append(image)

    def add_post(self, post: {}):
        self._posts.append(post)

    def get_post(self, post_id: str):
        return self._posts[post_id]

    def get_post_images(self, post_id:str)->{}:
        image_list={}
        for image_id, image in self._images.items():
            if image["post_id"]==post_id:
                image_list[image_id] = image
        return image_list


class ThreadObserver:
    """
    Observer used to monitor threads for updates and change the
    registered threads accordingly.
    """
    def __init__(self):
        self._threads = []

    def add_thread(self, thread: Thread):
        self._threads.append(thread)

    def update_threads(self):
        pass


class ThreadFactory:
    """
    Factory used to conveniently set up a thread with the necessary
    thread management tools in place.
    """
    def __init__(self):
        pass

    def getThread(self, thread_type, thread_observer:ThreadObserver)->Thread: #TODO: set thread_type to enum
        pass


class ThreadDownloader:
    """
    Downloads a thread at a given url and stores result
    in a string.
    """
    def __init__(self, url:str):
        pass

    def set_url(self, url:str):
        pass

    def get_url(self)->str:
        pass

    def get_thread(self)->str:
        pass


class ThreadFormatter:
    """
    Handles all presentation of threads in a format suitable
    for varius output channels.
    """
    def __init__(self, thread:Thread):
        self._thread = thread

    def get_irc_formatted_posts(self, from_time:str, to_time:str)->str:
        pass