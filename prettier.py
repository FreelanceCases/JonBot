def bonus_history_formatter(arr):

    result = "История транзакций:\n"
    index = 1
    for (date, count) in arr:
        if count < 0:
            count *= -1
            result += str(index) + ". Списание: " + str(count) + " бонусов.\nДата: " + date + ". \n\n"
        else: 
            result += str(index) + ". Получено: " + str(count) + " бонусов.\nДата: " + date + ". \n\n"
        index += 1
    return result


def bonus_balance_formatter(num):
    result = "Ваш остаток: " + str(num) + " бонусов."
    return result