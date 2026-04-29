#!/bin/sh

# Проверяем аргумент
if [ -z "$1"]  
    then ARG="../ex02/hh_sorted.csv" 
    else ARG="$1"  
fi

# Функция нормализации уровней позиций
cleaner()
{
    awk -F "\"," 'BEGIN{
        OFS = FS}{
        # Анализ и нормализация третьего поля (должность)
        if (tolower($3) ~ "junior" && tolower($3) ~ "middle" && tolower($3) ~ "senior")
            $3 = "\"Junior/Middle/Senior"      # Все три уровня
        else if (tolower($3) ~ "junior" && tolower($3) ~ "middle")
            $3 = "\"Junior/Middle"             # Junior + Middle
        else if (tolower($3) ~ "junior" && tolower($3) ~ "senior")
            $3 = "\"Junior/Senior"             # Junior + Senior  
        else if (tolower($3) ~ "middle" && tolower($3) ~ "senior")
            $3 = "\"Middle/Senior"             # Middle + Senior
        else if (tolower($3) ~ "junior")
            $3 = "\"Junior"                    # Только Junior
        else if (tolower($3) ~ "senior")
            $3 = "\"Senior"                    # Только Senior
        else if (tolower($3) ~ "middle")
            $3 = "\"Middle"                    # Только Middle
        else
            $3 = "\"-"                         # Уровень не найден
        print $0}'  # Вывод обработанной строки
}

# Создаем файл с заголовком
cat $ARG | head -n 1 > "hh_positions.csv"

# Обрабатываем все строки и добавляем в файл
cat < $ARG | while read -r; do cleaner >> "hh_positions.csv"; done