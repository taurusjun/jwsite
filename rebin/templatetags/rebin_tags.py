from django import template

from django.utils.html import format_html
register = template.Library()

@register.simple_tag()
def quotedComments(quotes):
    templateEle=''

    if len(quotes) > 0:
        last_item = quotes.pop()
        username = last_item['username']
        cid = last_item['cid']
        quoteid = last_item['quoteid']
        postdate = last_item['postdate']
        content = last_item['content']
        ref = quotedComments(quotes)
        templateEle = '''
            <div class="media">
              <a href="#" class="pull-right">
              <div>-</div>
              </a>
              <div class="media-body">
                <h4 class="media-heading">%s %s|ref:%s <span>%s / <a href="#">Reply</a></span></h4>
                <p>%s</p>
                %s
              </div>
            </div>
        '''%(username,cid,quoteid,postdate,content,ref)

    return format_html(templateEle)

