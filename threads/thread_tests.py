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
    def test_init(self):
        dl = ThreadDownloader("")
        self.assertIsInstance(dl,ThreadDownloader)
        self.assertEqual("", dl._url)

        dl = ThreadDownloader("test url")
        self.assertEqual("test url", dl._url)

    def test_set_url(self):
        dl = ThreadDownloader("test url")

        dl.set_url("new test url")
        self.assertEqual("new test url", dl._url)

    def test_get_url(self):
        dl = ThreadDownloader("")
        self.assertEqual(dl.get_url(), dl._url)

        dl._url = "new test"
        self.assertEqual(dl.get_url(), "new test")

    def test_get_thread(self):
        dl = ThreadDownloader("test url")
        self.assertRaises(dl.get_thread(),ConnectionError)

        dl = ThreadDownloader("https://a.4cdn.org/g/thread/51971506.json")
        page_content = """{"posts":[{"no":51971506,"sticky":1,"closed":1,"now":"12\/20\/15(Sun)20:03:52","name":"Anonymous","com":"The \/g\/ Wiki:<br><a href=\"http:\/\/wiki.installgentoo.com\/\">http:\/\/wiki.installgentoo.com\/<\/a><br><br>\r\n\r\n\/g\/ is for the discussion of technology and related topics.<br>\r\n\/g\/ is <b><u>NOT<\/u><\/b> your personal tech support team or personal consumer review site.<br><br>\r\nFor tech support\/issues with computers, use <a href=\"https:\/\/boards.4chan.org\/wsr\/\">\/wsr\/ - Worksafe Requests<\/a> or one of the following:<br>\r\n<a href=\"https:\/\/startpage.com\/\">https:\/\/startpage.com\/<\/a> or <a href=\"https:\/\/duckduckgo.com\">https:\/\/duckduckgo.com<\/a> (i.e., fucking google it)<br>\r\n<a href=\"https:\/\/stackexchange.com\/\">https:\/\/stackexchange.com\/<\/a><br>\r\n<a href=\"http:\/\/www.logicalincrements.com\/\">http:\/\/www.logicalincrements.com\/<\/a><br><br>\r\n\r\nYou can also search the catalog for a specific term by using:<br>\r\n<a href=\"https:\/\/boards.4chan.org\/g\/searchword\"><a href=\"https:\/\/boards.4chan.org\/g\/searchword\" target=\"_blank\">https:\/\/boards.4chan.org\/g\/searchwo<wbr>rd<\/a><\/a> or by clicking on [Search]<br><br> \r\n\r\nAlways check the catalog before creating a thread:<br><a href=\"https:\/\/boards.4chan.org\/g\/catalog\"><a href=\"\/g\/catalog\" class=\"quotelink\">&gt;&gt;&gt;\/g\/catalog<\/a><\/a><br><br>\r\n\r\nPlease check the rules before you post:<br><a href=\"https:\/\/www.4chan.org\/rules\"><\/a><br>\r\n<i>Begging for cryptocurrency is against the rules!<\/i><br><br>\r\n\r\nTo use the Code tag, book-end your body of code with: [code] and [\/code]","filename":"RMS","ext":".png","w":450,"h":399,"tn_w":250,"tn_h":221,"tim":1450659832892,"time":1450659832,"md5":"cEeDnXfLWSsu3+A\/HIZkuw==","fsize":299699,"resto":0,"capcode":"mod","semantic_url":"the-g-wiki","replies":0,"images":0,"unique_ips":1}]}"""
        self.assertEqual(dl.get_thread(), page_content)


class TestThreadFormatter(unittest.TestCase):
    def test_init(self):
        self.fail("not implemented")

    def test_get_irc_formatted_posts(self):
        self.fail("not implemented")

