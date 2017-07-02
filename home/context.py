from models import Category, LargeCategory


def common_context_processor(context):
    categories = Category.objects.all()
    large_categories = LargeCategory.objects.all()

    return {
        'large_categories': large_categories,
        'categories': categories,
    }
