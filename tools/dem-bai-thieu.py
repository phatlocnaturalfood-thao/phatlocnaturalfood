# Đếm số bài SEO còn thiếu so với lịch, tính theo GIỜ VIỆT NAM (máy chạy tự động dùng giờ UTC).
# Lịch: 2 bài/ngày, mốc 6:40 và 18:40 giờ VN, từ 23/10/2026. In: "da_den_han=.. da_dang=.. thieu=.."
import json, os, datetime
VN = datetime.timezone(datetime.timedelta(hours=7))
now = datetime.datetime.now(VN)
d, den_han = datetime.date(2026, 10, 23), 0
while d <= now.date():
    for h, m in ((6, 40), (18, 40)):
        if datetime.datetime(d.year, d.month, d.day, h, m, tzinfo=VN) <= now:
            den_han += 1
    d += datetime.timedelta(days=1)
R = os.path.dirname(os.path.abspath(__file__))
da_dang = sum(x['trang_thai'] == 'da_dang' for x in json.load(open(R + '/lich-bai.json', encoding='utf-8')))
print(f'gio_vn={now:%Y-%m-%d %H:%M} da_den_han={den_han} da_dang={da_dang} thieu={max(0, den_han - da_dang)}')
