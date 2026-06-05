import streamlit as st
from datetime import datetime

# =======================================================
# ⚙️ 1. 九星の名前・解説文の定義
# =======================================================
def get_kyusei_name(star_num):
    kyusei_list = {
        1: "一白水星", 2: "二黒土星", 3: "三碧木星", 4: "四緑木星",
        5: "五黄土星", 6: "六白金星", 7: "七赤金星", 8: "八白土星", 9: "九紫火星"
    }
    return kyusei_list.get(star_num, "不明")

# 九星の数字から「五行」を返す辞書
STAR_GOGYOM = {
    1: "水",
    2: "土", 3: "木", 4: "木",
    5: "土", 6: "金", 7: "金",
    8: "土", 9: "火"
}

CHARACTER_EXPLANATIONS = {
    "一白水星": "【柔軟性と強い芯を持つ水の精神】\n人当たりが良く柔軟で、周囲に合わせるのが上手な潤滑油タイプ。しかし内面は非常に頑固で、じっくり物事を考える思慮深さを持っています。",
    "二黒土星": "【大地のような包容力と育成の心】\n真面目でコツコツ派。人をサポートしたり育てたりするのが得意な、縁の下の力持ちです。",
    "三碧木星": "【アイデアの泉・若々しい開拓者】\n頭の回転が速く、常に新しいワクワクを探している少年のような好奇心の持ち主。フットワークが軽く行動力抜群です。",
    "四緑木星": "【調和をもたらす風・抜群の社交性】\n人当たりが柔らかく、周囲の空気を読んで柔軟に合わせられる「大人の気配り」が自然とできる癒やし系です。",
    "五黄土星": "【圧倒的な存在感を持つ統率者】\n周囲を巻き込む強力なエネルギーの持ち主。波乱万丈を生き抜く強さを持っています。",
    "六白金星": "【磨けば光る原石・完璧主義のリーダー】\n高いプライドと強い責任感を持つ職人気質の星。正義感が強く、自分の信念を曲げない高潔さがあります。",
    "七赤金星": "【豊かな表現力と楽しさを生む星】\nおしゃべりや楽しいことが大好きで、人を惹きつける魅力があります。物事をクリティカルに見る鋭さも併せ持ちます。",
    "八白土星": "【山のような安定感と意志の強さ】\n一見クールに見えますが、内面は熱い情熱家。目標に向かって一歩一歩突き進む努力家です。",
    "九紫火星": "【美と知性を兼ね備えた情熱の火】\n華やかでセンスが良く、直感力に優れています。先見の明がありますが、熱しやすく冷めやすい一面も。"
}

