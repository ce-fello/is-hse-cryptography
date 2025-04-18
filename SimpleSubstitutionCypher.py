alphabet = 'abcdefghijklmnopqrstuvwxyz'

symbolsFreqsStandart = [8.17, 1.49, 2.78, 4.25, 12.7, 2.23, 2.02, 6.09, 6.97, 
                        0.15, 0.77, 4.03, 2.41, 6.75, 7.51, 1.93, 0.1, 5.99, 
                        6.33, 9.06, 2.76, 0.98, 2.36, 0.15, 1.97, 0.05]

bigrammsFreqsStandart = {'oc': 0.1333384, 'um': 0.0728041, 'vz': 0.0, 'ox': 0.0139953, 'jr': 0.0, 'bh': 0.0004793,
                         'ys': 0.0889562, 'pc': 0.0005751, 'ha': 1.7533862, 'ez': 0.002684, 'az': 0.0172544,
                         'xi': 0.0111675, 'bc': 0.0001438, 'qx': 0.0, 'hd': 0.0015817, 'kl': 0.0156249, 'yd': 0.0030195,
                         'xw': 0.0, 'ew': 0.1074089, 'id': 0.4131479, 'wl': 0.018932, 'mz': 0.0, 'wi': 0.5180165,
                         'qo': 0.0, 'pf': 0.0013899, 'hn': 0.0092503, 'on': 1.4637513, 'hx': 0.0, 'gd': 0.0012462,
                         'co': 0.6017964, 'gg': 0.0393018, 'cc': 0.0585213, 'hh': 0.0009107, 'pd': 0.0011024, 'wq': 0.0,
                         'bw': 0.0001438, 'ta': 0.4067254, 'kk': 0.0001438, 'qn': 0.0, 'vr': 0.0004793, 'pe': 0.3927781,
                         'ly': 0.436681, 'wv': 0.0, 'lq': 0.0, 'ep': 0.1284976, 'xt': 0.0313456, 'aa': 0.0001917,
                         'wc': 0.0011024, 'zi': 0.0061828, 'wa': 0.7742928, 'zn': 0.0, 'uj': 9.59e-05, 'kn': 0.1178095,
                         'gf': 0.0003834, 're': 1.7554471, 'ex': 0.1552899, 'ho': 0.7850289, 'xq': 0.0002876,
                         'fw': 0.0012941, 'ht': 0.2339893, 'wz': 0.0, 'hf': 0.0028757, 'yx': 4.79e-05, 'ia': 0.0999799,
                         'ob': 0.0785556, 'fq': 0.0, 'oh': 0.0224308, 'to': 1.1336164, 'qf': 0.0, 'gj': 0.0,
                         'ud': 0.0639373, 'iz': 0.0226704, 'ft': 0.0989734, 'by': 0.1159882, 'lv': 0.0322562,
                         'aw': 0.1056355, 'pi': 0.0983024, 'sj': 0.0005751, 'oi': 0.0861284, 'iv': 0.1765225, 'pv': 0.0,
                         'me': 1.0261117, 'as': 1.1904123, 'bs': 0.0404521, 'km': 0.0024923, 'bj': 0.0115509, 'vt': 0.0,
                         'nj': 0.0082917, 'gv': 9.59e-05, 'oy': 0.0270319, 'uk': 0.0023485, 'vd': 0.0, 'ss': 0.3641165,
                         'ke': 0.3602822, 'cn': 0.0001438, 'yg': 0.0008627, 'vs': 9.59e-05, 'ul': 0.4280059,
                         'lm': 0.159316, 'zw': 0.0, 'kh': 0.0035947, 'fh': 0.0010544, 'ei': 0.1148858, 'lw': 0.0184527,
                         'jg': 0.0, 'hq': 0.0, 'mn': 0.0075728, 'xr': 0.0002396, 'ci': 0.1234171, 'em': 0.282781,
                         'ge': 0.3587964, 'jm': 0.0, 'vp': 0.0, 'ir': 0.3141266, 'cb': 9.59e-05, 'of': 0.8852484,
                         'ib': 0.0658065, 'fv': 0.0, 'ua': 0.0644166, 'ds': 0.1273953, 'yn': 0.0037385, 'yh': 0.0043136,
                         'am': 0.3072248, 'qr': 0.0, 'zo': 0.0012941, 'iw': 0.0002876, 'xl': 0.0004314, 'ar': 0.9913153,
                         'ww': 0.0005272, 'wm': 0.0005272, 'rf': 0.0232935, 'uh': 4.79e-05, 'sg': 0.0048888,
                         'rc': 0.0551663, 'rk': 0.1053479, 'vq': 0.0, 'zv': 0.0001438, 'xx': 0.0, 'do': 0.3965645,
                         'es': 1.0640235, 'fd': 0.0009586, 'hj': 4.79e-05, 'wg': 4.79e-05, 'bf': 4.79e-05,
                         'lp': 0.0271757, 'ji': 0.0011024, 'zd': 0.0, 'mc': 0.0219994, 'pq': 0.0, 'nu': 0.0396852,
                         'vf': 0.0, 'ql': 0.0, 'tc': 0.0425609, 'gk': 0.0, 'qq': 0.0, 'ba': 0.1554337, 'kp': 0.0003834,
                         'dq': 0.0004793, 'wr': 0.0346047, 'dn': 0.0160083, 'yk': 0.0, 'ag': 0.1888881, 'wo': 0.2980224,
                         'xa': 0.0302432, 'mg': 0.0001438, 'ot': 0.4721485, 'nr': 0.0122219, 'tq': 0.0, 'bn': 0.0007669,
                         'jf': 0.0, 'qc': 0.0, 'xs': 0.0006231, 'fr': 0.2388781, 'ev': 0.265239, 'qw': 0.0,
                         'di': 0.2823017, 'ov': 0.1414864, 'si': 0.4520183, 'jo': 0.0370491, 'mo': 0.3124491,
                         'wn': 0.1516473, 'ax': 0.0052722, 'ey': 0.1752284, 'ui': 0.0821024, 'ut': 0.5242952,
                         'hs': 0.0106882, 'bd': 0.0014858, 'jt': 0.0, 'vw': 0.0, 'sk': 0.0684426, 'ej': 0.0031154,
                         'ks': 0.0362343, 'uy': 0.0014379, 'lu': 0.0876621, 'os': 0.2433834, 'kd': 0.0003355,
                         'ro': 0.6651585, 'rv': 0.0612532, 'jb': 0.0, 'cl': 0.1495864, 'fp': 0.0023006, 'mt': 0.000671,
                         'ne': 0.757997, 'xf': 0.0010544, 'dr': 0.1308941, 'qj': 0.0, 'fm': 0.0004314, 'ug': 0.1809799,
                         'la': 0.4516828, 'gm': 0.004026, 'hz': 0.0, 'pb': 0.0013899, 'xy': 0.0006231, 'ko': 0.0017734,
                         'ms': 0.0702639, 'yt': 0.026984, 'ij': 4.79e-05, 'jl': 0.0, 'wp': 0.0004793, 'lj': 4.79e-05,
                         'ns': 0.3018088, 'jy': 0.0, 'zc': 0.0, 'cp': 0.0014379, 'ip': 0.0550704, 'fe': 0.2252662,
                         'fi': 0.2207609, 'oa': 0.0706953, 'kt': 0.0008148, 'yo': 0.6294035, 'tp': 0.0025402,
                         'hl': 0.0068538, 'cy': 0.0223349, 'lc': 0.0059911, 'pp': 0.1200142, 'db': 0.004745,
                         'te': 0.9009212, 'vk': 0.0, 'ux': 0.0025882, 'tv': 0.0002396, 'gp': 0.0030195, 'gw': 0.0007189,
                         'kb': 0.0016775, 'or': 1.0262555, 'dv': 0.0247314, 'xc': 0.0284219, 'uq': 0.0001917, 'mx': 0.0,
                         'ym': 0.0129888, 'hg': 0.0001438, 'iy': 0.0, 'xd': 0.0, 'ie': 0.2681148, 'ee': 0.5119775,
                         'va': 0.0685385, 'tl': 0.1617124, 'ts': 0.250381, 'mj': 4.79e-05, 'yr': 0.0028757,
                         'xp': 0.053345, 'uf': 0.0159604, 'bk': 0.0, 'nx': 0.0043615, 'ae': 0.0016775, 'dx': 0.0,
                         'cg': 0.0046012, 'dh': 0.0055118, 'mu': 0.1292166, 'kg': 0.0009107, 'jv': 0.0, 'go': 0.1641089,
                         'gt': 0.0115988, 'rg': 0.0594799, 'xz': 0.0, 'bg': 0.0, 'be': 0.6146893, 'jz': 0.0, 'qm': 0.0,
                         'ai': 0.490697, 'pz': 0.0, 'uc': 0.1287373, 'us': 0.4861917, 'dj': 0.0007669, 'nc': 0.2857047,
                         'th': 3.9283557, 'ju': 0.050613, 'qa': 0.0, 'zj': 0.0, 'jd': 0.0, 'qy': 0.0, 'ur': 0.6653502,
                         'et': 0.4489029, 'dk': 0.0014858, 'er': 2.1172151, 'rz': 0.0002876, 'ih': 0.0003834,
                         'tb': 0.0034509, 'ef': 0.1511201, 'fj': 4.79e-05, 'ja': 0.0190278, 'ix': 0.0167272,
                         'rx': 9.59e-05, 'tn': 0.0088189, 'tw': 0.0874704, 'in': 2.2636382, 'hr': 0.0903941,
                         'pl': 0.1756118, 'zh': 4.79e-05, 'lh': 0.0015337, 'zg': 0.0, 'vv': 0.0, 'sm': 0.0639852,
                         'mh': 0.0003355, 'yw': 0.0032112, 'vu': 0.0025402, 'bm': 0.002684, 'hb': 0.0065183,
                         'dl': 0.0628349, 'vj': 0.0, 'kq': 0.0, 'ct': 0.2344207, 'ue': 0.0961935, 'jk': 0.0,
                         'ig': 0.2644722, 'sa': 0.3689094, 'np': 0.0053201, 'fn': 0.0001917, 'cd': 0.0021089, 'xk': 0.0,
                         'vh': 0.0, 'lr': 0.0161041, 'uu': 0.0, 'sd': 0.004026, 'oq': 0.0004314, 'cs': 0.0035467,
                         'hk': 0.0001917, 'oj': 0.0012941, 'kc': 0.0014379, 'pr': 0.2487035, 'qi': 0.0, 'eg': 0.0598633,
                         'aj': 0.0039781, 'ao': 0.006087, 'sv': 0.0004793, 'ad': 0.5948467, 'pm': 0.0030675,
                         'bu': 0.2697443, 'eb': 0.0212325, 'td': 0.0005751, 'zu': 0.0002396, 'ol': 0.4180366,
                         'xh': 0.0030195, 'sq': 0.0101609, 'nk': 0.0962893, 'xe': 0.0104964, 'bp': 0.0, 'zy': 0.0015337,
                         'tx': 0.0, 'cw': 0.0, 'rm': 0.087758, 'sy': 0.0212805, 'ls': 0.0814793, 'qh': 0.0,
                         'ek': 0.0205136, 'eq': 0.0119822, 'om': 0.5926419, 'zq': 0.0, 'dd': 0.0545911, 'lk': 0.0383432,
                         'po': 0.3729834, 'ng': 1.0051188, 'dt': 0.002684, 'jq': 0.0, 'av': 0.3843426, 'ac': 0.3905733,
                         'su': 0.240939, 'xv': 0.0, 'kr': 0.0004314, 'pk': 0.0038822, 'og': 0.0469704, 'ye': 0.1527018,
                         'ka': 0.0132763, 'ck': 0.2258414, 'vb': 0.0, 'mq': 0.0, 'eu': 0.012174, 'ik': 0.0484083,
                         'rw': 0.0217598, 'cj': 0.0, 'na': 0.175468, 'oz': 0.0027799, 'rj': 0.0004314, 'du': 0.0549745,
                         'wj': 0.0, 'da': 0.1481485, 'wu': 0.0013899, 'cu': 0.1149337, 'nn': 0.0748172, 'iq': 0.0022047,
                         'nb': 0.0047929, 'tz': 0.0010065, 'yl': 0.0072852, 'aq': 0.0004793, 'dy': 0.0791787,
                         'xu': 0.0018692, 'pt': 0.0508047, 'ce': 0.5314366, 'ry': 0.2762627, 'fx': 0.0, 'tu': 0.1738864,
                         'dm': 0.012126, 'uz': 0.004074, 'ca': 0.4243633, 'is': 1.214904, 'tm': 0.016871,
                         'rp': 0.037145, 'ph': 0.0321604, 'im': 0.3939763, 'rq': 0.0004793, 'gq': 0.0, 'tj': 0.0008148,
                         'nz': 0.0014379, 'zf': 0.0, 'cf': 0.0012462, 'sn': 0.0138994, 'nv': 0.0359947, 'sw': 0.0508047,
                         'cm': 0.0100651, 'le': 0.8587437, 'ow': 0.5455277, 'sh': 0.4811591, 'if': 0.1947355,
                         'rs': 0.3518946, 'hy': 0.0433757, 'fk': 9.59e-05, 'dp': 0.0012941, 'ab': 0.2164952, 'jn': 0.0,
                         'wk': 0.0009586, 'ru': 0.1182408, 'mb': 0.0555976, 'wh': 0.6630976, 'vo': 0.0497024, 'qe': 0.0,
                         'fl': 0.051284, 'mm': 0.0417941, 'ed': 1.3248052, 'nm': 0.0046491, 'xn': 0.0, 'nq': 0.010832,
                         'at': 1.5224164, 'ky': 0.0069018, 'au': 0.0806645, 'lg': 0.0022047, 'gi': 0.1091822,
                         'mi': 0.2701757, 'ec': 0.2608296, 'jw': 0.0, 'ap': 0.1791106, 'lb': 0.0041219, 'fy': 0.0044574,
                         'gs': 0.0416982, 'xm': 0.0001438, 'gb': 0.0011503, 'lo': 0.4294917, 'zx': 0.0, 'qu': 0.1142627,
                         'hm': 0.0100651, 'pw': 0.0016296, 'ah': 0.0156728, 'yu': 0.0, 'zm': 0.0, 'px': 0.0,
                         'ri': 0.543323, 'll': 0.7411739, 'sc': 0.1055876, 'sl': 0.054016, 'jp': 0.0002876, 'vn': 0.0,
                         'vm': 0.0, 'ws': 0.0362822, 'uw': 0.0, 'bi': 0.0537763, 'it': 1.2222851, 'ff': 0.1097574,
                         'gh': 0.3432195, 'sz': 0.0, 'vy': 0.008771, 'zz': 0.0056077, 'bb': 0.0178296, 'dg': 0.0395414,
                         'jc': 0.0, 'bl': 0.2468343, 'up': 0.2493745, 'fz': 0.0, 'fs': 0.0049367, 'tr': 0.3306142,
                         'oo': 0.4246988, 'kf': 0.0055118, 'qb': 0.0, 'pu': 0.0705515, 'an': 2.0177146, 'ok': 0.1354953,
                         'rh': 0.0187402, 'se': 0.8834271, 'hv': 0.0, 'ic': 0.4850414, 'lf': 0.0901544, 'mp': 0.1502574,
                         'ii': 0.0, 'zb': 0.0, 'dw': 0.0088669, 'ze': 0.0351319, 'eh': 0.0273675, 'ak': 0.1435952,
                         'yp': 0.0070456, 'hi': 1.2958561, 'za': 0.003355, 'fa': 0.2160639, 'zr': 0.0005751,
                         'gc': 0.0022527, 'bv': 0.0065663, 'he': 3.6071357, 'op': 0.1350639, 'lz': 4.79e-05,
                         'nh': 0.0082438, 'kx': 0.0, 'hp': 0.0002876, 'dz': 0.0, 'yj': 0.0001438, 'nt': 0.7810987,
                         'ub': 0.060726, 'yc': 0.0098734, 'lx': 0.0, 'ki': 0.095187, 'mk': 0.0, 'af': 0.0785556,
                         'jj': 0.0, 'ch': 0.5389135, 'ya': 0.0155769, 'hc': 0.0014379, 'qk': 0.0, 'qg': 0.0,
                         'kw': 0.0032592, 'gl': 0.0934615, 'ea': 0.7690206, 'iu': 0.0064225, 'py': 0.010113, 'gx': 0.0,
                         'il': 0.3936408, 'cx': 0.0, 'ay': 0.3080875, 'vc': 0.0, 'yz': 0.0007189, 'un': 0.3875538,
                         'br': 0.1393775, 'ga': 0.1517432, 'ty': 0.1117704, 'de': 0.6216869, 'bo': 0.1853414,
                         'fg': 0.0009107, 'bt': 0.0278467, 'nd': 1.4753501, 'mv': 0.0, 'gz': 0.0002396, 'ny': 0.1018491,
                         'bz': 0.0, 'wt': 0.0004793, 'zl': 0.0046491, 'je': 0.0247793, 'rt': 0.2767899, 'yv': 0.000671,
                         'vl': 0.0, 'so': 0.495442, 'ml': 0.004745, 'cr': 0.1618562, 've': 1.0398673, 'st': 1.0042082,
                         'qd': 0.0, 'qt': 0.0, 'yb': 0.0048408, 'cz': 0.0, 'pg': 4.79e-05, 'gr': 0.1434035,
                         'fo': 0.4685538, 'pj': 0.0, 'ni': 0.2512917, 'we': 0.5938881, 'ti': 0.6167982, 'li': 0.4602621,
                         'js': 0.0, 'ma': 0.5654183, 'xj': 0.0, 'gy': 0.0086751, 'cq': 0.0044095, 'uv': 0.0039302,
                         'pn': 0.0007189, 'yf': 0.0028278, 'fb': 0.0003834, 'fc': 0.0021089, 'rr': 0.1646361, 'zs': 0.0,
                         'df': 0.0115509, 'tt': 0.2426165, 'vi': 0.1706751, 'zk': 0.0, 'my': 0.2925106, 'xo': 0.0014858,
                         'el': 0.5384822, 'bq': 0.0, 'zt': 0.0, 'jx': 0.0, 'hu': 0.085026, 'gu': 0.0667172,
                         'en': 1.2625933, 'yq': 0.0, 'gn': 0.0320166, 'mr': 0.0999319, 'nw': 0.0081, 'no': 0.6392289,
                         'wd': 0.0053201, 'wx': 0.0, 'ln': 0.0033071, 'od': 0.1563444, 'pa': 0.234181, 'ra': 0.4437745,
                         'yi': 0.0260734, 'kz': 0.0, 'qp': 0.0, 'vg': 0.0, 'sf': 0.0103047, 'sx': 0.0, 'zp': 0.0,
                         'qs': 0.0, 'mf': 0.0036426, 'yy': 0.0, 'md': 0.0004314, 'cv': 0.0, 'rn': 0.1667929,
                         'sr': 0.0016296, 'hw': 0.0023006, 'dc': 0.0017734, 'wy': 0.0023485, 'ou': 1.7362276,
                         'oe': 0.0247314, 'rb': 0.0148101, 'vx': 0.0, 'al': 0.6719644, 'sp': 0.1451769, 'nf': 0.0441905,
                         'ku': 0.0012462, 'uo': 0.0038822, 'ld': 0.4214875, 'xb': 0.0002396, 'kj': 0.0, 'tf': 0.0070456,
                         'jh': 0.0001438, 'mw': 0.0001917, 'tk': 0.0001917, 'qz': 0.0, 'bx': 0.0, 'ps': 0.0514757,
                         'sb': 0.0118864, 'fu': 0.078316, 'nl': 0.099884, 'wf': 0.0014379, 'io': 0.3505526,
                         'eo': 0.0325438, 'kv': 0.0, 'rd': 0.2515793, 'qv': 0.0, 'lt': 0.0698805, 'tg': 0.0015817,
                         'xg': 0.0, 'rl': 0.101945, 'wb': 0.0011024
                         }

