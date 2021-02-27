## The Verge ##
target_1 = {
    'home_link': 'https://www.theverge.com/',
    'get_links': '//div/h2[@class="c-entry-box--compact__title"]/a/@href',
    'detail_get_title': '//h1[@class="c-page-title"]/text()',
    'detail_get_summary': '//div[@class="c-entry-hero c-entry-hero--default "]/p/text()',
    'detail_get_text': '//div[@class="c-entry-content "]/p/text()',
}

## LaRepublica ##
target_2 = {
    'home_link':'https://www.larepublica.co/',
    'get_links':'//div[@class="col mb-4"]/div[@class="news V_Title_Img"]/text-fill/a/@href',
    'get_news_title':'//text-fill[not(@class)]/span/text()',
    'get_news_summary':'//div[@class="lead"]/p/text()',
    'get_news_body':'//div[@class="html-content"]/p[not(@class)]/text()',
}
