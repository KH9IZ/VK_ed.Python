import re


def parse_html(html: str, open_tag_callback, data_callback, close_tag_callback):
    template = r"([^<]*)<\s*([a-zA-Z0-9]+)\s*[^>]*>(.*)<\/\2>(.*$)"
    match = re.match(template, html, re.DOTALL)
    if match:
        prefix, tag, raw_body, raw_postfix = match.groups()
        open_tag_callback(tag)
        body = parse_html(
            raw_body, open_tag_callback, data_callback, close_tag_callback
        )
        close_tag_callback(tag)
        data_callback(tag, body)
        postfix = parse_html(
            raw_postfix, open_tag_callback, data_callback, close_tag_callback
        )
        return prefix + postfix
    return html
