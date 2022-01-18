import requests
from tqdm import tqdm

headers = {
    'authority': 'downloader.disk.yandex.ru',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-dest': 'iframe',
    'referer': 'https://disk.yandex.ru/',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cookie': 'mda=0; fuid01=605cfc7a2b0cbeb4.1wJIE1xjRkL3imJ2r4sSjAijmyKnDvOxdCNXpYp7bQB4sOQ-jhFIFi0h3qL4IvsE7zxyq7-R_JytR60v-SLdnh06kscO2N_MoMT7qqb7JG6U8fgS3w9UKKnnjcA7fYbS; _ym_uid=1614385596317816884; is_gdpr=0; skid=7030054391618765281; gdpr=0; L=UXpIfENaZ19dfV1gB2Rvfml/QllyVm98BDkCARx4dUY=.1620846519.14599.349519.86f2662200a7f603e9e4abc3550cac30; yandex_login=aalov006; is_gdpr_b=CJ3XLxC9NCgC; yandexuid=9605977141614370855; yuidss=9605977141614370855; yp=1629059059.yu.67702671617322530; ymex=1631564659.oyu.67702671617322530#1932682530.yrts.1617322530#1944332662.yrtsi.1628972662; i=c9bAFwSjw+sqIzop+FChE/8v9pXmltTdYJ6I2IfIuyn3WL5rwg4AYTMjFYfxpPLFRfEpyBNoSFxkkB9LeN4uoLdg+Wk=; _ym_d=1633600249; prodqad=1; _ym_isad=1; Session_id=3:1638044960.5.1.1620846452687:HwzcXw:7a.1|1370308835.0.2|157008265.67.2.2:67|3:244285.668640.tfo8CiVvX3S2wGgGo04nzJs5hkE; sessionid2=3:1638044960.5.1.1620846452687:HwzcXw:7a.1|1370308835.0.2|157008265.67.2.2:67|3:244285.668640.tfo8CiVvX3S2wGgGo04nzJs5hkE; _yasc=fLGIoIAAFdc19QXwiMBYd5Qg3WXW+oo4FiZ8p+APU4bEG3+qfU5HrQ==',
    'dnt': '1',
    'sec-gpc': '1',
}

params = (
    ('uid', '0'),
    ('filename', 'img_codes.hdf5'),
    ('disposition', 'attachment'),
    ('hash', 'OFFRwADKx2YhIW6gndpMLZHYb1XNLK5O2RiGc0n5W1QHBKFOP/vuqQzI88288qvVq/J6bpmRyOJonT3VoXnDag==:/img_codes.hdf5'),
    ('limit', '0'),
    ('content_type', 'application/x-hdf'),
    ('owner_uid', '181405954'),
    ('fsize', '19641206408'),
    ('hid', '941d824427de0edfe198de8a49329c98'),
    ('media_type', 'data'),
    ('tknv', 'v2'),
)

resp = requests.get('https://downloader.disk.yandex.ru/disk/90b35669b38ef6a3bcdb87a6a87d172c98a47cefde7c69b2acd6db538c8c0e20/61a37015/VsxPlh9nn2BfshAArUKAS6ooF7Sx3lVfolOX_xyQiQbbytsj5_8kHL-jepKtVsFbE8fpWtQFRLApKeTaN4bPrQ%3D%3D', headers=headers, params=params, stream=True)
total = int(resp.headers.get('content-length', 0))
fname = 'img_codes.hdf5'
with open(fname, 'wb') as file, tqdm(
    desc=fname,
     total=total,
     unit='iB',
    unit_scale=True,
    unit_divisor=1024,
) as bar:
    for data in resp.iter_content(chunk_size=1024):
        size = file.write(data)
        bar.update(size)