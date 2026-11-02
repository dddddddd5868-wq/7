from shutil import copy2

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from config.models import CompanyInfo, Service


class Command(BaseCommand):
    help = 'Копирует изображения-заглушки и заполняет сайт тестовыми данными.'

    def handle(self, *args, **options):
        image_names = (
            'logo.svg',
            'service1.svg',
            'service2.svg',
            'service3.svg',
        )
        image_source = settings.BASE_DIR / 'static' / 'img'
        missing_images = [name for name in image_names if not (image_source / name).is_file()]
        if missing_images:
            missing_list = ', '.join(missing_images)
            raise CommandError(f'Не найдены обязательные изображения в static/img/: {missing_list}')

        media_root = settings.MEDIA_ROOT
        (media_root / 'logos').mkdir(parents=True, exist_ok=True)
        (media_root / 'services').mkdir(parents=True, exist_ok=True)
        copy2(image_source / 'logo.svg', media_root / 'logos' / 'logo.svg')
        for image_name in ('service1.svg', 'service2.svg', 'service3.svg'):
            copy2(image_source / image_name, media_root / 'services' / image_name)

        company_data = {
            'name': 'DigitalHub',
            'description': 'Создаём сайты, мобильные приложения и digital-стратегии, которые помогают бизнесу расти.',
            'phone': '+7 (700) 123-45-67',
            'email': 'info@digitalhub.kz',
            'address': 'г. Алматы, пр. Абая, 150',
            'socials': '\n'.join((
                'IG|https://instagram.com',
                'TG|https://t.me',
                'WA|https://wa.me/77001234567',
                'YT|https://youtube.com',
            )),
        }
        company = CompanyInfo.objects.first()
        if company is None:
            company = CompanyInfo.objects.create(**company_data, logo='logos/logo.svg')
        else:
            for field, value in company_data.items():
                setattr(company, field, value)
            company.logo.name = 'logos/logo.svg'
            company.save()

        services = (
            {
                'title': 'Веб-разработка',
                'description': 'Лендинги, корпоративные сайты и интернет-магазины на современных технологиях с адаптивной вёрсткой.',
                'price': 150000,
                'image': 'services/service1.svg',
            },
            {
                'title': 'Мобильные приложения',
                'description': 'Разработка приложений для iOS и Android: от прототипа и дизайна до публикации в магазинах.',
                'price': 400000,
                'image': 'services/service2.svg',
            },
            {
                'title': 'SEO и продвижение',
                'description': 'Выводим сайт в топ поисковых систем, настраиваем рекламу и аналитику для роста продаж.',
                'price': 90000,
                'image': 'services/service3.svg',
            },
        )
        for service_data in services:
            Service.objects.update_or_create(
                title=service_data['title'],
                defaults=service_data,
            )

        self.stdout.write(self.style.SUCCESS('Данные компании и три услуги созданы или обновлены.'))