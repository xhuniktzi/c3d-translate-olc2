
#include <stdio.h>
#include <math.h>

double heap[524288];
double stack[524288];

double p = 0;
double h = 0;
double t0,t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12,t13,t14,t15,t16,t17,t18,t19,t20,t21,t22,t23,t24,t25,t26,t27,t28,t29,t30,t31,t32,t33,t34,t35,t36,t37,t38,t39,t40,t41,t42,t43,t44,t45,t46,t47,t48,t49,t50,t51,t52,t53,t54,t55,t56,t57,t58,t59,t60,t61,t62,t63,t64,t65,t66,t67,t68,t69,t70,t71,t72,t73,t74,t75,t76,t77,t78,t79,t80,t81,t82,t83,t84,t85,t86,t87,t88,t89,t90,t91,t92,t93,t94,t95,t96,t97,t98,t99,t100,t101,t102,t103,t104,t105,t106,t107,t108,t109,t110,t111,t112,t113,t114,t115,t116,t117,t118,t119,t120,t121,t122,t123,t124,t125,t126,t127,t128,t129,t130,t131,t132,t133,t134,t135,t136,t137,t138,t139,t140,t141,t142,t143,t144,t145,t146,t147,t148,t149,t150,t151,t152,t153,t154,t155,t156,t157,t158,t159,t160,t161,t162,t163,t164;
void sp_actualizaalturamora() {
t1 = p + 1;
t0 = stack[(int)t1];
if (t0 > 0.0) goto L3;
goto L4;
L3:
t2 = 1;
goto L5;
L4:
t2 = 0;
L5:
t4 = p + 1;
t3 = stack[(int)t4];
if (t3 < 30.0) goto L6;
goto L7;
L6:
t5 = 1;
goto L8;
L7:
t5 = 0;
L8:
if (t2 == 1) goto L2;
goto L1;
L2:
if (t5 == 1) goto L0;
goto L1;
L0:
t6 = 1;
goto L9;
L1:
t6 = 0;
L9:
if (t6 == 1) goto L10;
goto L11;
L10:
t7 = p + 2;
stack[(int)t7] = 0.0;
L11:
t9 = p + 1;
t8 = stack[(int)t9];
if (t8 >= 30.0) goto L15;
goto L16;
L15:
t10 = 1;
goto L17;
L16:
t10 = 0;
L17:
t12 = p + 1;
t11 = stack[(int)t12];
if (t11 < 60.0) goto L18;
goto L19;
L18:
t13 = 1;
goto L20;
L19:
t13 = 0;
L20:
if (t10 == 1) goto L14;
goto L13;
L14:
if (t13 == 1) goto L12;
goto L13;
L12:
t14 = 1;
goto L21;
L13:
t14 = 0;
L21:
if (t14 == 1) goto L22;
goto L23;
L22:
t15 = p + 2;
stack[(int)t15] = 1.0;
L23:
t17 = p + 1;
t16 = stack[(int)t17];
if (t16 >= 30.0) goto L27;
goto L28;
L27:
t18 = 1;
goto L29;
L28:
t18 = 0;
L29:
t20 = p + 1;
t19 = stack[(int)t20];
if (t19 < 60.0) goto L30;
goto L31;
L30:
t21 = 1;
goto L32;
L31:
t21 = 0;
L32:
if (t18 == 1) goto L26;
goto L25;
L26:
if (t21 == 1) goto L24;
goto L25;
L24:
t22 = 1;
goto L33;
L25:
t22 = 0;
L33:
if (t22 == 1) goto L34;
goto L35;
L34:
t23 = p + 2;
stack[(int)t23] = 2.0;
L35:
t25 = p + 1;
t24 = stack[(int)t25];
if (t24 >= 60.0) goto L39;
goto L40;
L39:
t26 = 1;
goto L41;
L40:
t26 = 0;
L41:
t28 = p + 1;
t27 = stack[(int)t28];
if (t27 < 90.0) goto L42;
goto L43;
L42:
t29 = 1;
goto L44;
L43:
t29 = 0;
L44:
if (t26 == 1) goto L38;
goto L37;
L38:
if (t29 == 1) goto L36;
goto L37;
L36:
t30 = 1;
goto L45;
L37:
t30 = 0;
L45:
if (t30 == 1) goto L46;
goto L47;
L46:
t31 = p + 2;
stack[(int)t31] = 3.0;
L47:
t33 = p + 1;
t32 = stack[(int)t33];
if (t32 >= 90.0) goto L51;
goto L52;
L51:
t34 = 1;
goto L53;
L52:
t34 = 0;
L53:
t36 = p + 1;
t35 = stack[(int)t36];
if (t35 < 120.0) goto L54;
goto L55;
L54:
t37 = 1;
goto L56;
L55:
t37 = 0;
L56:
if (t34 == 1) goto L50;
goto L49;
L50:
if (t37 == 1) goto L48;
goto L49;
L48:
t38 = 1;
goto L57;
L49:
t38 = 0;
L57:
if (t38 == 1) goto L58;
goto L59;
L58:
t39 = p + 2;
stack[(int)t39] = 4.0;
L59:
t41 = p + 2;
t40 = stack[(int)t41];
printf("%d", (int)t40);
printf("%c", 10);
}
void sp_calculacuota() {
t43 = p + 1;
t42 = stack[(int)t43];
if (t42 > 5000.0) goto L63;
goto L64;
L63:
t44 = 1;
goto L65;
L64:
t44 = 0;
L65:
t46 = p + 3;
t45 = stack[(int)t46];
if (t45 > 30.0) goto L66;
goto L67;
L66:
t47 = 1;
goto L68;
L67:
t47 = 0;
L68:
if (t44 == 1) goto L62;
goto L61;
L62:
if (t47 == 1) goto L60;
goto L61;
L60:
t48 = 1;
goto L69;
L61:
t48 = 0;
L69:
if (t48 == 1) goto L70;
goto L71;
L70:
t52 = p + 1;
t51 = stack[(int)t52];
t54 = p + 2;
t53 = stack[(int)t54];
t50 = t51 / t53;
t49 = t50 * 0.45;
t55 = p + 4;
stack[(int)t55] = t49;
L71:
t57 = p + 1;
t56 = stack[(int)t57];
if (t56 > 15000.0) goto L75;
goto L76;
L75:
t58 = 1;
goto L77;
L76:
t58 = 0;
L77:
t60 = p + 3;
t59 = stack[(int)t60];
if (t59 > 30.0) goto L78;
goto L79;
L78:
t61 = 1;
goto L80;
L79:
t61 = 0;
L80:
if (t58 == 1) goto L74;
goto L73;
L74:
if (t61 == 1) goto L72;
goto L73;
L72:
t62 = 1;
goto L81;
L73:
t62 = 0;
L81:
if (t62 == 1) goto L82;
goto L83;
L82:
t66 = p + 1;
t65 = stack[(int)t66];
t68 = p + 2;
t67 = stack[(int)t68];
t64 = t65 / t67;
t63 = t64 * 0.65;
t69 = p + 4;
stack[(int)t69] = t63;
L83:
t71 = p + 1;
t70 = stack[(int)t71];
if (t70 > 25000.0) goto L87;
goto L88;
L87:
t72 = 1;
goto L89;
L88:
t72 = 0;
L89:
t74 = p + 3;
t73 = stack[(int)t74];
if (t73 > 60.0) goto L90;
goto L91;
L90:
t75 = 1;
goto L92;
L91:
t75 = 0;
L92:
if (t72 == 1) goto L86;
goto L85;
L86:
if (t75 == 1) goto L84;
goto L85;
L84:
t76 = 1;
goto L93;
L85:
t76 = 0;
L93:
if (t76 == 1) goto L94;
goto L95;
L94:
t80 = p + 1;
t79 = stack[(int)t80];
t82 = p + 2;
t81 = stack[(int)t82];
t78 = t79 / t81;
t77 = t78 * 0.7;
t83 = p + 4;
stack[(int)t83] = t77;
L95:
t85 = p + 1;
t84 = stack[(int)t85];
if (t84 < 15000.0) goto L99;
goto L100;
L99:
t86 = 1;
goto L101;
L100:
t86 = 0;
L101:
t88 = p + 3;
t87 = stack[(int)t88];
if (t87 < 30.0) goto L102;
goto L103;
L102:
t89 = 1;
goto L104;
L103:
t89 = 0;
L104:
if (t86 == 1) goto L98;
goto L97;
L98:
if (t89 == 1) goto L96;
goto L97;
L96:
t90 = 1;
goto L105;
L97:
t90 = 0;
L105:
if (t90 == 1) goto L106;
goto L107;
L106:
t94 = p + 1;
t93 = stack[(int)t94];
t96 = p + 2;
t95 = stack[(int)t96];
t92 = t93 / t95;
t91 = t92 * 0.15;
t97 = p + 4;
stack[(int)t97] = t91;
L107:
t99 = p + 4;
t98 = stack[(int)t99];
if (t98 > 1000.0) goto L111;
goto L112;
L111:
t100 = 1;
goto L113;
L112:
t100 = 0;
L113:
t102 = p + 4;
t101 = stack[(int)t102];
if (t101 < 1500.0) goto L114;
goto L115;
L114:
t103 = 1;
goto L116;
L115:
t103 = 0;
L116:
if (t100 == 1) goto L110;
goto L109;
L110:
if (t103 == 1) goto L108;
goto L109;
L108:
t104 = 1;
goto L117;
L109:
t104 = 0;
L117:
if (t104 == 1) goto L118;
goto L119;
L118:
t105 = p + 5;
stack[(int)t105] = 75.0;
goto L120;
L119:
t107 = p + 4;
t106 = stack[(int)t107];
if (t106 >= 1500.0) goto L124;
goto L125;
L124:
t108 = 1;
goto L126;
L125:
t108 = 0;
L126:
t110 = p + 4;
t109 = stack[(int)t110];
if (t109 < 2000.0) goto L127;
goto L128;
L127:
t111 = 1;
goto L129;
L128:
t111 = 0;
L129:
if (t108 == 1) goto L123;
goto L122;
L123:
if (t111 == 1) goto L121;
goto L122;
L121:
t112 = 1;
goto L130;
L122:
t112 = 0;
L130:
if (t112 == 1) goto L131;
goto L132;
L131:
t113 = p + 5;
stack[(int)t113] = 125.0;
goto L133;
L132:
t115 = p + 4;
t114 = stack[(int)t115];
if (t114 > 0.0) goto L137;
goto L138;
L137:
t116 = 1;
goto L139;
L138:
t116 = 0;
L139:
t118 = p + 4;
t117 = stack[(int)t118];
if (t117 < 1000.0) goto L140;
goto L141;
L140:
t119 = 1;
goto L142;
L141:
t119 = 0;
L142:
if (t116 == 1) goto L136;
goto L135;
L136:
if (t119 == 1) goto L134;
goto L135;
L134:
t120 = 1;
goto L143;
L135:
t120 = 0;
L143:
if (t120 == 1) goto L144;
goto L145;
L144:
t121 = p + 5;
stack[(int)t121] = 25.0;
goto L146;
L145:
t123 = p + 4;
t122 = stack[(int)t123];
if (t122 >= 2000.0) goto L147;
goto L148;
L147:
t124 = 1;
goto L149;
L148:
t124 = 0;
L149:
if (t124 == 1) goto L150;
goto L151;
L150:
t125 = p + 5;
stack[(int)t125] = 150.0;
goto L152;
L151:
t126 = p + 5;
stack[(int)t126] = 0.0;
L152:
L146:
L133:
L120:
t129 = p + 4;
t128 = stack[(int)t129];
t131 = p + 5;
t130 = stack[(int)t131];
t127 = t128 - t130;
t132 = p + 4;
stack[(int)t132] = t127;
t135 = p + 4;
t134 = stack[(int)t135];
t133 = t134;
t136 = p + 0;
stack[(int)t136] = t133;
return;
}
int main() {
t137 = 0;
t138 = 4000.0;
t139 = 10.0;
t140 = 20.0;
p = p + 0;
t141 = p + 1;
stack[(int)t141] = t138;
t142 = p + 2;
stack[(int)t142] = t139;
t143 = p + 3;
stack[(int)t143] = t140;
sp_calculacuota();
t145 = p + 0;
t144 = stack[(int)t145];
p = p - 0;
printf("%f", (double)t144);
printf("%c", 10);
t146 = 0;
t147 = 10000.0;
t148 = 10.0;
t149 = 40.0;
p = p + 0;
t150 = p + 1;
stack[(int)t150] = t147;
t151 = p + 2;
stack[(int)t151] = t148;
t152 = p + 3;
stack[(int)t152] = t149;
sp_calculacuota();
t154 = p + 0;
t153 = stack[(int)t154];
p = p - 0;
printf("%f", (double)t153);
printf("%c", 10);
t155 = 0;
t156 = 1.0;
t157 = 10.0;
p = p + 0;
t158 = p + 0;
stack[(int)t158] = t156;
t159 = p + 1;
stack[(int)t159] = t157;
sp_actualizaalturamora();
p = p - 0;
t160 = 0;
t161 = 2.0;
t162 = 40.0;
p = p + 0;
t163 = p + 0;
stack[(int)t163] = t161;
t164 = p + 1;
stack[(int)t164] = t162;
sp_actualizaalturamora();
p = p - 0;

return 0;
}
