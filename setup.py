#!/usr/bin/env python3
#
# Copyright 2020 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# This software is distributed under the terms of the MIT License.
#

import sys
import setuptools

from typing import Dict

if int(setuptools.__version__.split('.')[0]) < 30:
    print('A newer version of setuptools is required. The current version does not support declarative config.',
          file=sys.stderr)
    sys.exit(1)

version = {}  # type: Dict
with open('src/yukon/version.py') as fp:
    exec(fp.read(), version)

setuptools.setup(version=version['__version__'],
                 package_data={'': ['*.j2', '*.ini', '*.hpp']})