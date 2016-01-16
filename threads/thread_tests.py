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
    def test_init(self):
        ob = ThreadObserver()

        self.assertEqual([], ob._threads)

    def test_add_observer(self):
        ob = ThreadObserver()

        thread = Thread({},{}, "")
        ob.add_thread(thread)

        self.assertEqual(ob._threads[0], thread)
        self.assertEqual(len(ob._threads), 1)

    def test_update_threads(self):
        self.fail("test_update_threads: Not implemented")

class TestThreadFactory(unittest.TestCase):
    def test_init(self):
        self.fail("ThreadFactory: test_init not implemented")

    def test_get_thread(self):
        self.fail("ThreadFactory: test_get_thread not implemented")

class TestThreadDownloader(unittest.TestCase):
    pass

class TestThreadFormatter(unittest.TestCase):
    pass