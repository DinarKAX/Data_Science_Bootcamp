# Проверяем наличие аргумента 
if [ -z "$1" ]
    then ARG="../ex01/hh.csv"
    else ARG="$1"
fi

# Создаем файл с заголовком
cat $ARG | head -n 1 > "hh_sorted.csv"

# Добавляем отсортированные данные (последние 20 строк)
cat $ARG | tail -n 20 | sort -t "," -k 2 -k 1n >> "hh_sorted.csv"