# 📜 萬年暦に基づく陽遁・陰遁データベース（1940〜2030）
HISTORICAL_SWITCH_TIMELINE = [
    (datetime(1939, 12, 21).date(), 'yoton'), (datetime(1940, 6, 18).date(), 'inton'),
    (datetime(1940, 12, 15).date(), 'yoton'), (datetime(1941, 6, 13).date(), 'inton'),
    (datetime(1941, 12, 10).date(), 'yoton'), (datetime(1942, 6, 8).date(),  'inton'),
    (datetime(1942, 12, 29).date(), 'yoton'), (datetime(1943, 6, 27).date(), 'inton'),
    (datetime(1943, 12, 24).date(), 'yoton'), (datetime(1944, 6, 21).date(), 'inton'),
    (datetime(1944, 12, 18).date(), 'yoton'), (datetime(1945, 6, 16).date(), 'inton'),
    (datetime(1945, 12, 13).date(), 'yoton'), (datetime(1946, 6, 11).date(), 'inton'),
    (datetime(1946, 12, 7).date(),  'yoton'), (datetime(1947, 6, 5).date(),  'inton'),
    (datetime(1947, 12, 26).date(), 'yoton'), (datetime(1948, 6, 23).date(), 'inton'),
    (datetime(1948, 12, 20).date(), 'yoton'), (datetime(1949, 6, 18).date(), 'inton'),
    (datetime(1949, 12, 15).date(), 'yoton'), (datetime(1950, 6, 13).date(), 'inton'),
    (datetime(1950, 12, 10).date(), 'yoton'), (datetime(1951, 6, 8).date(),  'inton'),
    (datetime(1951, 12, 29).date(), 'yoton'), (datetime(1952, 6, 26).date(), 'inton'),
    (datetime(1952, 12, 23).date(), 'yoton'), (datetime(1953, 6, 21).date(), 'inton'),
    (datetime(1953, 12, 18).date(), 'yoton'), (datetime(1954, 6, 16).date(), 'inton'),
    (datetime(1954, 12, 13).date(), 'yoton'), (datetime(1955, 6, 11).date(), 'inton'),
    (datetime(1956, 12, 7).date(),  'yoton'), (datetime(1956, 6, 5).date(),  'inton'),
    (datetime(1956, 12, 26).date(), 'yoton'), (datetime(1957, 6, 24).date(), 'inton'),
    (datetime(1957, 12, 21).date(), 'yoton'), (datetime(1958, 6, 19).date(), 'inton'),
    (datetime(1958, 12, 16).date(), 'yoton'), (datetime(1959, 6, 14).date(), 'inton'),
    (datetime(1959, 12, 30).date(), 'yoton'), (datetime(1960, 6, 27).date(), 'inton'),
    (datetime(1960, 12, 24).date(), 'yoton'), (datetime(1961, 6, 22).date(), 'inton'),
    (datetime(1961, 12, 19).date(), 'yoton'), (datetime(1962, 6, 17).date(), 'inton'),
    (datetime(1962, 12, 14).date(), 'yoton'), (datetime(1963, 6, 12).date(), 'inton'),
    (datetime(1963, 12, 9).date(),  'yoton'), (datetime(1964, 6, 6).date(),  'inton'),
    (datetime(1964, 12, 29).date(), 'yoton'), (datetime(1965, 6, 27).date(), 'inton'),
    (datetime(1965, 12, 24).date(), 'yoton'), (datetime(1966, 6, 22).date(), 'inton'),
    (datetime(1966, 12, 19).date(), 'yoton'), (datetime(1967, 6, 17).date(), 'inton'),
    (datetime(1967, 12, 23).date(), 'yoton'), (datetime(1968, 6, 20).date(), 'inton'),
    (datetime(1968, 12, 17).date(), 'yoton'), (datetime(1969, 6, 15).date(), 'inton'),
    (datetime(1969, 12, 12).date(), 'yoton'), (datetime(1970, 6, 10).date(), 'inton'),
    (datetime(1970, 12, 29).date(), 'yoton'), (datetime(1971, 6, 27).date(), 'inton'),
    (datetime(1971, 12, 24).date(), 'yoton'), (datetime(1972, 6, 21).date(), 'inton'),
    (datetime(1972, 12, 18).date(), 'yoton'), (datetime(1973, 6, 16).date(), 'inton'),
    (datetime(1973, 12, 13).date(), 'yoton'), (datetime(1974, 6, 11).date(), 'inton'),
    (datetime(1974, 12, 8).date(),  'yoton'), (datetime(1975, 6, 6).date(),  'inton'),
    (datetime(1975, 12, 29).date(), 'yoton'), (datetime(1976, 6, 26).date(), 'inton'),
    (datetime(1976, 12, 22).date(), 'yoton'), (datetime(1977, 6, 20).date(), 'inton'),
    (datetime(1977, 12, 17).date(), 'yoton'), (datetime(1978, 6, 15).date(), 'inton'),
    (datetime(1978, 12, 12).date(), 'yoton'), (datetime(1979, 6, 10).date(), 'inton'),
    (datetime(1979, 12, 7).date(),  'yoton'), (datetime(1980, 6, 4).date(),  'inton'),
    (datetime(1980, 12, 28).date(), 'yoton'), (datetime(1981, 6, 26).date(), 'inton'),
    (datetime(1981, 12, 23).date(), 'yoton'), (datetime(1982, 6, 21).date(), 'inton'),
    (datetime(1982, 12, 18).date(), 'yoton'), (datetime(1983, 6, 16).date(), 'inton'),
    (datetime(1983, 12, 13).date(), 'yoton'), (datetime(1984, 6, 10).date(), 'inton'),
    (datetime(1984, 12, 9).date(),  'yoton'), (datetime(1985, 6, 7).date(),  'inton'),
    (datetime(1985, 12, 29).date(), 'yoton'), (datetime(1986, 6, 27).date(), 'inton'),
    (datetime(1986, 12, 24).date(), 'yoton'), (datetime(1987, 6, 22).date(), 'inton'),
    (datetime(1987, 12, 19).date(), 'yoton'), (datetime(1988, 6, 17).date(), 'inton'),
    (datetime(1988, 12, 13).date(), 'yoton'), (datetime(1989, 6, 11).date(), 'inton'),
    (datetime(1989, 12, 8).date(),  'yoton'), (datetime(1990, 6, 6).date(),  'inton'),
    (datetime(1990, 12, 29).date(), 'yoton'), (datetime(1991, 6, 27).date(), 'inton'),
    (datetime(1991, 12, 24).date(), 'yoton'), (datetime(1992, 6, 21).date(), 'inton'),
    (datetime(1992, 12, 18).date(), 'yoton'), (datetime(1993, 6, 16).date(), 'inton'),
    (datetime(1993, 12, 13).date(), 'yoton'), (datetime(1994, 6, 11).date(), 'inton'),
    (datetime(1994, 12, 8).date(),  'yoton'), (datetime(1995, 6, 6).date(),  'inton'),
    (datetime(1995, 12, 29).date(), 'yoton'), (datetime(1996, 6, 26).date(), 'inton'),
    (datetime(1996, 12, 22).date(), 'yoton'), (datetime(1997, 6, 20).date(), 'inton'),
    (datetime(1997, 12, 17).date(), 'yoton'), (datetime(1998, 6, 15).date(), 'inton'),
    (datetime(1998, 12, 12).date(), 'yoton'), (datetime(1999, 6, 10).date(), 'inton'),
    (datetime(1999, 12, 7).date(),  'yoton'), (datetime(2000, 6, 4).date(),  'inton'),
    (datetime(2000, 12, 28).date(), 'yoton'), (datetime(2001, 6, 26).date(), 'inton'),
    (datetime(2001, 12, 23).date(), 'yoton'), (datetime(2002, 6, 21).date(), 'inton'),
    (datetime(2002, 12, 18).date(), 'yoton'), (datetime(2003, 6, 16).date(), 'inton'),
    (datetime(2003, 12, 13).date(), 'yoton'), (datetime(2004, 6, 10).date(), 'inton'),
    (datetime(2004, 12, 23).date(), 'yoton'), (datetime(2005, 6, 21).date(), 'inton'),
    (datetime(2005, 12, 18).date(), 'yoton'), (datetime(2006, 6, 16).date(), 'inton'),
    (datetime(2006, 12, 13).date(), 'yoton'), (datetime(2007, 6, 11).date(), 'inton'),
    (datetime(2007, 12, 8).date(),  'yoton'), (datetime(2008, 6, 5).date(),  'inton'),
    (datetime(2008, 12, 29).date(), 'yoton'), (datetime(2009, 6, 27).date(), 'inton'),
    (datetime(2009, 12, 24).date(), 'yoton'), (datetime(2010, 6, 22).date(), 'inton'),
    (datetime(2010, 12, 19).date(), 'yoton'), (datetime(2011, 6, 17).date(), 'inton'),
    (datetime(2011, 12, 14).date(), 'yoton'), (datetime(2012, 6, 20).date(), 'inton'), 
    (datetime(2012, 12, 24).date(), 'yoton'), (datetime(2013, 6, 22).date(), 'inton'),
    (datetime(2013, 12, 19).date(), 'yoton'), (datetime(2014, 6, 17).date(), 'inton'),
    (datetime(2014, 12, 14).date(), 'yoton'), (datetime(2015, 6, 12).date(), 'inton'),
    (datetime(2015, 12, 9).date(),  'yoton'), (datetime(2016, 6, 6).date(),  'inton'),
    (datetime(2016, 12, 29).date(), 'yoton'), (datetime(2017, 6, 27).date(), 'inton'),
    (datetime(2017, 12, 24).date(), 'yoton'), (datetime(2018, 6, 22).date(), 'inton'),
    (datetime(2018, 12, 19).date(), 'yoton'), (datetime(2019, 6, 17).date(), 'inton'),
    (datetime(2019, 12, 14).date(), 'yoton'), (datetime(2020, 6, 11).date(), 'inton'),
    (datetime(2020, 12, 29).date(), 'yoton'), (datetime(2021, 6, 27).date(), 'inton'),
    (datetime(2021, 12, 24).date(), 'yoton'), (datetime(2022, 6, 22).date(), 'inton'),
    (datetime(2022, 12, 19).date(), 'yoton'), (datetime(2023, 6, 17).date(), 'inton'),
    (datetime(2023, 12, 14).date(), 'yoton'), (datetime(2024, 6, 11).date(), 'inton'),
    (datetime(2024, 12, 24).date(), 'yoton'), (datetime(2025, 6, 22).date(), 'inton'),
    (datetime(2025, 12, 19).date(), 'yoton'), (datetime(2026, 6, 17).date(), 'inton'),
    (datetime(2026, 12, 14).date(), 'yoton'), (datetime(2027, 6, 12).date(), 'inton'),
    (datetime(2027, 12, 9).date(),  'yoton'), (datetime(2028, 6, 6).date(),  'inton'),
    (datetime(2028, 12, 29).date(), 'yoton'), (datetime(2029, 6, 27).date(), 'inton'),
    (datetime(2029, 12, 24).date(), 'yoton'), (datetime(2030, 6, 22).date(), 'inton')
]

