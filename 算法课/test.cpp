#include <stdio.h>
int main()
{
    int i = 1, j = 1, k = 2;
    if (j++ || k++ && i++)
    {
        printf("%d,%d,%d", i, j, k);
    }
}