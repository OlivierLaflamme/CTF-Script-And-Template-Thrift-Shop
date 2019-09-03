from z3 import *

k = [
BitVec("k[0]", 8),
BitVec("k[1]", 8),
BitVec("k[2]", 8),
BitVec("k[3]", 8),
BitVec("k[4]", 8),
BitVec("k[5]", 8),
BitVec("k[6]", 8),
BitVec("k[7]", 8),
BitVec("k[8]", 8),
BitVec("k[9]", 8),
BitVec("k[10]", 8),
BitVec("k[11]", 8),
BitVec("k[12]", 8),
BitVec("k[13]", 8),
BitVec("k[14]", 8),
BitVec("k[15]", 8),
BitVec("k[16]", 8),
BitVec("k[17]", 8),
BitVec("k[18]", 8),
BitVec("k[19]", 8),
BitVec("k[20]", 8),
BitVec("k[21]", 8),
BitVec("k[22]", 8),
BitVec("k[23]", 8),
BitVec("k[24]", 8),
BitVec("k[25]", 8),
BitVec("k[26]", 8),
BitVec("k[27]", 8),
BitVec("k[28]", 8),
BitVec("k[29]", 8),
BitVec("k[30]", 8),
BitVec("k[31]", 8),
BitVec("k[32]", 8),
BitVec("k[33]", 8),
BitVec("k[34]", 8),
BitVec("k[35]", 8),
BitVec("k[36]", 8),
BitVec("k[37]", 8),
BitVec("k[38]", 8),
BitVec("k[39]", 8),
BitVec("k[40]", 8),
BitVec("k[41]", 8),
BitVec("k[42]", 8),
BitVec("k[43]", 8),
BitVec("k[44]", 8),
BitVec("k[45]", 8),
BitVec("k[46]", 8),
BitVec("k[47]", 8),
BitVec("k[48]", 8),
BitVec("k[49]", 8),
BitVec("k[50]", 8),
BitVec("k[51]", 8),
BitVec("k[52]", 8),
BitVec("k[53]", 8),
BitVec("k[54]", 8),
BitVec("k[55]", 8),
BitVec("k[56]", 8),
BitVec("k[57]", 8),
BitVec("k[58]", 8),
BitVec("k[59]", 8),
BitVec("k[60]", 8),
BitVec("k[61]", 8),
BitVec("k[62]", 8),
BitVec("k[63]", 8),
BitVec("k[64]", 8),
BitVec("k[65]", 8),
BitVec("k[66]", 8),
BitVec("k[67]", 8)
]

s = Solver()

s.add(k[0] * k[0] - 203 * k[0] == -10296) #6b8
s.add(k[2] * k[2] - 203 * k[2] == -10296)

s.add(k[1] * k[1] - 204 * k[1] == -10379) #73c
s.add(k[3] * k[3] - 204 * k[3] == -10379)

s.add(k[2] * k[2] - 204 * k[2] == -10395) #7c0
s.add(k[4]* k[4] - 204 * k[4] == -10395)

s.add(k[3] * k[3] - 216 * k[3] == -11663) #844
s.add(k[5] * k[5] - 216 * k[5] == -11663)

s.add(k[4] * k[4] - 154 * k[4] == -5145) #8c8
s.add(k[6] * k[6] - 154 * k[6] == -5145)

s.add(k[5] * k[5] - 165 * k[5] == -6104) #94c
s.add(k[7] * k[7] - 165 * k[7] == -6104)

s.add(k[6] * k[6] - 172 * k[6] == -6027) #9d0
s.add(k[8] * k[8] - 172 * k[8] == -6027)

s.add(k[7] * k[7] - 95 * k[7] == -2184) #a54
s.add(k[9] * k[9] - 95 * k[9] == -2184)

s.add(k[8] * k[8] - 210 * k[8] == -10701) #ad0
s.add(k[10] * k[10] - 210 * k[10] == -10701)

s.add(k[9] * k[9] - 87 * k[9] == -1872) #b54
s.add(k[11] * k[11] - 87 * k[11] == -1872)

s.add(k[10] * k[10] - 174 * k[10] == -7569) #bd0
s.add(k[12] * k[12] - 174 * k[12] == -7569)

s.add(k[11] * k[11] - 143 * k[11] == -4560) #c54
s.add(k[13] * k[13] - 143 * k[13] == -4560)

s.add(k[12] * k[12] - 206 * k[12] == -10353) #cd8
s.add(k[14] * k[14] - 206 * k[14] == -10353)

