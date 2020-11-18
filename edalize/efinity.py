import logging
import os.path
import os
import platform
import subprocess
import re
import xml.etree.ElementTree as ET
from functools import partial
from edalize.edatool import Edatool

logger = logging.getLogger(__name__)

class Efinity(Edatool):
    """ Initial setup of the class

    This calls the parent constructor
    """
     def __init__(self, edam=None, work_root=None, eda_api=None):
        if not edam:
            edam = eda_api

        super(Efinity, self).__init__(edam, work_root)


    """ Configuration is the first phase of the build
    """
    def configure_main(self):
        pass

    def src_file_filter(self, f):
        pass
