3. Фильтр: найдите все наблюдения, где count > 500 — сколько их? В какое время года чаще всего?
high_count = df_1[df_1['count'] > 500]
num_observations = len(high_count)
print(f"Количество наблюдений, где count > 500: {num_observations}")

season_counts = high_count.groupby('season').size()
most_common_season = season_counts.idxmax()
print(f"\nЧаще всего count > 500 происходит в сезоне: {most_common_season}")