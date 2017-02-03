// **********************************************************************
//
// Copyright (c) 2003-2016 ZeroC, Inc. All rights reserved.
//
// This copy of Ice is licensed to you under the terms described in the
// ICE_LICENSE file included in this distribution.
//
// **********************************************************************

#ifndef JS_UTIL_H
#define JS_UTIL_H

#include <Slice/Parser.h>
#include <IceUtil/OutputUtil.h>

namespace Slice
{

class JsGenerator : private ::IceUtil::noncopyable
{
public:

    virtual ~JsGenerator() {};

protected:

    static bool isClassType(const TypePtr&);
    static std::string fixId(const std::string&);
    static std::string fixId(const ContainedPtr&);
    static std::string typeToString(const TypePtr&);
    static std::string getLocalScope(const std::string&, const std::string& separator = ".");
    static std::string getReference(const std::string&, const std::string&);

    static std::string getHelper(const TypePtr&);
    //
    // Generate code to marshal or unmarshal a type
    //
    void writeMarshalUnmarshalCode(::IceUtilInternal::Output&, const TypePtr&, const std::string&, bool);
    void writeOptionalMarshalUnmarshalCode(::IceUtilInternal::Output&, const TypePtr&, const std::string&, int, bool);

private:
    
    std::vector< std::string> _seenProxy;
};

}

#endif
