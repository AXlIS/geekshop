from django.shortcuts import render


def index(request):
    return render(request, 'mainapp/index.html')


def products(request):
    context = {
        'products': [
            {'title': 'Худи черного цвета с монограммами adidas Originals',
             'img': 'vendor/img/products/Adidas-hoodie.png', 'price': '6 090,00 руб.',
             'description': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.'},
            {'title': 'Синяя куртка The North Face', 'img': 'vendor/img/products/Blue-jacket-The-North-Face.png',
             'price': '23 725,00 руб.',
             'description': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.'},
            {'title': 'Коричневый спортивный oversized-топ ASOS DESIGN',
             'img': 'vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png', 'price': '3 390,00 руб.',
             'description': 'Материал с плюшевой текстурой. Удобный и мягкий.'},
            {'title': 'Черный рюкзак Nike Heritage', 'img': 'vendor/img/products/Black-Nike-Heritage-backpack.png',
             'price': '2 340,00 руб.', 'description': 'Плотная ткань. Легкий материал.'},
            {'title': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex',
             'img': 'vendor/img/products/Black-Dr-Martens-shoes.png', 'price': '13 590,00 руб.',
             'description': 'Гладкий кожаный верх. Натуральный материал.'},
            {'title': 'Темно-синие широкие строгие брюки ASOS DESIGN',
             'img': 'vendor/img/products/Dark-blue-wide-leg-ASOs-DESIGN-trousers.png', 'price': '2 890,00 руб.',
             'description': 'Легкая эластичная ткань сирсакер Фактурная ткань.'},
        ]
    }
    return render(request, 'mainapp/products.html', context)


def test_context(request):
    context = {
        'title': 'добро подаловать!',
        'username': 'Igor Svistun',
        'products': [
            {'name': 'Черное худи', 'price': '2 990 руб.'},
            {'name': 'Джинсы', 'price': '5 800 руб.'}
        ],
        'promotion': True,
        'promotion_products': [
            {'name': 'Туфли Dr.Martens', 'price': '10 000 руб.'}
        ],
    }
    return render(request, 'mainapp/context.html', context)
