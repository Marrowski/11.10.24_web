#ApacheBench - однопотокова програма для командної строки, яка вимірює продуктивність HTTP веб-серверів.
#Програма підходить для тестування будь-якого веб-сервера

#Для встановлення необхідна unix-подібна система, якщо вона є, виконуємо такі кроки:
#Оновлення списку пакетів в репозиторіях: apt update
#Встановлення пакету утиліт apache2: apt install apache2-utils
#Перевірка встановлення ApacheBench: ab -V

#ВАЖЛИВО: ApacheBench слід запускати тільки на тих серверах, якими ви володієте або є право на тестування.
#У деяких країнах використання ApacheBench без дозволу власника серверу вважається злочином і може нести покарання.

#Тестування: # ab -n 100 -c 10 https://blog.sedicomm.com/
#Де https://blog.sedicomm.com/ - посилання; #100 - кількість запитів до сайту; 10 - одночасне виконання запитів.

