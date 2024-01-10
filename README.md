# Программирование мобильных устройств и встраиваемых приложений

Разработана система распознавания движения на базе python-opencv, которая при обнаружении "вторжения" в холодьник осуществляет запись "преступления". Запись сопровождается громким звуковым и световым сигналами, подобно другим охранным системам.

Управление системой осуществляется с помощью мобильного приложения на Android

Псевдоним | ФИО | Группа
--- | --- | ---
KopeykinDmitriy | Копейкин Дмитрий Евгеньевич | РИС-20-1б
Schtinguerch | Шумилов Лев Сергеевич | РИС-20-1б
SpidiMun | Ознобихин Елисей Андреевич | РИС-20-1б

Тестовый стенд представлен на фото

![image](https://github.com/Schtinguerch/orangepi-fridge-observer/assets/67968183/c8e3f9db-3396-46ec-a239-cb9499e48cf3)

<h2>Настройка автозапуска</h2>
В директории /etc/systemd/system создаём файл thief_detector.service со следующим скриптом:


```
[Unit]
Description=Thief detector
After=multi-user.target

[Service]
Type=idle
ExecStart=hypercorn main:app --access-logfile=access.log --error-logfile=errors.log
WorkingDirectory=/home/schtinguerch/Documents/gpio_test/CAMERA
User=root

[Install]
WantedBy=multi-user.target
```
После чего выполняем следующие команды:

```
sudo systemctl daemon-reload
sudo systemctl enable thief_detector.service
sudo systemctl start thief_detector.service 
```

