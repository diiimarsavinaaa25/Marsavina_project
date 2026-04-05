#1. Найдите час суток с максимальным числом поездок в выходные дни
weekend_data = df_1[df_1['workingday'] == 0]
hourly_count = weekend_data.groupby(weekend_data['datetime'].dt.hour)['count'].sum()
max_hour = hourly_count.idxmax()
print(f"Час с максимальным числом поездок в выходные: {max_hour}:00")