bigramms = {'bf': 0, 'yh': 0, 'fq': 0, 'dg': 0, 'cv': 0, 'kp': 0, 'pk': 0, 'dl': 0, 'zv': 0, 'cx': 0, 'ry': 0, 'gv': 0,
            'yw': 0, 'ar': 0, 'jv': 0, 'mr': 0, 'fd': 0, 'bz': 0, 'xf': 0, 'ny': 0, 'pa': 0, 'po': 0, 'lf': 0, 'll': 0,
            'nb': 0, 'jq': 0, 'io': 0, 'ao': 0, 'zc': 0, 'xu': 0, 'th': 0, 'cu': 0, 'cc': 0, 'fy': 0, 'bi': 0, 'fc': 0,
            'ad': 0, 'rv': 0, 'ms': 0, 'pt': 0, 'xd': 0, 'hq': 0, 'un': 0, 'gh': 0, 'qa': 0, 'fx': 0, 'kr': 0, 'zk': 0,
            'nm': 0, 'fv': 0, 'vt': 0, 'wy': 0, 'zs': 0, 'ku': 0, 'eh': 0, 'or': 0, 'ae': 0, 'vc': 0, 'bh': 0, 'xx': 0,
            'ff': 0, 'dx': 0, 'bc': 0, 'ls': 0, 'ai': 0, 'tc': 0, 'ze': 0, 'eq': 0, 'aa': 0, 'si': 0, 'fn': 0, 'bv': 0,
            'ro': 0, 'yc': 0, 'tx': 0, 'dj': 0, 'hu': 0, 'dp': 0, 'cp': 0, 'sy': 0, 'zr': 0, 'vf': 0, 'dk': 0, 'tk': 0,
            'zi': 0, 'hi': 0, 'rm': 0, 'ac': 0, 'ax': 0, 'vm': 0, 'fe': 0, 'uk': 0, 'ah': 0, 'wa': 0, 'ak': 0, 're': 0,
            'nr': 0, 'uf': 0, 'hj': 0, 'pw': 0, 'ni': 0, 'ul': 0, 'kx': 0, 'ej': 0, 'sn': 0, 'pc': 0, 'jh': 0, 'fb': 0,
            'dw': 0, 'qw': 0, 'aq': 0, 'ba': 0, 'nf': 0, 'jx': 0, 'ha': 0, 'oo': 0, 'tg': 0, 'uu': 0, 'rl': 0, 'ot': 0,
            'os': 0, 'nx': 0, 'ko': 0, 'ig': 0, 'lh': 0, 'is': 0, 'ta': 0, 'sg': 0, 'hl': 0, 'fm': 0, 'wl': 0, 'ik': 0,
            'oc': 0, 'qh': 0, 'uy': 0, 'bt': 0, 'yo': 0, 'er': 0, 'px': 0, 'bw': 0, 'qz': 0, 'rz': 0, 'ml': 0, 'hn': 0,
            'nu': 0, 'ss': 0, 'ca': 0, 'zf': 0, 'xq': 0, 'gm': 0, 'sq': 0, 'py': 0, 'ne': 0, 'fl': 0, 'dr': 0, 'kh': 0,
            'es': 0, 'gd': 0, 'bx': 0, 'mv': 0, 'xo': 0, 'dh': 0, 'so': 0, 'ty': 0, 'uj': 0, 'mf': 0, 'ki': 0, 'se': 0,
            'tz': 0, 'nw': 0, 'jo': 0, 'mh': 0, 'dt': 0, 'mi': 0, 'pq': 0, 'lj': 0, 'ri': 0, 'qf': 0, 'km': 0, 'hd': 0,
            'iv': 0, 'kt': 0, 'gx': 0, 'zu': 0, 'in': 0, 'fk': 0, 'mk': 0, 'kc': 0, 'rc': 0, 'ew': 0, 'ux': 0, 'sl': 0,
            'vy': 0, 'ti': 0, 'kq': 0, 'xj': 0, 'xp': 0, 'uc': 0, 'qu': 0, 'rg': 0, 'aw': 0, 'ym': 0, 'cr': 0, 'di': 0,
            'rj': 0, 'gu': 0, 'pn': 0, 'ru': 0, 'gs': 0, 'wx': 0, 'sk': 0, 'pd': 0, 'xz': 0, 'ud': 0, 'ev': 0, 'lo': 0,
            'ov': 0, 'xs': 0, 'be': 0, 'yu': 0, 'yt': 0, 'ec': 0, 'bn': 0, 'js': 0, 'gr': 0, 'vb': 0, 'hh': 0, 'el': 0,
            'mp': 0, 'wn': 0, 'kl': 0, 'qj': 0, 'ja': 0, 'om': 0, 'us': 0, 'cg': 0, 'cj': 0, 'ye': 0, 'wk': 0, 'oq': 0,
            'dc': 0, 'dm': 0, 'up': 0, 'fs': 0, 'yq': 0, 'sf': 0, 'gn': 0, 'if': 0, 'ou': 0, 'qn': 0, 'lx': 0, 'rq': 0,
            'fu': 0, 'rk': 0, 'tr': 0, 'nq': 0, 'ur': 0, 'pm': 0, 'rw': 0, 'cn': 0, 'ge': 0, 'um': 0, 'gq': 0, 'tn': 0,
            'va': 0, 'qt': 0, 'wf': 0, 'wu': 0, 'le': 0, 'tm': 0, 'rr': 0, 'iu': 0, 'vz': 0, 'ei': 0, 'id': 0, 'mu': 0,
            'vo': 0, 'zg': 0, 'tp': 0, 'mb': 0, 'cy': 0, 'zx': 0, 've': 0, 'he': 0, 'lc': 0, 'qi': 0, 'ol': 0, 'ub': 0,
            'zz': 0, 'ip': 0, 'sv': 0, 'oj': 0, 'bu': 0, 'vw': 0, 'ef': 0, 'fh': 0, 'sm': 0, 'al': 0, 'uw': 0, 'xb': 0,
            'hp': 0, 'af': 0, 'pf': 0, 'wc': 0, 'zo': 0, 'ts': 0, 'qy': 0, 'nc': 0, 'lk': 0, 'dv': 0, 'vs': 0, 'jr': 0,
            'hx': 0, 'co': 0, 'ij': 0, 'pi': 0, 'pu': 0, 'ix': 0, 'jg': 0, 'zt': 0, 'hm': 0, 'hz': 0, 'gl': 0, 'jw': 0,
            'jz': 0, 'ui': 0, 'mz': 0, 'ma': 0, 'dy': 0, 'zj': 0, 'yl': 0, 'za': 0, 'wj': 0, 'dq': 0, 'hr': 0, 'xn': 0,
            'ay': 0, 'zh': 0, 'sr': 0, 'lg': 0, 'vk': 0, 'yk': 0, 'tb': 0, 'kb': 0, 'hs': 0, 'rd': 0, 'gk': 0, 'vi': 0,
            'kk': 0, 'fp': 0, 'qe': 0, 'kv': 0, 'hw': 0, 'dz': 0, 'yj': 0, 'su': 0, 'tv': 0, 'wr': 0, 'gz': 0, 'wd': 0,
            'wq': 0, 'do': 0, 'yg': 0, 'nn': 0, 'ct': 0, 'pp': 0, 'iw': 0, 'hy': 0, 'ra': 0, 'xm': 0, 'bq': 0, 'pj': 0,
            'mn': 0, 'bs': 0, 'vd': 0, 'qo': 0, 'wb': 0, 'tt': 0, 'rp': 0, 'sb': 0, 'gb': 0, 'ph': 0, 'wt': 0, 'ww': 0,
            'wg': 0, 'dn': 0, 'nk': 0, 'yz': 0, 'we': 0, 'df': 0, 'ek': 0, 'ag': 0, 'on': 0, 'zq': 0, 'sj': 0, 'pe': 0,
            'bd': 0, 'lp': 0, 'qv': 0, 'db': 0, 'jf': 0, 'md': 0, 'uv': 0, 'sc': 0, 'xa': 0, 'my': 0, 'ga': 0, 'jl': 0,
            'as': 0, 'gp': 0, 'vx': 0, 'gw': 0, 'mx': 0, 'nz': 0, 'ep': 0, 'ug': 0, 'fa': 0, 'xg': 0, 'tu': 0, 'xw': 0,
            'kz': 0, 'mo': 0, 'cm': 0, 'mc': 0, 'jj': 0, 'nt': 0, 'em': 0, 'rn': 0, 'ie': 0, 'mg': 0, 'jk': 0, 'xr': 0,
            'wv': 0, 'jt': 0, 'ap': 0, 'en': 0, 'wz': 0, 'bp': 0, 'ke': 0, 'de': 0, 'zw': 0, 'ez': 0, 'qs': 0, 'eg': 0,
            'na': 0, 'st': 0, 'oh': 0, 'oi': 0, 'ut': 0, 'ck': 0, 'ho': 0, 'yr': 0, 'wo': 0, 'yy': 0, 'ht': 0, 'eu': 0,
            'tq': 0, 'yx': 0, 'ds': 0, 'op': 0, 'ly': 0, 'sd': 0, 'jb': 0, 'jd': 0, 'gt': 0, 'pg': 0, 'ey': 0, 'pl': 0,
            'vq': 0, 'xl': 0, 'nd': 0, 'cb': 0, 'xy': 0, 'sw': 0, 'ee': 0, 'rx': 0, 'np': 0, 'wh': 0, 'fj': 0, 'xc': 0,
            'bj': 0, 'iq': 0, 'ia': 0, 'yb': 0, 'cq': 0, 'eb': 0, 'hv': 0, 'nl': 0, 'ir': 0, 'yf': 0, 'eo': 0, 'fr': 0,
            'qd': 0, 'nv': 0, 'jp': 0, 'xe': 0, 'ys': 0, 'jc': 0, 'zy': 0, 'fi': 0, 'tw': 0, 'qc': 0, 'lv': 0, 'gy': 0,
            'du': 0, 'vn': 0, 'cd': 0, 'vg': 0, 'nh': 0, 'nj': 0, 'at': 0, 'av': 0, 'hg': 0, 'ql': 0, 'gf': 0, 'da': 0,
            'kf': 0, 'kd': 0, 'sh': 0, 'pz': 0, 'ox': 0, 'kw': 0, 'il': 0, 'vl': 0, 'gg': 0, 'qr': 0, 'uo': 0, 'iz': 0,
            'tl': 0, 'ex': 0, 'gj': 0, 'qx': 0, 'ab': 0, 'oa': 0, 'mq': 0, 'qq': 0, 'ws': 0, 'lm': 0, 'ob': 0, 'te': 0,
            'pb': 0, 'ow': 0, 'xi': 0, 'xt': 0, 'mt': 0, 'uh': 0, 'oy': 0, 'an': 0, 'xv': 0, 'et': 0, 'to': 0, 'hf': 0,
            'ld': 0, 'ci': 0, 'ns': 0, 'hc': 0, 'lr': 0, 'bo': 0, 'az': 0, 'ue': 0, 'ih': 0, 'bb': 0, 'sz': 0, 'mm': 0,
            'rh': 0, 'lu': 0, 'tf': 0, 'ic': 0, 'oe': 0, 'je': 0, 'ln': 0, 'yp': 0, 'vv': 0, 'it': 0, 'cw': 0, 'iy': 0,
            'ib': 0, 'me': 0, 'ft': 0, 'vj': 0, 'lb': 0, 'zl': 0, 'zp': 0, 'dd': 0, 'uz': 0, 'ya': 0, 'br': 0, 'sa': 0,
            'lw': 0, 'ng': 0, 'rt': 0, 'ji': 0, 'rb': 0, 'of': 0, 'vu': 0, 'bm': 0, 'rf': 0, 'bl': 0, 'qk': 0, 'la': 0,
            'ce': 0, 'aj': 0, 'am': 0, 'fz': 0, 'rs': 0, 'ea': 0, 'yn': 0, 'fg': 0, 'oz': 0, 'ua': 0, 'sx': 0, 'gc': 0,
            'ju': 0, 'zb': 0, 'yi': 0, 'bg': 0, 'wm': 0, 'im': 0, 'au': 0, 'qb': 0, 'fw': 0, 'ka': 0, 'td': 0, 'tj': 0,
            'ky': 0, 'lq': 0, 'kg': 0, 'jy': 0, 'hb': 0, 'cf': 0, 'by': 0, 'lz': 0, 'fo': 0, 'ks': 0, 'ch': 0, 'ok': 0,
            'jm': 0, 'vp': 0, 'og': 0, 'hk': 0, 'zn': 0, 'cl': 0, 'mw': 0, 'od': 0, 'kj': 0, 'wp': 0, 'sp': 0, 'qg': 0,
            'ps': 0, 'pr': 0, 'qp': 0, 'vr': 0, 'gi': 0, 'pv': 0, 'kn': 0, 'bk': 0, 'vh': 0, 'cz': 0, 'zm': 0, 'no': 0,
            'cs': 0, 'xh': 0, 'go': 0, 'yv': 0, 'yd': 0, 'ii': 0, 'li': 0, 'mj': 0, 'jn': 0, 'qm': 0, 'xk': 0, 'ed': 0,
            'zd': 0, 'wi': 0, 'uq': 0, 'lt': 0}