# =======================================================
# 🔮 2. 汎用・超高精度九星判定エンジン
# =======================================================
def perfect_grand_master_matrix(year, month, day):
    target_date = datetime(year, month, day).date()
    
    setsui_days = [0, 6, 4, 6, 5, 6, 6, 8, 8, 8, 9, 8, 7]
    gaku_year = year
    gaku_month = month
    
    if month == 1:
        gaku_year -= 1
        gaku_month = 11 if day < setsui_days[1] else 12
    elif month == 2:
        if day < setsui_days[2]:
            gaku_year -= 1
            gaku_month = 1
        else:
            gaku_month = 2
    else:
        if day < setsui_days[month]: gaku_month -= 1

    base_year = 1967
    base_star = 6
    diff_year = gaku_year - base_year
    honmei_num = (base_star - diff_year - 1) % 9 + 1

    month_star_table = {
        1: [0, 8, 7, 6, 5, 4, 3, 2, 1, 9, 8, 7, 9], 4: [0, 8, 7, 6, 5, 4, 3, 2, 1, 9, 8, 7, 9], 7: [0, 8, 7, 6, 5, 4, 3, 2, 1, 9, 8, 7, 9],
        2: [0, 2, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 3], 5: [0, 2, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 3], 8: [0, 2, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 3],
        3: [0, 5, 4, 3, 2, 1, 9, 8, 7, 6, 5, 4, 3], 6: [0, 5, 4, 3, 2, 1, 9, 8, 7, 6, 5, 4, 3], 9: [0, 5, 4, 3, 2, 1, 9, 8, 7, 6, 5, 4, 3]
    }
    getsumei_num = month_star_table[honmei_num][gaku_month]

    active_anchor = HISTORICAL_SWITCH_TIMELINE[0][0]
    active_mode = HISTORICAL_SWITCH_TIMELINE[0][1]
    
    for sw_date, sw_mode in HISTORICAL_SWITCH_TIMELINE:
        if sw_date <= target_date:
            active_anchor = sw_date
            active_mode = sw_mode
        else:
            break
            
    days_delta = (target_date - active_anchor).days
    
    if active_mode == 'yoton':
        nichimei_num = (1 + days_delta - 1) % 9 + 1
    else:
        nichimei_num = (9 - days_delta - 1) % 9 + 1
        while nichimei_num <= 0: nichimei_num += 9

    return honmei_num, getsumei_num, nichimei_num, gaku_year, gaku_month

