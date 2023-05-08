import os
import dotenv

# Это файл настройки, для того чтобы пароли и логины не были в коде
# были вынесены в отдельный файл,data_file.env
# удобно редактрровать данные
# и безопасно
# обычно данный data_file.env файл не отправляется а гитхаб,
# но так как данный ресурс reqres.in открыт, то для демонcтрации был отправлен

dotenv.load_dotenv('data_file.env')

name = os.environ['name']
name_1 = os.environ['name']
name_2 = os.environ['name']
job = os.environ['job']
job_1 = os.environ['job_1']
job_2 = os.environ['job_1']
email = os.environ['email']
email_1 = os.environ['email_1']
email_2 = os.environ['email_2']
email_3 = os.environ['email_2']
password = os.environ['password']
password_1 = os.environ['password_1']

