// **********************************************************************
//
// Copyright (c) 2003-2016 ZeroC, Inc. All rights reserved.
//
// This copy of Ice is licensed to you under the terms described in the
// ICE_LICENSE file included in this distribution.
//
// **********************************************************************

package test.Ice.slicing.exceptions;

public class AMDServer extends test.Util.Application
{
    @Override
    public int run(String[] args)
    {
        com.zeroc.Ice.ObjectAdapter adapter = communicator().createObjectAdapter("TestAdapter");
        com.zeroc.Ice.Object object = new AMDTestI();
        adapter.add(object, com.zeroc.Ice.Util.stringToIdentity("Test"));
        adapter.activate();
        return WAIT;
    }

    @Override
    protected com.zeroc.Ice.InitializationData getInitData(String[] args, java.util.List<String> rArgs)
    {
        com.zeroc.Ice.InitializationData initData = super.getInitData(args, rArgs);
        initData.properties.setProperty("Ice.Package.Test", "test.Ice.slicing.exceptions.serverAMD");
        initData.properties.setProperty("Ice.Warn.Dispatch", "0");
        initData.properties.setProperty("TestAdapter.Endpoints",
                                          getTestEndpoint(initData.properties, 0) + " -t 2000");
        return initData;
    }

    public static void main(String[] args)
    {
        AMDServer c = new AMDServer();
        int status = c.main("AMDServer", args);

        System.gc();
        System.exit(status);
    }
}
