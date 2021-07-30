// gcc64 .\comfun.c -o com.exe -lole32 -luuid -loleaut32

#include <windows.h>
#include <Unknwn.h>
#include <objbase.h>
#include <stdio.h>

VOID FormatCOM(CHAR *com, CLSID *clsid) {
    WCHAR data[256];
    swprintf(data, 256, L"%hs", com);
    if(com[0] == '{') {
        if(CLSIDFromString(data, clsid) != S_OK) {
            printf("CLSIDFromString failed to resolve CLSID %s. Error %d\n", com, GetLastError());
            ExitProcess(0);
        }
    } else {
        if(CLSIDFromProgID(data, clsid) != S_OK) {
            printf("CLSIDFromProgID failed to resolve CLSID %s. Error %d\n", com, GetLastError());
            ExitProcess(0);           
        }
    }
}

int main(int argc, char **argv) {

    CLSID clsid;
    LPOLESTR os;
    HRESULT hr;
    IClassFactory *icf = NULL;
    IDispatch *id = NULL;

    FormatCOM(argv[1], &clsid);

    StringFromCLSID(&clsid, &os);
    printf("%s CLSID is %ws\n", argv[1], os);

    hr = CoInitialize(NULL);

    /*
    hr = CoGetClassObject(&clsid, CLSCTX_REMOTE_SERVER | CLSCTX_INPROC_SERVER, NULL, &IID_IClassFactory, (void **)&icf);
    if(hr != S_OK) {
            printf("CoGetClassObject failed to do something. Error %d HRESULT 0x%08x\n", GetLastError(), (unsigned int)hr);

            CoUninitialize();
            ExitProcess(0);          
    }
    */

    FARPROC DllGetClassObject = GetProcAddress(LoadLibrary("shell32.dll"), "DllGetClassObject");
    printf("DllGetClassObject is at 0x%p\n", DllGetClassObject);
    hr = DllGetClassObject(&clsid, &IID_IClassFactory, (void **)&icf);

    if(hr != S_OK) {
            printf("DllGetClassObject failed to do something. Error %d HRESULT 0x%08x\n", GetLastError(), (unsigned int)hr);

            CoUninitialize();
            ExitProcess(0);          
    }

    printf("IClassFactory 0x%p\n", icf);

    hr = icf->lpVtbl->CreateInstance(icf, NULL, &IID_IDispatch, (void **)&id);
    if(hr != S_OK) {
            printf("CreateInstance failed to do something. Error %d HRESULT 0x%08x\n", GetLastError(), (unsigned int)hr);

            CoUninitialize();
            ExitProcess(0);          
    }

    printf("IDispatch 0x%p\n", id);

    OLECHAR *member = L"ShellExecute";
    DISPID dispid = 0;

    hr = id->lpVtbl->GetIDsOfNames(id, &IID_NULL, &member, 1, LOCALE_USER_DEFAULT, &dispid);
    if(hr != S_OK) {
            printf("GetIDsOfNames failed to do something. Error %d HRESULT 0x%08x\n", GetLastError(), (unsigned int)hr);

            CoUninitialize();
            ExitProcess(0);          
    }

    printf("DISPID 0x%08x\n", dispid);

    DISPPARAMS dp;
    VARIANT args = { VT_EMPTY };
    VARIANT output = { VT_EMPTY };
    EXCEPINFO ei = { 0 };
    UINT uerror;

    CHAR *ShellExecuteArgs = argv[2];

    printf("Args For ShellExecute is %s\n", ShellExecuteArgs);
    int length = MultiByteToWideChar(CP_ACP, 0, ShellExecuteArgs, strlen(ShellExecuteArgs), 0, 0);
    printf("We need %d bytes\n", length);
    BSTR bstr = SysAllocStringLen(0, length);
    length = MultiByteToWideChar(CP_ACP, 0, ShellExecuteArgs, strlen(ShellExecuteArgs), bstr, length);

    printf("MultiByteToWideChar wrote %d\n", length);

    args.vt = VT_BSTR;
    args.bstrVal = bstr;

    dp.cArgs = 1;
    dp.rgvarg = &args;

    hr = id->lpVtbl->Invoke(id, dispid, &IID_NULL, LOCALE_USER_DEFAULT, DISPATCH_METHOD, &dp, &output, &ei, &uerror);
    if(hr != S_OK) {
            printf("Invoke failed to do something. Error %d HRESULT 0x%08x EXCEPTION %ws Exception index %d\n", GetLastError(), (unsigned int)hr, ei.bstrDescription ,uerror);

            CoUninitialize();
            ExitProcess(0);          
    }

    id->lpVtbl->Release(id);
    icf->lpVtbl->Release(icf);

    SysFreeString(bstr);
    CoUninitialize();

    return 0;
}