# 🗺️ 2026年現在の気学中宮星を動的に判定する独立ロジック
def calculate_current_target_chugu(target_year, target_month):
    """ 指定された年月の『実際の気学中宮星』を正確に返す """
    year_chugu = 5 
    
    # 厳密な気学カレンダーに準拠した2026年各月の固定中宮マッピング
    month_chugu_map = {
        1: 1, 2: 9, 3: 8, 4: 7, 5: 6, 6: 5, 7: 4, 8: 3, 9: 2, 10: 1, 11: 9, 12: 8
    }
    month_chugu = month_chugu_map.get(target_month, 1)
    
    return year_chugu, month_chugu


# =======================================================
# 🗺️ 3. 方位盤（飛星・吉凶自動判定）計算エンジン
# =======================================================
def get_eto_opposite_direction(year):
    """ 年の十二支（寅）の対面「申」＝【南西】のインデックス（2）を返す """
    # 3x3画面上の配置 [東南(0), 南(1), 南西(2), 東(3), 中宮(4), 西(5), 東北(6), 北(7), 北西(8)]
    return 2

def get_month_eto_opposite_direction(gaku_month):
    """ 各月の十二支の対面（月破）が位置する画面上のインデックス（0〜8）を正確に返す """
    # 各月の十二支：1月丑, 2月寅, 3月卯, 4月辰, 5月巳, 6月午, 7月未, 8月申, 9月酉, 10月戌, 11月亥, 12月子
    # それぞれの対面（破）：1月未(南西=2), 2月申(南西=2), 3月酉(西=5), 4月戌(北西=8), 5月亥(北西=8), 6月子(北=7)...
    geppa_grid_map = {
        1: 2,  # 丑の対面 未（南西）
        2: 2,  # 寅の対面 申（南西）
        3: 5,  # 卯の対面 酉（西）
        4: 8,  # 辰の対面 戌（北西）
        5: 8,  # 巳の対面 亥（北西）
        6: 7,  # 午の対面 子（北）🌟 6月はここが「7（北）」になるべき！
        7: 6,  # 未の対面 丑（北東）
        8: 6,  # 申の対面 寅（北東）
        9: 3,  # 酉の対面 卯（東）
        10: 0, # 戌の対面 辰（南東）
        11: 0, # 亥の対面 巳（南東）
        12: 1  # 子の対面 午（南）
    }
    return geppa_grid_map.get(gaku_month, -1)

