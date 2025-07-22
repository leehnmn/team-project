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