s.add(k[13] * k[13] - 206 * k[13] == -10545) #d5c
s.add(k[15] * k[15] - 206 * k[15] == -10545)

s.add(k[14] * k[14] - 238 * k[14] == -14161) #de0
s.add(k[16] * k[16] - 238 * k[16] == -14161)

s.add(k[15] * k[15] - 206 * k[15] == -10545) #e64
s.add(k[17] * k[17] - 206 * k[17] == -10545)

s.add(k[16] * k[16] - 238 * k[16] == -14161) #ee8
s.add(k[18] * k[18] - 238 * k[18] == -14161)

s.add(k[17] * k[17] - 143 * k[17] == -4560) #f6c
s.add(k[19] * k[19] - 143 * k[19] == -4560)

s.add(k[18] * k[18] - 238 * k[18] == -14161) #ff0
s.add(k[20] * k[20] - 238 * k[20] == -14161)

s.add(k[19] * k[19] - 143 * k[19] == -4560) #1074
s.add(k[21] * k[21] - 143 * k[21] == -4560)

s.add(k[20] * k[20] - 206 * k[20] == -10353) #10f8
s.add(k[22] * k[22] - 206 * k[22] == -10353)

s.add(k[21] * k[21] - 206 * k[21] == -10545) #117c
s.add(k[23] * k[23] - 206 * k[23] == -10545)

s.add(k[22] * k[22] - 174 * k[22] == -7569) #1200
s.add(k[24] * k[24] - 174 * k[24] == -7569)

s.add(k[23] * k[23] - 206 * k[23] == -10545) #1284
s.add(k[25] * k[25] - 206 * k[25] == -10545)

s.add(k[24] * k[24] - 208 * k[24] == -10527) #1308
s.add(k[26] * k[26] - 208 * k[26] == -10527)

s.add(k[25] * k[25] - 143 * k[25] == -4560) #138c
s.add(k[27] * k[27] - 143 * k[27] == -4560)

s.add(k[26] * k[26] - 238 * k[26] == -14157) #1410
s.add(k[28] * k[28] - 238 * k[28] == -14157)

s.add(k[27] * k[27] - 143 * k[27] == -4560) #1494
s.add(k[29] * k[29] - 143 * k[29] == -4560)

s.add(k[28] * k[28] - 221 * k[28] == -12168) #1518
s.add(k[30] * k[30] - 221 * k[30] == -12168)

s.add(k[29] * k[29] - 147 * k[29] == -4940) #159c
s.add(k[31] * k[31] - 147 * k[31] == -4940)

s.add(k[30] * k[30] - 222 * k[30] == -12272) #1620
s.add(k[32] * k[32] - 222 * k[32] == -12272)

s.add(k[31] * k[31] - 103 * k[31] == -2652) #16a4
s.add(k[33] * k[33] - 103 * k[33] == -2652)

s.add(k[32] * k[32] - 213 * k[32] == -11210) #1720
s.add(k[34] * k[34] - 213 * k[34] == -11210)

s.add(k[33] * k[33] - 160 * k[33] == -5559) #17a4
s.add(k[35] * k[35] - 160 * k[35] == -5559)

s.add(k[34] * k[34] - 147 * k[34] == -4940) #1828
s.add(k[36] * k[36] - 147 * k[36] == -4940)

s.add(k[35] * k[35] - 225 * k[35] == -12644) #18ac
s.add(k[37] * k[37] - 225 * k[37] == -12644)

s.add(k[36] * k[36] - 156 * k[36] == -5408) #1930
s.add(k[38] * k[38] - 156 * k[38] == -5408)

s.add(k[37] * k[37] - 211 * k[37] == -11020) #19b4
s.add(k[39] * k[39] - 211 * k[39] == -11020)

s.add(k[38] * k[38] - 219 * k[38] == -11960) #1a38
s.add(k[40] * k[40] - 219 * k[40] == -11960)

s.add(k[39] * k[39] - 202 * k[39] == -10165) #1abc
s.add(k[41] * k[41] - 202 * k[41] == -10165)

s.add(k[40] * k[40] - 164 * k[40] == -5635) #1b40
s.add(k[42] * k[42] - 164 * k[42] == -5635)

s.add(k[41] * k[41] - 215 * k[41] == -11556) #1bc4
s.add(k[43] * k[43] - 215 * k[43] == -11556)

s.add(k[42] * k[42] - 157 * k[42] == -5292) #1c48
s.add(k[44] * k[44] - 157 * k[44] == -5292)

