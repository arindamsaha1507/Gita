svara = ['अ', 'आ', 'इ', 'ई', 'उ', 'ऊ', 'ऋ', ' ॠ', 'ऌ', 'ए', 'ऐ', 'ओ', 'औ']
maatraa = ['ा', 'ि', 'ी', 'ु', 'ू', 'ृ', 'ॄ',  'ॢ', 'े', 'ै', 'ो', 'ौ']

anunaasika_svara = ['अँ', 'आँ', 'इँ', 'ईँ', 'उँ', 'ऊँ', 'ऋँ', ' ॠँ', 'ऌँ', 'एँ', 'ऐँ', 'ओँ', 'औँ']

maatraa_to_svara = dict(zip(maatraa, svara[1:]))
svara_to_maatraa = dict(zip(svara[1:], maatraa))

vyanjana = ['क्', 'ख्', 'ग्', 'घ्', 'ङ्', 'च्', 'छ्', 'ज्', 'झ्', 'ञ्', 'ट्', 'ठ्', 'ड्', 'ढ्', 'ण्', 'त्', 'थ्', 'द्', 'ध्', 'न्', 'प्', 'फ्', 'ब्', 'भ्', 'म्', 'य्', 'र्', 'ल्', 'व्', 'श्', 'ष्', 'स्', 'ह्']
vyanjana_with_akaara = ['क', 'ख', 'ग', 'घ', 'ङ', 'च', 'छ', 'ज', 'झ', 'ञ', 'ट', 'ठ', 'ड', 'ढ', 'ण', 'त', 'थ', 'द', 'ध', 'न', 'प', 'फ', 'ब', 'भ', 'म', 'य', 'र', 'ल', 'व', 'श', 'ष', 'स', 'ह']

avasaana = [' ', '।', '॥']

maaheshwar_suutra = ['अ', 'इ', 'उ', 'ण्', 'ऋ', 'ऌ', 'क्', 'ए', 'ओ', 'ङ्', 'ऐ', 'औ', 'च्', 'ह', 'य', 'व', 'र', 'ट्', 'ल', 'ण्', 'ञ', 'म', 'ङ', 'ण', 'न', 'म्', 'झ', 'भ', 'ञ्', 'घ', 'ढ', 'ध', 'ष्', 'ज', 'ब', 'ग', 'ड', 'द', 'श्', 'ख', 'फ', 'छ', 'ठ', 'थ', 'च', 'ट', 'त', 'व्', 'क', 'प', 'य्', 'श', 'ष', 'स', 'र्', 'ह', 'ल्']