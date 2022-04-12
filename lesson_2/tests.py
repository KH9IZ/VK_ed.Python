#!/usr/bin/env python3
import unittest
from unittest.mock import patch
import factory
import html_parser


class Base:
    link = None
    text = None


class ArticleFactory(factory.Factory):
    link = factory.Faker("uri")
    text = factory.Faker("text")

    class Meta:
        model = Base


class HTMLParserTestCase(unittest.TestCase):
    def setUp(self):
        self.calls = []

    def open_tag(self, tag):
        self.calls.append(f"{tag} opened")

    def close_tag(self, tag):
        self.calls.append(f"{tag} closed")

    def data_process(self, tag, data):
        self.calls.append(f"from {tag} {data} processed")

    @patch("__main__.HTMLParserTestCase.open_tag", return_value=None)
    @patch("__main__.HTMLParserTestCase.close_tag", return_value=None)
    @patch("__main__.HTMLParserTestCase.data_process", return_value=None)
    def test_html_parser_mock(self, open_tag, close_tag, data_process):
        html = r" \t<html><div><div>div</div></div></html>\n\n"
        html_parser.parse_html(html, open_tag, data_process, close_tag)
        self.assertEqual(open_tag.call_count, 3)
        self.assertEqual(close_tag.call_count, 3)
        self.assertEqual(data_process.call_count, 3)

    def test_html_parser(self):
        html = ""
        html_parser.parse_html(html, self.open_tag, self.data_process, self.close_tag)
        self.assertListEqual(self.calls, [])
        html = "<H1></H1><h2 font='awesome'></h2>"
        html_parser.parse_html(html, self.open_tag, self.data_process, self.close_tag)
        self.assertListEqual(
            self.calls,
            [
                "H1 opened",
                "H1 closed",
                "from H1  processed",
                "h2 opened",
                "h2 closed",
                "from h2  processed",
            ],
        )
        self.calls = []
        html = " \t\n\t<div> first <p>/p</p> second </div> passed"
        html_parser.parse_html(html, self.open_tag, self.data_process, self.close_tag)
        self.assertListEqual(
            self.calls,
            [
                "div opened",
                "p opened",
                "p closed",
                "from p /p processed",
                "div closed",
                "from div  first  second  processed",
            ],
        )
        self.calls = []
        html = """<html>
    <head></head>
    <body>
        <h1>Header1</h1>
        <p>TEXT</p>
    </body>
    <footer>
    </footer>
</html>"""
        html_parser.parse_html(html, self.open_tag, self.data_process, self.close_tag)
        self.assertListEqual(
            self.calls,
            [
                "html opened",
                "head opened",
                "head closed",
                "from head  processed",
                "body opened",
                "h1 opened",
                "h1 closed",
                "from h1 Header1 processed",
                "p opened",
                "p closed",
                "from p TEXT processed",
                "body closed",
                "from body \n        \n        \n     processed",
                "footer opened",
                "footer closed",
                "from footer \n     processed",
                "html closed",
                "from html \n    \n    \n    \n processed",
            ],
        )

    def test_factory_boy_tests(self):
        article = ArticleFactory.stub()
        href = article.link
        text = article.text
        html = f'<a href="{href}">link</a><body>{text}</body>'
        html_parser.parse_html(html, self.open_tag, self.data_process, self.close_tag)
        self.assertListEqual(
            self.calls,
            [
                "a opened",
                "a closed",
                "from a link processed",
                "body opened",
                "body closed",
                f"from body {text} processed",
            ],
        )


if __name__ == "__main__":
    unittest.main()
