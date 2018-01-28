#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class HtmlOutputer(object):

    def __init__(self):
        self.datas = []

    def collect_data(self, new_data):
        if new_data is None:
            return

        self.datas.append(new_data)

    def output_html(self):

        fout = open('output.html', 'w', encoding='utf-8')
        fout.write('<html><head><meta charset="UTF-8"></head>')
        fout.write('<body>')

        fout.write('<table border="1" cellspacing="0" cellpadding="0">')
        for data in self.datas:
            fout.write('<tr>')
            fout.write('<th>{0}</th>'.format(data['title'].replace(u'\xa0', u' ').encode('utf-8').decode('utf-8')))
            fout.write('<td>{0}\n{1}</td>'.format(data['url'].replace(u'\xa0', u' ').encode('utf-8').decode('utf-8'), data['summary'].replace(u'\xa0', u' ').encode('utf-8').decode('utf-8')))
            fout.write('</tr>')

        fout.write("</table>")

        fout.write('</body>')
        fout.close()
