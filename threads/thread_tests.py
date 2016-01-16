import unittest
import time

from threads.thread import *

class ThreadTest(unittest.TestCase):
    def test_init(self):
        start = time.clock()
        thread = Thread({},{},"")
        end = time.clock()

        self.assertIsInstance(thread, Thread)
        self.assertLess(start, thread._update_time)
        self.assertGreater(end, thread._update_time)

        self.assertEqual({}, thread._posts)
        self.assertEqual({}, thread._images)
        self.assertEqual("", thread._url)

        posts = {1:"post1"}
        imgs = {"img1":{}}
        url = "http://example.com"
        thread = Thread(posts,imgs,url)

        self.assertEqual(posts, thread._posts)
        self.assertEqual(imgs, thread._images)
        self.assertEqual(url, thread._url)


    def test_getters(self):
        thread = Thread({},{},"")

        self.assertEqual(thread._posts, thread.get_all_posts())
        self.assertEqual(thread._images, thread.get_images())
        self.assertEqual(thread._update_time, thread.get_update_time())
        self.assertEqual(thread._url, thread.get_url())


    def test_modifiers(self):
        thread = Thread({},{},"")
        post = {1:"post1"}
        image = {"img": {}}

        thread.add_image(image)
        self.assertIn(image, thread._images)

        thread.add_post(post)
        self.assertIn(post, thread._posts)

        start = time.clock()
        thread.set_update_time()
        end = time.clock()
        self.assertLess(start, thread._update_time)
        self.assertGreater(end, thread._update_time)

class TestThreadObserver(unittest.TestCase):
    pass

class TestThreadFactory(unittest.TestCase):
    pass

class TestThreadDownloader(unittest.TestCase):
    pass

class TestThreadFormatter(unittest.TestCase):
    pass