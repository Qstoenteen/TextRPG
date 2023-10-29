import cv2
import datetime

# Задаем путь к папке для сохранения изображений
output_folder = 'Q:\screens'

current_time = datetime.datetime.now()
time_str = current_time.strftime('%Y-%m-%d_%H-%M')
image_name = f'{time_str}.jpg'
output_file = os.path.join(output_folder, image_name)

    # Получаем изображение с камеры
cap = cv2.VideoCapture(0)
ret, frame = cap.read()
cap.release()

# Сохраняем изображение
cv2.imwrite(output_file, frame)
print(f"Сохранено изображение {image_name}")