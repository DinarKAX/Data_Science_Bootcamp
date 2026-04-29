#!/bin/bash


if [ -z "$1" ]
    then ARG="../ex03/hh_positions.csv" 
    else ARG="$1" 
fi

# Создаем файл с заголовком
echo "name","count" > "hh_uniq_positions.csv"

# Обработка данных и подсчет уникальных позиций
tail -n 20 $ARG | cut -f 3 -d ',' | sort | uniq -ci \
| while read -r line; do 
    words=($line)  # Разбиваем строку на слова
    echo "${words[1]}", "${words[0]}" >> "hh_uniq_positions.csv"  # :название, количество
  done