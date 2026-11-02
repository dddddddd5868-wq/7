from django.db import models


class CompanyInfo(models.Model):
	name = models.CharField('Название компании', max_length=200)
	description = models.TextField('Описание')
	logo = models.ImageField('Логотип', upload_to='logos/')
	phone = models.CharField('Номер телефона', max_length=50)
	email = models.EmailField('Email')
	address = models.CharField('Адрес', max_length=255)
	socials = models.TextField(
		'Ссылки на соцсети',
		blank=True,
		help_text='Каждая соцсеть с новой строки в формате: IG|https://instagram.com',
	)

	class Meta:
		verbose_name = 'Информация о компании'
		verbose_name_plural = 'Информация о компании'

	def __str__(self):
		return self.name

	@property
	def phone_link(self):
		return ''.join(character for character in self.phone if character.isdigit() or character == '+')

	@property
	def socials_list(self):
		result = []
		for line in self.socials.splitlines():
			if '|' in line:
				label, url = line.split('|', 1)
				result.append({'label': label.strip(), 'url': url.strip()})
		return result


class Service(models.Model):
	title = models.CharField('Название услуги', max_length=200)
	description = models.TextField('Описание')
	price = models.DecimalField('Цена', max_digits=12, decimal_places=0)
	image = models.ImageField('Изображение', upload_to='services/')

	class Meta:
		verbose_name = 'Услуга'
		verbose_name_plural = 'Услуги'
		ordering = ['id']

	def __str__(self):
		return self.title
