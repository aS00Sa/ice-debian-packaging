# -*- coding: utf-8 -*-
# **********************************************************************
#
# Copyright (c) 2003-2018 ZeroC, Inc. All rights reserved.
#
# This copy of Ice is licensed to you under the terms described in the
# ICE_LICENSE file included in this distribution.
#
# **********************************************************************

# Enable some tracing to allow investigating test failures
traceProps = {
    "Ice.Trace.Locator" : 2,
    "Ice.Trace.Protocol" : 1
}

TestSuite(__name__, [ClientServerTestCase(traceProps=traceProps)])
