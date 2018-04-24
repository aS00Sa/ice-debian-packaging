%{
**********************************************************************

Copyright (c) 2003-2018 ZeroC, Inc. All rights reserved.

This copy of Ice is licensed to you under the terms described in the
ICE_LICENSE file included in this distribution.

**********************************************************************
%}

function client(args)
    addpath('generated');
    if ~libisloaded('ice')
        loadlibrary('ice', @iceproto)
    end

    initData = TestApp.createInitData('client', args);
    communicator = Ice.initialize(initData);
    cleanup = onCleanup(@() communicator.destroy());

    app = TestApp(communicator);
    g = AllTests.allTests(app);
    g.shutdown();

    clear('classes'); % Avoids conflicts with tests that define the same symbols.
end
