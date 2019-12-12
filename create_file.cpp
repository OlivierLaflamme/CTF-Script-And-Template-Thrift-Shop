#include <windows.h>
#include <stdio.h>
 
void main( )
{
   HANDLE hFile, hStream;
   DWORD dwRet;
 
   hFile = CreateFile( "sample.txt",
                    GENERIC_WRITE,
                 FILE_SHARE_WRITE,
                             NULL,
                      OPEN_ALWAYS,
                                0,
                              NUL );
   if( hFile == INVALID_HANDLE_VALUE )
      printf( "Cannot open testfile\n" );
   else
       WriteFile( hFile, "This is a Sample File", 21, &dwRet, NULL );
 
   hStream = CreateFile( "sample.txt:my_stream",
                             GENERIC_WRITE,
                          FILE_SHARE_WRITE,
                                      NULL,
                               OPEN_ALWAYS,
                                         0,
                                      NULL );
   if( hStream == INVALID_HANDLE_VALUE )
      printf( "Cannot open sample.txt:my_stream\n" );
   else
      WriteFile(hStream, "This data is hidden in the stream.Can you Read IT ???", 53, &dwRet, NULL);
}