def create_substitution_key(key):
    key = key.lower()
    key = ''.join(sorted(set(key), key=key.index))
    for letter in alphabet:
        if letter not in key:
            key += letter
    return key

def encrypt(text, key):
    key = create_substitution_key(key)
    encrypted_text = ''
    for char in text.lower():
        if char in alphabet:
            index = alphabet.index(char)
            encrypted_text += key[index]
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, key):
    key = create_substitution_key(key)
    decrypted_text = ''
    for char in text.lower():
        if char in key:
            index = key.index(char)
            decrypted_text += alphabet[index]
        else:
            decrypted_text += char
    return decrypted_text

def simple_substitution_crack(code):
    code = code.lower()
    freqs = [0 for i in range(26)]
    for i in range(len(code)):
        if code[i] != ' ':
            freqs[alphabet.index(code[i])] += 1

    for i in range(len(freqs)):
        freqs[i] = (freqs[i] / len(code)) * 100

    freqsSorted = sorted(freqs)

    key = []
    for i in range(len(freqsSorted)):
        symb = alphabet[freqs.index(freqsSorted[i])]
        if not (symb in key):
            key.append(symb)
        else:
            curFreq = freqsSorted[i]
            for j in range(len(freqs)):
                if freqs[j] == curFreq:
                    s = alphabet[j]
                    if not (s in key):
                        key.append(s)
                        break

    tmp_key = ''
    for e in list(reversed(key)):
        tmp_key += e
    key = tmp_key
    print('First key: ', key)
    text = decrypt(code, key)
    for i in range(1, len(text)):
        if text[i] != ' ' and text[i - 1] != ' ':
            bigramms[text[i - 1] + text[i]] += 1
    for k, v in bigramms.items():
        bigramms[k] = (bigramms[k] / (len(text) - 1)) * 100
    bigrammsRating = 0
    for k, v in bigramms.items():
        bigrammsRating += (bigramms[k] - bigrammsFreqsStandart[k]) ** 2
    prevBigrammsRating = bigrammsRating
    step = 1
    while True:
        findGoodBigrammFlag = False
        for i in range(0, 26):
            if i + step >= 26:
                break
            tmp = list(key)
            tmp[i], tmp[i + step] = tmp[i + step], tmp[i]
            key = ''.join(tmp)
            copyBigrammsFreq = {k: v for k, v in bigramms.items()}
            for sym in alphabet:
                if sym == alphabet[i] or sym == alphabet[i + step]:
                    continue
                bigramms[sym + alphabet[i]], bigramms[sym + alphabet[i + step]] = \
                bigramms[sym + alphabet[i + step]], bigramms[sym + alphabet[i]]
                bigramms[alphabet[i] + sym], bigramms[alphabet[i + step] + sym] = \
                bigramms[alphabet[i + step] + sym], bigramms[alphabet[i] + sym]
            bigramms[alphabet[i] + alphabet[i + step]], bigramms[alphabet[i + step] + alphabet[i]] = \
                bigramms[alphabet[i + step] + alphabet[i]], bigramms[alphabet[i] + alphabet[i + step]]
            bigramms[alphabet[i] + alphabet[i]], bigramms[alphabet[i + step] + alphabet[i + step]] = \
                bigramms[alphabet[i + step] + alphabet[i + step]], bigramms[alphabet[i] + alphabet[i]]
            bigrammsRating = 0
            for k, v in bigramms.items():
                bigrammsRating += (bigramms[k] - bigrammsFreqsStandart[k]) ** 2
            if bigrammsRating < prevBigrammsRating:
                findGoodBigrammFlag = True
                prevBigrammsRating = bigrammsRating
                step = 1
                break
            else:
                tmp = list(key)
                tmp[i], tmp[i + step] = tmp[i + step], tmp[i]
                key = ''.join(tmp)
                for k, v in copyBigrammsFreq.items():
                    bigramms[k] = v
        if findGoodBigrammFlag == False:
            step += 1
            if step >= 25:
                break
    print('Final key: ', key)
    return key

if __name__ == "__main__":
    key = ''
    while True:
        user_input = input("> Choose what to do: e(ncrypt), d(ecrypt), k(ey), c(crack), q(uit): ").lower()
        match user_input:
            case 'q':
                print("> Shutting down...")
                break
            case 'k':
                key = input("> Type in the key (line of unique symbols): ")
                print("> Key saved")
            case 'c':
                text_to_crack = input("> Type in text to crack: ")
                simple_substitution_crack(text_to_crack)
            case 'e':
                text_to_encrypt = input("> Type in the text to encrypt: ")
                encrypted_text = encrypt(text_to_encrypt, key)
                print(f"> Encrypted text: {encrypted_text}")
            case 'd':
                text_to_decrypt = input("> Type in the text to decrypt: ")
                decrypted_text = decrypt(text_to_decrypt, key)
                print(f"> Decrypted text: {decrypted_text}")
            case _:
                print("> Input not recognised")
