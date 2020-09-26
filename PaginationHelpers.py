PAGE_SIZE_DEFAULT = 30


def normalize_pagination_parameters(page, page_size):
    if page is None or int(page) > 30 or int(page) <= 0:
        page = 1  # default value
    if page_size is None or int(page_size) > 30 or int(page_size) <= 0:
        page_size = PAGE_SIZE_DEFAULT
    return int(page), int(page_size)


def get_pagination_parameters_from_http_context(request):
    page = request.args.get('page')
    page_size = request.args.get('page_size')

    page, page_size = normalize_pagination_parameters(page, page_size);
    return page, page_size
