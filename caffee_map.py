import pandas as pd
import matplotlib.pyplot as plt

# CSV 불러오기 (혹은 분석 결과에서 바로 사용 가능)
df = pd.read_csv('area1_data.csv')

# 'ConstructionSite'가 1인 경우 struct 이름 변경
df.loc[df['ConstructionSite'] == 1, 'struct'] = 'ConstructionSite'

# struct 값이 없는 경우 '기타'로 채우기
df['struct'] = df['struct'].fillna('기타')

# 구조물 종류별 개수 집계
summary = df['struct'].value_counts().reset_index()
summary.columns = ['구조물 종류', '개수']

# 📊 막대 그래프 생성
plt.figure(figsize=(8, 6))
plt.bar(summary['구조물 종류'], summary['개수'], color='skyblue')
plt.title('구조물 종류별 통계')
plt.xlabel('구조물 종류')
plt.ylabel('개수')
plt.xticks(rotation=45)
plt.tight_layout()

# 이미지로 저장
plt.savefig('structure_summary_chart.png')
plt.show()

# 1단계 보너스 과제
import pandas as pd

# 데이터 불러오기
df = pd.read_csv('area1_data.csv')

# Construction Site가 표시된 구획 처리
df.loc[df['ConstructionSite'] == 1, 'struct'] = 'Construction Site'

# 구조물 이름이 비어있는 경우 '기타'로 채우기
df['struct'] = df['struct'].fillna('기타')

# 내 집 좌표에 'My House' 지정 (x=14, y=2 기준)
df.loc[(df['x'] == 14) & (df['y'] == 2), 'struct'] = 'My House'

# 구조물 종류 영문 표기로 통일
name_map = {
    'Apartment': 'Apartment',
    'Building': 'Buildings',
    'BandalgomCoffee': 'Bandalgom_Cafe',
    'Construction Site': 'Construction Site',
    'My House': 'My House'
}
df['struct'] = df['struct'].replace(name_map)

# 전체 구조물 수
total_count = len(df)

# 전체 건축물 구획수 (공사현장 제외)
non_construction = df[df['struct'] != 'Construction Site']
total_buildings = len(non_construction)

# 구조물 종류별 통계
total_stats = df['struct'].value_counts()

# 전역 통계 출력
print('[전역 구조물 현황]')
print(f'전체 구조물 갯수 = {total_count}개')
print(f'전체 건축물 구획수 = {total_buildings}개')
print(f'전체 Construction Site 구획수 = {total_stats.get("Construction Site", 0)}개')
print(f'Apartment 갯수 = {total_stats.get("Apartment", 0)}개')
print(f'Buildings 갯수 = {total_stats.get("Buildings", 0)}개')
print(f'My House 갯수 = {total_stats.get("My House", 0)}개')
print(f'Bandalgom_Cafe 갯수 = {total_stats.get("Bandalgom_Cafe", 0)}개\n')

# Area별 요약 출력 함수
def print_area_summary(area_number):
    area_df = df[df['area'] == area_number]
    stats = area_df['struct'].value_counts()
    building_count = len(area_df[area_df['struct'] != 'Construction Site'])
    construction_count = stats.get('Construction Site', 0)

    print(f'[Area {area_number} 구조물 현황]')
    print(f'건축물 구획수 = {building_count}개')
    print(f'Construction Site 구획수 = {construction_count}개')
    if stats.get('Apartment', 0):
        print(f'Apartment 갯수 = {stats["Apartment"]}개')
    if stats.get('Buildings', 0):
        print(f'Buildings 갯수 = {stats["Buildings"]}개')
    if stats.get('My House', 0):
        print(f'My House 갯수 = {stats["My House"]}개')
    if stats.get('Bandalgom_Cafe', 0):
        print(f'Bandalgom_Cafe 갯수 = {stats["Bandalgom_Cafe"]}개')
    print('')

# 모든 구역 반복 출력
for area in sorted(df['area'].unique()):
    print_area_summary(area)
