from django.template.loader_tags import register


@register.inclusion_tag("comment.html")
def place_comment(comment):
    print(comment)
    return {'comment': comment}