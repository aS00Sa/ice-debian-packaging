# **********************************************************************
#
# Copyright (c) 2003-2016 ZeroC, Inc. All rights reserved.
#
# This copy of Ice is licensed to you under the terms described in the
# ICE_LICENSE file included in this distribution.
#
# **********************************************************************

if not isinstance(platform, Darwin) and (isinstance(platform, Windows) or os.getuid() == 0):
    TestSuite(__name__)
