import streamlit as st
from datetime import datetime, date

# 十干
heavenly_stems = ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"]

def calculate_day_pillar_ten_stem(birth_date):
    """日柱の十干を計算（男女共通）"""
    base_date = datetime(1900, 1, 1)  # 基準日
    base_stem = 0  # 十干の基準（甲）
    
    # 誕生日から基準日までの日数を計算
    delta_days = (birth_date - base_date.date()).days
    
    # 十干の計算
    heavenly_stem_index = (base_stem + delta_days) % 10
    
    # 日柱の十干を算出
    return heavenly_stems[heavenly_stem_index]

# Streamlit アプリ
st.title("四柱推命 日柱の十干計算ツール")
st.write("1900年〜2100年の誕生日に対応しています。")

# 入力フォーム
birth_date = st.date_input("生年月日を選んでください", value=date(2000, 1, 1), min_value=date(1900, 1, 1), max_value=date(2100, 12, 31))

if st.button("計算する"):
    # 日柱の十干を計算（男女共通）
    day_pillar_ten_stem = calculate_day_pillar_ten_stem(birth_date)
    
    # 結果表示
    st.write(f"生年月日: {birth_date}")
    st.write(f"日柱の十干: {day_pillar_ten_stem}")