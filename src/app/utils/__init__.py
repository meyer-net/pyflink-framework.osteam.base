################################################################################
#  Licensed to the Apache Software Foundation (ASF) under one
#  or more contributor license agreements.  See the NOTICE file
#  distributed with this work for additional information
#  regarding copyright ownership.  The ASF licenses this file
#  to you under the Apache License, Version 2.0 (the
#  "License"); you may not use this file except in compliance
#  with the License.  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
# limitations under the License.
################################################################################

import socket

from utils.system import Config
from utils.logger import Logger, Printer
from utils.string import String

def gen_free_port(port=5000, granularity=1):
    port = int(port)
    if port not in range(1024, 65535):
        raise Exception("input port is should be in range of 1024..65535.")
    try:
        skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        while port <= 65535:
            try:
                skt.bind(('', port))
                addr = skt.getsockname()
                return addr[1]
            except IOError:
                port += granularity
                if port > 65535:
                    raise Exception("free port not found.")
    finally:
        skt.close()

__all__ = [
    'Printer', 'Logger', 'Config', 'String'
]
