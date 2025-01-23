
team1_num = 5
print('В команде Мастера кода учасников: %s' % (team1_num), '!')
team2_num = 6
print('Итого сегодня в командахучасников: %s и %s' % (team1_num, team2_num), '!')
score_2 = 42
print('Команда волшебники данных решила задач: {} !'. format(42))
team1_time = 18015.2
team2_time = 10717.6
print('Волшебники данных решили задачи за {} c!'.format(team1_time))
score_1 = 40
print(f'Команды решили {score_1} и {score_2} задач.')

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    result = 'Победа команды Волшебники Данных!'
else:
    result = 'Ничья!'

challenge_result = result
print(f'Результат битвы: {challenge_result}')

tasks_total = score_1 + score_2
time_avg = (team1_time + team2_time) / tasks_total

print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg.__round__(1)} секунды на задачу!.')
