#
# Copyright (c) ZeroC, Inc. All rights reserved.
#

from Util import *

class UdpTestCase(ClientServerTestCase):

    def setupServerSide(self, current):
        if current.config.android:
            self.servers = [Server(ready="McastTestAdapter")]
        else:
            self.servers = [Server(args=[i], ready="McastTestAdapter") for i in range(0, 5)]

    def setupClientSide(self, current):
        if current.config.android:
            self.clients = [Client()]
        else:
            self.clients = [Client(args=[5])]

TestSuite(__name__, [ UdpTestCase() ], multihost=False)
