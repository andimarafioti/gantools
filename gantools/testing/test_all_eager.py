
if __name__ == '__main__':
    import sys, os
    import shutil
    import tensorflow as tf
    sys.path.insert(0, os.path.join(os.path.dirname(__file__),'../../'))
    os.environ["CUDA_VISIBLE_DEVICES"] = ""
    tf.enable_eager_execution()



import unittest

from gantools.testing import test_patch2img
from gantools.testing import test_patch2img


loader = unittest.TestLoader()

suites = []
suites.append(loader.loadTestsFromModule(test_patch2img))
suites.append(loader.loadTestsFromModule(test_patch2img))

suite = unittest.TestSuite(suites)


def run():  # pragma: no cover
    unittest.TextTestRunner(verbosity=2).run(suite)

def saferm(path):
    if os.path.isdir(path):
        shutil.rmtree(path)
        
def clean():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    saferm(os.path.join(dir_path,'checkpoints'))
    saferm(os.path.join(dir_path,'__pycache__'))

if __name__ == '__main__':  # pragma: no cover
    os.environ["CUDA_VISIBLE_DEVICES"]=""

    run()
    clean()
    
    