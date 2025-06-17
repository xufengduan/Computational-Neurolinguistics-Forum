---
layout: default
title: 历史讲座汇总
permalink: /archive
---

# 历史讲座汇总

{% assign events_by_year = site.data.events.events | group_by_exp: "event", "event.date | date: '%Y'" | sort: "name" | reverse %}

{% for year in events_by_year %}
## {{ year.name }}年

<div class="card" style="margin: 2rem 0;">
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1.5rem;">
{% assign events_by_month = year.items | group_by_exp: "event", "event.date | date: '%m'" | sort: "name" | reverse %}
{% for month in events_by_month %}
{% for event in month.items %}
            <div class="event-card">
                <h4>{% assign hour = event.date | date: "%H" | plus: 0 %}{% if hour < 12 %}上午{% else %}下午{% endif %}{{ event.date | date: "%Y年%m月%d日 %H:%M" }}</h4>
                <p><strong>{{ event.title }}</strong></p>
                <p>{{ event.speaker }}（{{ event.institution }}）</p>
                {% if event.slides %}
                <a href="{{ event.slides }}" class="button">查看幻灯片</a>
                {% endif %}
                {% if event.video %}
                <a href="{{ event.video }}" class="button">观看视频</a>
  {% endif %}
            </div>
{% endfor %}
{% endfor %}
    </div>
</div>
{% endfor %}

<style>
.event-card {
    background: var(--background-light);
    padding: 1.5rem;
    border-radius: var(--border-radius);
    transition: all 0.3s ease;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
}

.event-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.event-card h4 {
    color: var(--text-color);
    margin-bottom: 0.5rem;
}

.event-card p {
    color: var(--text-light);
    margin: 0.5rem 0;
}

.event-card .button {
    margin-top: 1rem;
    margin-right: 0.5rem;
}
</style>

---

> 注：所有讲座材料仅供学术交流使用，未经授权不得用于商业目的。 