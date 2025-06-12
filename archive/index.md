---
layout: default
title: 历史讲座汇总
permalink: /archive
---

# 历史讲座汇总

{% assign events_by_year = site.data.events.events | group_by_exp: "event", "event.date | date: '%Y'" | sort: "name" | reverse %}

{% for year in events_by_year %}
## {{ year.name }}年

{% assign events_by_month = year.items | group_by_exp: "event", "event.date | date: '%m'" | sort: "name" | reverse %}

{% for month in events_by_month %}
### {{ month.name }}月

{% for event in month.items %}
- **{{ event.speaker }}** ({{ event.institution }})
  - 主题：*{{ event.title }}*
  - 日期：{{ event.date | date: "%Y年%m月%d日" }}
  {% if event.resources %}
  - 资源：
    {{ event.resources }}
  {% endif %}
{% endfor %}

{% endfor %}
{% endfor %}

---

> 注：所有讲座材料仅供学术交流使用，未经授权不得用于商业目的。 