
#include <stdio.h>
#include <math.h>

double heap[524288];
double stack[524288];

double p = 0;
double h = 0;
double t0,t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12,t13,t14,t15,t16,t17,t18,t19,t20,t21,t22,t23,t24,t25,t26,t27,t28,t29,t30,t31,t32,t33,t34,t35,t36,t37,t38,t39,t40,t41,t42,t43,t44,t45,t46,t47,t48,t49,t50,t51,t52,t53,t54,t55,t56,t57,t58,t59,t60,t61,t62,t63,t64,t65,t66,t67,t68,t69,t70,t71,t72,t73,t74,t75,t76,t77,t78,t79,t80,t81,t82,t83,t84,t85,t86,t87,t88,t89,t90,t91,t92,t93,t94,t95,t96,t97,t98,t99;
void ackermann() {
t1 = p + 1;
t0 = stack[(int)t1];
if (t0 == 0.0) goto L0;
goto L1;
L0:
t2 = 1;
goto L2;
L1:
t2 = 0;
L2:
if (t2 == 1) goto L3;
goto L4;
L3:
t6 = p + 2;
t5 = stack[(int)t6];
t4 = t5 + 1.0;
t3 = t4;
t7 = p + 0;
stack[(int)t7] = t3;
return;
L4:
t9 = p + 1;
t8 = stack[(int)t9];
if (t8 > 0.0) goto L8;
goto L9;
L8:
t10 = 1;
goto L10;
L9:
t10 = 0;
L10:
t12 = p + 2;
t11 = stack[(int)t12];
if (t11 == 0.0) goto L11;
goto L12;
L11:
t13 = 1;
goto L13;
L12:
t13 = 0;
L13:
if (t10 == 1) goto L7;
goto L6;
L7:
if (t13 == 1) goto L5;
goto L6;
L5:
t14 = 1;
goto L14;
L6:
t14 = 0;
L14:
if (t14 == 1) goto L15;
goto L16;
L15:
t16 = 3;
t20 = p + 1;
t19 = stack[(int)t20];
t18 = t19 - 1.0;
t17 = t18;
t21 = 1.0;
p = p + 3;
t22 = p + 1;
stack[(int)t22] = t17;
t23 = p + 2;
stack[(int)t23] = t21;
ackermann();
t25 = p + 0;
t24 = stack[(int)t25];
p = p - 3;
t15 = t24;
t26 = p + 0;
stack[(int)t26] = t15;
return;
L16:
t28 = p + 1;
t27 = stack[(int)t28];
if (t27 > 0.0) goto L20;
goto L21;
L20:
t29 = 1;
goto L22;
L21:
t29 = 0;
L22:
t31 = p + 2;
t30 = stack[(int)t31];
if (t30 > 0.0) goto L23;
goto L24;
L23:
t32 = 1;
goto L25;
L24:
t32 = 0;
L25:
if (t29 == 1) goto L19;
goto L18;
L19:
if (t32 == 1) goto L17;
goto L18;
L17:
t33 = 1;
goto L26;
L18:
t33 = 0;
L26:
if (t33 == 1) goto L27;
goto L28;
L27:
t35 = 3;
t39 = p + 1;
t38 = stack[(int)t39];
t37 = t38 - 1.0;
t36 = t37;
t41 = 3;
t44 = p + 1;
t43 = stack[(int)t44];
t42 = t43;
t48 = p + 2;
t47 = stack[(int)t48];
t46 = t47 - 1.0;
t45 = t46;
p = p + 3;
t49 = p + 1;
stack[(int)t49] = t42;
t50 = p + 2;
stack[(int)t50] = t45;
ackermann();
t52 = p + 0;
t51 = stack[(int)t52];
p = p - 3;
t40 = t51;
p = p + 3;
t53 = p + 1;
stack[(int)t53] = t36;
t54 = p + 2;
stack[(int)t54] = t40;
ackermann();
t56 = p + 0;
t55 = stack[(int)t56];
p = p - 3;
t34 = t55;
t57 = p + 0;
stack[(int)t57] = t34;
return;
L28:
}
int main() {
t58 = 0;
t59 = 0.0;
t60 = 0.0;
p = p + 0;
t61 = p + 1;
stack[(int)t61] = t59;
t62 = p + 2;
stack[(int)t62] = t60;
ackermann();
t64 = p + 0;
t63 = stack[(int)t64];
p = p - 0;
printf("%d", (int)t63);
printf("%c", 10);
t65 = 0;
t66 = 1.0;
t67 = 1.0;
p = p + 0;
t68 = p + 1;
stack[(int)t68] = t66;
t69 = p + 2;
stack[(int)t69] = t67;
ackermann();
t71 = p + 0;
t70 = stack[(int)t71];
p = p - 0;
printf("%d", (int)t70);
printf("%c", 10);
t72 = 0;
t73 = 2.0;
t74 = 2.0;
p = p + 0;
t75 = p + 1;
stack[(int)t75] = t73;
t76 = p + 2;
stack[(int)t76] = t74;
ackermann();
t78 = p + 0;
t77 = stack[(int)t78];
p = p - 0;
printf("%d", (int)t77);
printf("%c", 10);
t79 = 0;
t80 = 3.0;
t81 = 3.0;
p = p + 0;
t82 = p + 1;
stack[(int)t82] = t80;
t83 = p + 2;
stack[(int)t83] = t81;
ackermann();
t85 = p + 0;
t84 = stack[(int)t85];
p = p - 0;
printf("%d", (int)t84);
printf("%c", 10);
t86 = 0;
t87 = 4.0;
t88 = 0.0;
p = p + 0;
t89 = p + 1;
stack[(int)t89] = t87;
t90 = p + 2;
stack[(int)t90] = t88;
ackermann();
t92 = p + 0;
t91 = stack[(int)t92];
p = p - 0;
printf("%d", (int)t91);
printf("%c", 10);
t93 = 0;
t94 = 4.0;
t95 = 1.0;
p = p + 0;
t96 = p + 1;
stack[(int)t96] = t94;
t97 = p + 2;
stack[(int)t97] = t95;
ackermann();
t99 = p + 0;
t98 = stack[(int)t99];
p = p - 0;
printf("%d", (int)t98);
printf("%c", 10);

return 0;
}