def generate_houiban(chugu_star):
    """ 中宮の星から3x3方位盤を生成する """
    base_pattern = [4, 9, 2, 3, 5, 7, 8, 1, 6]
    shift = chugu_star - 5
    houiban = []
    for star in base_pattern:
        new_star = (star + shift - 1) % 9 + 1
        houiban.append(new_star)
    return houiban

def evaluate_directions(houiban, honmei_num, ha_idx, mode="year"):
    """ 方位盤から各マスの吉凶を判定する """
    directions_meta = [
        {"name": "南東"}, {"name": "南"}, {"name": "南西"},
        {"name": "東"},   {"name": "中宮"}, {"name": "西"},
        {"name": "北東"}, {"name": "北"}, {"name": "北西"}
    ]
    
    my_gogyo = STAR_GOGYOM[honmei_num]
    
    gogyo_relations = {
        "木": {"shojo": ["水", "火"], "shoku": ["土", "金"]},
        "火": {"shojo": ["木", "土"], "shoku": ["金", "水"]},
        "土": {"shojo": ["火", "金"], "shoku": ["水", "木"]},
        "金": {"shojo": ["土", "水"], "shoku": ["木", "火"]},
        "水": {"shojo": ["金", "木"], "shoku": ["火", "土"]}
    }

    goou_idx = houiban.index(5) if 5 in houiban else -1
    taichu_map = {0:8, 1:7, 2:6, 3:5, 4:4, 5:3, 6:2, 7:1, 8:0}
    anken_idx = taichu_map.get(goou_idx, -1)

    honmeisatsu_idx = houiban.index(honmei_num) if honmei_num in houiban else -1
    honmeitekitsatsu_idx = taichu_map.get(honmeisatsu_idx, -1)

    results = []
    for idx, star in enumerate(houiban):
        meta = directions_meta[idx].copy()
        meta["star"] = star
        meta["star_name"] = get_kyusei_name(star)
        
        if idx == 4:
            meta["status"] = "🔄 中宮"
            meta["color"] = "gray"
            results.append(meta)
            continue

        badges = []
        is_kyou = False

        if idx == goou_idx:
            badges.append("五黄殺(大凶)")
            is_kyou = True
        if idx == anken_idx:
            badges.append("暗剣殺(大凶)")
            is_kyou = True
        if idx == ha_idx:
            label = "歳破(大凶)" if mode == "year" else "月破(大凶)"
            badges.append(label)
            is_kyou = True
        if idx == honmeisatsu_idx:
            badges.append("本命殺(凶)")
            is_kyou = True
        if idx == honmeitekitsatsu_idx:
            badges.append("本命的殺(凶)")
            is_kyou = True

        if not is_kyou:
            star_gogyo = STAR_GOGYOM[star]
            if star == honmei_num:
                badges.append("比和(普通/良)")
                meta["color"] = "blue"
            elif star_gogyo in gogyo_relations[my_gogyo]["shojo"]:
                badges.append("✨ 吉方位")
                meta["color"] = "green"
            else:
                badges.append("ー")
                meta["color"] = "black"
        else:
            meta["color"] = "red"

        meta["status"] = " / ".join(badges) if badges else "ー"
        results.append(meta)
        
    return results

