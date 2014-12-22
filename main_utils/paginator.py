# django
from django.core.paginator import Paginator


def get_page(object_list, per_page, page_no):
    paginator = Paginator(object_list, per_page)
    if page_no < 1:
        page_no = 1
    if page_no > paginator.num_pages:
        page_no = paginator.num_pages
    return paginator.page(page_no)


def get_page_from_request(object_list, request):
    """
    For this project only
    """

    try:
        page_no = int(request.GET.get('page', 1))
    except (ValueError, TypeError):
        page_no = 1

    return get_page(object_list, request.user.account.rows_on_page, page_no)