s.add(k[43] * k[43] - 161 * k[43] == -5724) #1ccc
s.add(k[45] * k[45] - 161 * k[45] == -5724)

s.add(k[44] * k[44] - 203 * k[44] == -10260) #1d50
s.add(k[46] * k[46] - 203 * k[46] == -10260)

s.add(k[45] * k[45] - 140 * k[45] == -4611) #1dd4
s.add(k[47] * k[47] - 140 * k[47] == -4611)

s.add(k[46] * k[46] - 143 * k[46] == -4560) #1e58
s.add(k[48] * k[48] - 143 * k[48] == -4560)

s.add(k[47] * k[47] - 198 * k[47] == -9657) #1edc
s.add(k[49] * k[49] - 198 * k[49] == -9657)

s.add(k[48] * k[48] - 135 * k[48] == -4176) #1f60
s.add(k[50] * k[50] - 135 * k[50] == -4176)

s.add(k[49] * k[49] - 206 * k[49] == -10545) #1fe4
s.add(k[51] * k[51] - 206 * k[51] == -10545)

s.add(k[50] * k[50] - 206 * k[50] == -10353) #2068
s.add(k[52] * k[52] - 206 * k[52] == -10353)

s.add(k[51] * k[51] - 143 * k[51] == -4560) #20ec
s.add(k[53] * k[53] - 143 * k[53] == -4560)

s.add(k[52] * k[52] - 230 * k[52] == -13209) #2170
s.add(k[54] * k[54] - 230 * k[54] == -13209)

s.add(k[53] * k[53] - 167 * k[53] == -5712) #21f4
s.add(k[55] * k[55] - 167 * k[55] == -5712)

s.add(k[54] * k[54] - 206 * k[54] == -10545) #2278
s.add(k[56] * k[56] - 206 * k[56] == -10545)

s.add(k[55] * k[55] - 238 * k[55] == -14161) #22fc
s.add(k[57] * k[57] - 238 * k[57] == -14161)

s.add(k[56] * k[56] - 206 * k[56] == -10545) #2380
s.add(k[58] * k[58] - 206 * k[58] == -10545)

s.add(k[57] * k[57] - 167 * k[57] == -5712) #2404
s.add(k[59] * k[59] - 167 * k[59] == -5712)

s.add(k[58] * k[58] - 230 * k[58] == -13209) #2488
s.add(k[60] * k[60] - 230 * k[60] == -13209)

s.add(k[59] * k[59] - 143 * k[59] == -4560) #250c
s.add(k[61] * k[61] - 143 * k[61] == -4560)

s.add(k[60] * k[60] - 206 * k[60] == -10353) #2590
s.add(k[62] * k[62] - 206 * k[62] == -10353)

s.add(k[61] * k[61] - 206 * k[61] == -10545) #2614
s.add(k[63] * k[63] - 206 * k[63] == -10545)

s.add(k[62] * k[62] - 135 * k[62] == -4176) #2698
s.add(k[64] * k[64] - 135 * k[64] == -4176)

s.add(k[63] * k[63] - 198 * k[63] == -9657) #271c
s.add(k[65] * k[65] - 198 * k[65] == -9657)

s.add(k[64] * k[64] - 87 * k[64] == -1872) #27a0
s.add(k[66] * k[66] - 87 * k[66] == -1872)

s.add(k[65] * k[65] - 212 * k[65] == -10875) #281c
s.add(k[67] * k[67] - 212 * k[67] == -10875)

for i in range(1,68):
    s.add(k[i] >= 21)
    s.add(And(k[i] != 91, k[i] != 92, k[i] != 93, k[i] != 94))

for i in range(10,65):
    s.add(k[i] != ord('\''))
    s.add(k[i] != ord('/'))
    s.add(k[i] != ord('?'))

s.add(k[0]==ord('h'))
s.add(k[1]==ord('a'))
s.add(k[2]==ord('c'))
s.add(k[3]==ord('k'))
s.add(k[4]==ord('i'))
s.add(k[5]==ord('m'))
s.add(k[6]==ord('1'))
s.add(k[7]==ord('8'))
s.add(k[8]==ord('{'))
s.add(k[9]==ord("'"))
s.add(k[66]==ord("'"))
s.add(k[67]==ord('}'))