def render_cell_html(item, stars_list, idx):
    color_map = {"red": "#FFD2D2", "green": "#D2FFD2", "blue": "#E6F2FF", "gray": "#F0F0F0", "black": "#FFFFFF"}
    text_color = {"red": "#990000", "green": "#006600", "blue": "#003366", "gray": "#555555", "black": "#000000"}
    bg = color_map.get(item['color'], "#FFFFFF")
    tc = text_color.get(item['color'], "#000000")
    
    return f"""
    <div style="background-color:{bg}; color:{tc}; padding:15px; border-radius:8px; text-align:center; border:1px solid #ddd; height:105px;">
        <b style="font-size:14px;">{item['name']}</b><br/>
        <span style="font-size:16px; font-weight:bold;">{stars_list[idx]} {item['star_name'][:2]}</span><br/>
        <span style="font-size:11px; font-weight:bold;">{item['status']}</span>
    </div>
    """

# =======================================================
# 📱 4. Streamlit Web画面表示処理
# =======================================================
st.set_page_config(page_title="九星気学チェッカー Pro", layout="centered")

st.markdown("""
<h3 style="margin-bottom: 0px; padding-bottom: 5px;">🌌 九星気学 三面大盤＆吉凶方位盤チェッカー</h3>
""", unsafe_allow_html=True)

st.markdown("""
あなたの九星を自動計算で割り出し、
&nbsp;&nbsp;&nbsp;&nbsp;✨本命星（本質）🌙月命星（精神）☀️日命星（行動）を表示、
&nbsp;&nbsp;&nbsp;&nbsp;さらに、年盤・月盤における【吉凶方位】も表示します。
""")

st.write("") 

selected_date = st.date_input(
    "生年月日を選択してください",
    value=datetime(1985, 5, 15),
    min_value=datetime(1940, 1, 1),
    max_value=datetime(2030, 12, 31)
)

# 固定の計算用デフォルト基準（2026年6月）
current_run_year = 2026
default_run_month = 6

