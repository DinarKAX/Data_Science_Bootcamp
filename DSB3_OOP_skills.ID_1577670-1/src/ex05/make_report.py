import sys
import os
from analytics import Research
from config import num_of_steps, report_template

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python make_report.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    
    # Проверка существования файла
    if not os.path.exists(file_path):
        print(f"Error: {file_path} not exists")
        sys.exit(1)
    if not os.path.isfile(file_path):
        print(f"Error: {file_path} is not file")
        sys.exit(1)
        
    try:
        # Инициализация и получения данных
        research = Research(file_path)
        data = research.file_reader()

        # Выполнение калькулятора
        calculations = research.Calculations(data)
        count_res = calculations.counts()
        fraction_res = calculations.fractions()
        
        # Выполение аналитики
        analytics = research.Analytics(data)
        prediction_random = analytics.predict_random(num_of_steps)
        
        # Форматирование предсказаний для отчета
        predictions_str = ', '.join(str(pred) for pred in prediction_random)
        
        # Создание отчета
        report = report_template.format(
            observations=len(data),
            tails=count_res[1],
            heads=count_res[0],
            tails_pct=fraction_res[1] * 100,
            heads_pct=fraction_res[0] * 100,
            num_predictions=num_of_steps,
            predictions_str=predictions_str
        )

        # Сохранение отчета в файл
        result = analytics.save_file(report, 'ex05/report', 'txt')
        print(result)
        
        # Вывод отчета в консоль
        print(report)

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)