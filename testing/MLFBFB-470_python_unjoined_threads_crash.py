#
# MLFBFB-470_python_unjoined_threads_crash.py
# Mich, 2016-04-04
# Copyright (c) 2016 Datacratic Inc. All rights reserved.
#
import threading
import time
import unittest

mldb = mldb_wrapper.wrap(mldb)  # noqa


def thread_fct(*args):
    for i in range(3):
        mldb.log(i)
        time.sleep(0.5)


class PythonPluginUnjoinedThreadsTest(MldbUnitTest):  # noqa

    def test_join(self):
        t = threading.Thread(target=thread_fct)
        t.start()
        t.join()

    @unittest.skip("MLDBFB-470")
    def test_no_join(self):
        t = threading.Thread(target=thread_fct)
        t.start()


if __name__ == '__main__':
    mldb.run_tests()
