    
#see these characters in almost every other CTF kind of annoying 
#Example
#聐㠃㐊㐀㐀膜舕㐀㐀㐀㐀㐀㐀㐵㐜ꕳ𓅡𔕨𓁯𓅤騭𓍰扢改饤渹朷霭收户阴氱洭椹户騳樸昲顥游湢訯㵔㜀𦌷遻𦍋遻𖡵㐋㠁㟨㐀𦸄㐃蔀㝋䠄㐀㰀爀澜坉𢜸杢㐁稀㐂礀儀𓄀陭鵳𒁷饲扳𒅥靵渭餰湤氹戲止氰椭晡户游水栭浥朵騱浣
#霹搹鹴ꍴ𒅥鱡捥鵸ꕴ詬㵔㜀𖠦賩𦈲遻𖡵㐋㠁㟨㐀𦸄㐃言𤞑𠥮䀰𧖆㹻𥣋䒎銪𢁖绐𧲕𦌄𥁹䦂瘲𦙠讕𦓕㵽𢥴駤𤔧𧺿𦮷𦋾𒇔𠒢𣍰𣹗桉𧠄抦𣶝𦔊𣖎棉㿮𒉙㥐咥謔鋌𤨮𡐸𧻩𣲔䦽𧎛恶蛎蚃𥶔䨺𤶓㗢𡟂𦼕䉲𣪧𥰡帐𠌉𤅽
#𤢓𧅃熙𤴧籋鬈䣎𢌲祙䋪𢭌𠟻𥍘𠼍䰻𣐻涩𤞴䢂𣡳䈼𢽼洉𒁠栴㰌羓慡鋩𧕉𓃱𡀩𢯧𡳓𦃠柩囎𣊇勣𤀴𥒷囧軾璉𧣚谂𨊈𥵄𨃎脜𢗨勺㗼𧇮𥹧蘚袺𣈠𧄄

# pip install base65536

import base65536

with open('FILE.txt','r') as f:
    ct = f.readline().rstrip().replace(' ','')

with open('FILE_out','wb') as f2:
    f2.write(base65536.decode(ct))
