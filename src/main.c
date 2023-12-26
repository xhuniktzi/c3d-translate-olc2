
#include <stdio.h>
#include <math.h>

double heap[524288];
double stack[524288];

double p = 0;
double h = 0;
double t0, t1, t2, t3, t4, t5, t6, t7, t8, t9;
int main()
{
    t0 = p + 0;
    stack[(int)t0] = 0.0;
L0:
    t2 = p + 0;
    t1 = stack[(int)t2];
    if (t1 < 10.0)
        goto L1;
    goto L2;
L1:
    t3 = 1;
    goto L3;
L2:
    t3 = 0;
L3:
    if (t3 == 0)
        goto L4;
    t5 = p + 0;
    t4 = stack[(int)t5];
    printf("%d", (int)t4);
    printf("%c", 10);
    t8 = p + 0;
    t7 = stack[(int)t8];
    t6 = t7 + 1.0;
    t9 = p + 0;
    stack[(int)t9] = t6;
    goto L0;
L4:

    return 0;
}