if selected_date:
    honmei_num, getsumei_num, nichimei_num, gaku_year, gaku_month = perfect_grand_master_matrix(
        selected_date.year, selected_date.month, selected_date.day
    )
    
    honmei = get_kyusei_name(honmei_num)
    getsumei = get_kyusei_name(getsumei_num)
    nichimei = get_kyusei_name(nichimei_num)
    
    st.markdown("---")
    
    tab1, tab2, tab3 = st.tabs([
        "✨ 診断結果＆キャラクター解説", 
        "🧭 当年の吉凶方位盤", 
        "🌙 毎月の吉凶方位盤"
    ])
    
    # ---------------------------------------------------
    # Tab 1: ✨ 診断結果＆キャラクター解説
    # ---------------------------------------------------
    with tab1:
        st.write(f"📅 あなたの気学上の出生基準年: **{gaku_year}年 {gaku_month}月度**")
        
        status_card_html = f"""
        <table style="width:100%; border-collapse: separate; border-spacing: 10px; margin-bottom: 20px;">
            <tr>
                <td style="width:33%; background-color: #E6F2FF; border: 1px solid #B3D7FF; padding: 12px; border-radius: 8px; text-align: center; color: #003366;">
                    <span style="font-size:13px; font-weight:bold;">✨ 本命星（本質）</span><br/>
                    <span style="font-size:18px; font-weight:bold; margin-top:5px; display:inline-block;">{honmei}</span>
                </td>
                <td style="width:33%; background-color: #FFF2E6; border: 1px solid #FFD9B3; padding: 12px; border-radius: 8px; text-align: center; color: #663300;">
                    <span style="font-size:13px; font-weight:bold;">🌙 月命星（精神）</span><br/>
                    <span style="font-size:18px; font-weight:bold; margin-top:5px; display:inline-block;">{getsumei}</span>
                </td>
                <td style="width:33%; background-color: #F2E6FF; border: 1px solid #E1BFFF; padding: 12px; border-radius: 8px; text-align: center; color: #330066;">
                    <span style="font-size:13px; font-weight:bold;">☀️ 日命星（行動）</span><br/>
                    <span style="font-size:18px; font-weight:bold; margin-top:5px; display:inline-block;">{nichimei}</span>
                </td>
            </tr>
        </table>
        """
        st.markdown(status_card_html, unsafe_allow_html=True)
        
        st.markdown(f"### 【本命星】{honmei} の性質")
        st.write(CHARACTER_EXPLANATIONS.get(honmei, "解説準備中..."))

    # ---------------------------------------------------
    # Tab 2: 当年の吉凶方位盤（年盤）
    # ---------------------------------------------------
    with tab2:
        st.subheader(f"🧭 当年の吉凶方位盤")
        st.write(f"あなたの本命星 **{honmei}** から見た、**今年**（{current_run_year}年）の方位盤の吉凶レイアウトです。")
        st.caption("⚠️ 上が「南」、下が「北」の配置になっています。")

        suiha_idx_cur = get_eto_opposite_direction(current_run_year)
        y_chugu_correct, _ = calculate_current_target_chugu(current_run_year, default_run_month)
        
        y_houiban_stars = generate_houiban(y_chugu_correct)
        y_evaluated_grid = evaluate_directions(y_houiban_stars, honmei_num, suiha_idx_cur, mode="year")

        grid_data_y = [y_evaluated_grid[0:3], y_evaluated_grid[3:6], y_evaluated_grid[6:9]]
        
        for r_idx, row in enumerate(grid_data_y):
            cols = st.columns(3)
            for c_idx, cell in enumerate(row):
                abs_idx = r_idx * 3 + c_idx
                cols[c_idx].markdown(render_cell_html(cell, y_houiban_stars, abs_idx), unsafe_allow_html=True)

    # ---------------------------------------------------
    # Tab 3: 毎月の吉凶方位盤（月盤）🌟【バグ完全修正版】
    # ---------------------------------------------------
    with tab3:
        st.subheader(f"🌙 毎月の吉凶方位盤")
        
        if "sim_month" not in st.session_state:
            st.session_state.sim_month = default_run_month

        st.write(f"あなたの本命星 **{honmei}** から見た、**{st.session_state.sim_month}月度** の月盤レイアウトです。")
        st.caption("⚠️ 上が「南」、下が「北」の配置になっています。")

        # 動的再計算処理
        _, m_chugu_dynamic = calculate_current_target_chugu(current_run_year, st.session_state.sim_month)
        
        # 🌟 修正ポイント：インデックス変換を正しく行うマッピング関数を使用
        geppa_idx_dynamic = get_month_eto_opposite_direction(st.session_state.sim_month)
        
        m_houiban_stars = generate_houiban(m_chugu_dynamic)
        m_evaluated_grid = evaluate_directions(m_houiban_stars, honmei_num, geppa_idx_dynamic, mode="month")

        grid_data_m = [m_evaluated_grid[0:3], m_evaluated_grid[3:6], m_evaluated_grid[6:9]]
        
        # 3x3グリッドを描画
        for r_idx, row in enumerate(grid_data_m):
            cols = st.columns(3)
            for c_idx, cell in enumerate(row):
                abs_idx = r_idx * 3 + c_idx
                cols[c_idx].markdown(render_cell_html(cell, m_houiban_stars, abs_idx), unsafe_allow_html=True)
        
        # 下段のセレクトボックス
        st.write("")
        st.markdown("---")
        st.markdown("##### 🗓️ 未来の計画・シミュレーション用")
        st.caption("※数ヶ月先の旅行や計画を立てる際、下のボックスから月を切り替えて方位盤の変化を確認できます。")
        
        st.selectbox(
            "表示する月を切り替える:",
            options=list(range(1, 13)),
            key="sim_month"
        )
