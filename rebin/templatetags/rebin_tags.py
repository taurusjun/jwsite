import re
from django import template
from django.utils.html import format_html
register = template.Library()

@register.simple_tag()
def standardComments(accm):
    username = accm['username']
    cid = accm['cid']
    quoteid = accm['quoteid']
    postdate = accm['postdate']
    content = accm['content']
    conts = re.sub(re.compile(r"(\[img=[^\]]*?\])(.*?)(\[/img\])", re.S), dashrepl, content)
    count = accm['count']
    templateEle = '''
        <div class="media" style="margin-top: 2px;">
          <a href="#" class="pull-left">
          <div>-</div>
          </a>
          <div class="media-body">
            <h4 class="media-heading comment-head">#%s %s <span>%s / <a href="#">Reply</a></span></h4>
            <p class="comment-content">%s</p>
          </div>
        </div>
    '''%(count,username,postdate,conts)

    return format_html(templateEle)

def dashrepl(matchobj):
    img = matchobj.group(2)
    html='''
    <img src="%s"/>
    '''%img
    return format_html(html)

@register.simple_tag()
def quotedComments(quotes):
    templateEle=''
    if len(quotes) > 0:
        contents = quotedCommentContents(quotes)
        templateEle = '''
            <div class="comment-quote">
            %s
            </div>
        '''%contents
    return format_html(templateEle)

def quotedCommentContents(quotes):
    templateEle=''

    if len(quotes) > 0:
        last_item = quotes.pop()
        username = last_item['username']
        cid = last_item['cid']
        quoteid = last_item['quoteid']
        postdate = last_item['postdate']
        content = last_item['content']
        count = last_item['count']
        ref = quotedCommentContents(quotes)
        templateEle = '''
            <div class="media">
              <a href="#" class="pull-left">
              <div>-</div>
              </a>
              <div class="media-body">
                <h4 class="media-heading comment-head">#%s %s <span>%s / <a href="#">Reply</a></span></h4>
                <p class="comment-content">%s</p>
                %s
              </div>
            </div>
        '''%(count,username,postdate,content,ref)

    return format_html(templateEle)

