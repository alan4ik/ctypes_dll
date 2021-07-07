#include <stdio.h>
#include <stdlib.h>

#pragma warning(disable : 4996)

extern "C" {
    int print_getenv() 
    { 
        if (getenv("TEST") != NULL)
        {
            printf("get: %s\n", getenv("TEST"));
            return 101;
        }
        else
        {
            printf("NO\n");
            return 404;
        }
    }
}
