import pygal
pie_chart = pygal.Pie()
pie_chart.title = '中国各星座人口比例（%)'
pie_chart.add('天蝎', 15.74)
pie_chart.add('射手', 9.86)
pie_chart.add('双子', 9.97)
pie_chart.add('金牛', 9.31)
pie_chart.add('巨蟹', 9.27)
pie_chart.add('白羊', 8.66)
pie_chart.add('水瓶', 6.85)
pie_chart.add('狮子', 6.70)
pie_chart.add('双鱼', 6.40)
pie_chart.add('天秤', 6.31)
pie_chart.add('摩羯', 5.75)
pie_chart.add('处女',5.36 )
pie_chart.render()
pie_chart.render_to_file('language1.svg')