'''
hackim18{'0G_GG_G_G_GW_y0u_h4v3_m4th_sk1ll5_W0OW_70OwOwo0W_Wo0W'}
hackim18{'07_g7_G__gW_y_u_h4v3_m4th_sk1ll5_W0oW_0Ow_wO0w_WO0W0'}
hackim18{'0__g_70g_goW_y0u_h4v3_m4th_sk1ll5_W0OW_W0OwowO0_WO0W'}
hackim18{'W07_w_g_70w_g_W_y0u_h4v3_m4th_sk1ll5_W0OW_W0owwo07_Wo0W'}
hackim18{'W07_7_g_70w_g_W_y0u_h4v3_m4th_sk1ll5_W0OW_W0owwo07_Wo0W'}
hackim18{'W07_Gg_70w_goW_y0u_h4v3_m4th_sk1ll5_W0OW_W0owwo07_Wo0W'}
hackim18{'W07_gg_70w_goW_y0u_h4v3_m4th_sk1ll5_W0OW_W0owwo07_Wo0W'}
'''

while s.check() == sat:
    m = s.model()
    print (
    str("%.8x"%(m[k[0]].as_long())).decode("hex") +
    str("%.8x"%(m[k[1]].as_long())).decode("hex") +
    str("%.8x"%(m[k[2]].as_long())).decode("hex") +
    str("%.8x"%(m[k[3]].as_long())).decode("hex") +
    str("%.8x"%(m[k[4]].as_long())).decode("hex") +
    str("%.8x"%(m[k[5]].as_long())).decode("hex") +
    str("%.8x"%(m[k[6]].as_long())).decode("hex") +
    str("%.8x"%(m[k[7]].as_long())).decode("hex") +
    str("%.8x"%(m[k[8]].as_long())).decode("hex") +
    str("%.8x"%(m[k[9]].as_long())).decode("hex") +
    str("%.8x"%(m[k[10]].as_long())).decode("hex") +
    str("%.8x"%(m[k[11]].as_long())).decode("hex") +
    str("%.8x"%(m[k[12]].as_long())).decode("hex") +
    str("%.8x"%(m[k[13]].as_long())).decode("hex") +
    str("%.8x"%(m[k[14]].as_long())).decode("hex") +
    str("%.8x"%(m[k[15]].as_long())).decode("hex") +
    str("%.8x"%(m[k[16]].as_long())).decode("hex") +
    str("%.8x"%(m[k[17]].as_long())).decode("hex") +
    str("%.8x"%(m[k[18]].as_long())).decode("hex") +
    str("%.8x"%(m[k[19]].as_long())).decode("hex") +
    str("%.8x"%(m[k[20]].as_long())).decode("hex") +
    str("%.8x"%(m[k[21]].as_long())).decode("hex") +
    str("%.8x"%(m[k[22]].as_long())).decode("hex") +
    str("%.8x"%(m[k[23]].as_long())).decode("hex") +
    str("%.8x"%(m[k[24]].as_long())).decode("hex") +
    str("%.8x"%(m[k[25]].as_long())).decode("hex") +
    str("%.8x"%(m[k[26]].as_long())).decode("hex") +
    str("%.8x"%(m[k[27]].as_long())).decode("hex") +
    str("%.8x"%(m[k[28]].as_long())).decode("hex") +
    str("%.8x"%(m[k[29]].as_long())).decode("hex") +
    str("%.8x"%(m[k[30]].as_long())).decode("hex") +
    str("%.8x"%(m[k[31]].as_long())).decode("hex") +
    str("%.8x"%(m[k[32]].as_long())).decode("hex") +
    str("%.8x"%(m[k[33]].as_long())).decode("hex") +
    str("%.8x"%(m[k[34]].as_long())).decode("hex") +
    str("%.8x"%(m[k[35]].as_long())).decode("hex") +
    str("%.8x"%(m[k[36]].as_long())).decode("hex") +
    str("%.8x"%(m[k[37]].as_long())).decode("hex") +
    str("%.8x"%(m[k[38]].as_long())).decode("hex") +
    str("%.8x"%(m[k[39]].as_long())).decode("hex") +
    str("%.8x"%(m[k[40]].as_long())).decode("hex") +
    str("%.8x"%(m[k[41]].as_long())).decode("hex") +
    str("%.8x"%(m[k[42]].as_long())).decode("hex") +
    str("%.8x"%(m[k[43]].as_long())).decode("hex") +
    str("%.8x"%(m[k[44]].as_long())).decode("hex") +
    str("%.8x"%(m[k[45]].as_long())).decode("hex") +
    str("%.8x"%(m[k[46]].as_long())).decode("hex") +
    str("%.8x"%(m[k[47]].as_long())).decode("hex") +
    str("%.8x"%(m[k[48]].as_long())).decode("hex") +
    str("%.8x"%(m[k[49]].as_long())).decode("hex") +
    str("%.8x"%(m[k[50]].as_long())).decode("hex") +
    str("%.8x"%(m[k[51]].as_long())).decode("hex") +
    str("%.8x"%(m[k[52]].as_long())).decode("hex") +
    str("%.8x"%(m[k[53]].as_long())).decode("hex") +
    str("%.8x"%(m[k[54]].as_long())).decode("hex") +
    str("%.8x"%(m[k[55]].as_long())).decode("hex") +
    str("%.8x"%(m[k[56]].as_long())).decode("hex") +
    str("%.8x"%(m[k[57]].as_long())).decode("hex") +
    str("%.8x"%(m[k[58]].as_long())).decode("hex") +
    str("%.8x"%(m[k[59]].as_long())).decode("hex") +
    str("%.8x"%(m[k[60]].as_long())).decode("hex") +
    str("%.8x"%(m[k[61]].as_long())).decode("hex") +
    str("%.8x"%(m[k[62]].as_long())).decode("hex") +
    str("%.8x"%(m[k[63]].as_long())).decode("hex") +
    str("%.8x"%(m[k[64]].as_long())).decode("hex") +
    str("%.8x"%(m[k[65]].as_long())).decode("hex") +
    str("%.8x"%(m[k[66]].as_long())).decode("hex") +
    str("%.8x"%(m[k[67]].as_long())).decode("hex"))

    s.add(Or(k[0] != s.model()[k[0]],
    k[1] != s.model()[k[1]],
    k[2] != s.model()[k[2]],
    k[3] != s.model()[k[3]],
    k[4] != s.model()[k[4]],
    k[5] != s.model()[k[5]],
    k[6] != s.model()[k[6]],
    k[7] != s.model()[k[7]],
    k[8] != s.model()[k[8]],
    k[9] != s.model()[k[9]],
    k[10] != s.model()[k[10]],
    k[11] != s.model()[k[11]],
    k[12] != s.model()[k[12]],
    k[13] != s.model()[k[13]],
    k[14] != s.model()[k[14]],
    k[15] != s.model()[k[15]],
    k[16] != s.model()[k[16]],
    k[17] != s.model()[k[17]],
    k[18] != s.model()[k[18]],
    k[19] != s.model()[k[19]],
    k[20] != s.model()[k[20]],
    k[21] != s.model()[k[21]],
    k[22] != s.model()[k[22]],
    k[23] != s.model()[k[23]],
    k[24] != s.model()[k[24]],
    k[25] != s.model()[k[25]],
    k[26] != s.model()[k[26]],
    k[27] != s.model()[k[27]],
    k[28] != s.model()[k[28]],
    k[29] != s.model()[k[29]],
    k[30] != s.model()[k[30]],
    k[31] != s.model()[k[31]],
    k[32] != s.model()[k[32]],
    k[33] != s.model()[k[33]],
    k[34] != s.model()[k[34]],
    k[35] != s.model()[k[35]],
    k[36] != s.model()[k[36]],
    k[37] != s.model()[k[37]],
    k[38] != s.model()[k[38]],
    k[39] != s.model()[k[39]],
    k[40] != s.model()[k[40]],
    k[41] != s.model()[k[41]],
    k[42] != s.model()[k[42]],
    k[43] != s.model()[k[43]],
    k[44] != s.model()[k[44]],
    k[45] != s.model()[k[45]],
    k[46] != s.model()[k[46]],
    k[47] != s.model()[k[47]],
    k[48] != s.model()[k[48]],
    k[49] != s.model()[k[49]],
    k[50] != s.model()[k[50]],
    k[51] != s.model()[k[51]],
    k[52] != s.model()[k[52]],
    k[53] != s.model()[k[53]],
    k[54] != s.model()[k[54]],
    k[55] != s.model()[k[55]],
    k[56] != s.model()[k[56]],
    k[57] != s.model()[k[57]],
    k[58] != s.model()[k[58]],
    k[59] != s.model()[k[59]],
    k[60] != s.model()[k[60]],
    k[61] != s.model()[k[61]],
    k[62] != s.model()[k[62]],
    k[63] != s.model()[k[63]],
    k[64] != s.model()[k[64]],
    k[65] != s.model()[k[65]],
    k[66] != s.model()[k[66]],
    k[67] != s.model()[k[67]]))
