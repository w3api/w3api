---
title: justify-items
permalink: /CSS/justify-items/
date: 2021-03-07 03:05:15.646911
key: CSS.j.justify-items
category: CSS
tags: ['propiedad css']
sidebar: 
  nav: css
---

## Descripción
{{site.data.CSS.j.justify-items.description }}

## Sintaxis
~~~css
justify-items : normal | stretch | <baseline-position> | <overflow-position>? [ <self-position> | left | right ] | legacy | legacy && [ left | right | center ]
~~~

## Valores
* **self-position**,  {% include w3api/value_description.html propiedad=site.data.CSS.j.justify-items valor="self-position" %}
* **normal**,  {% include w3api/value_description.html propiedad=site.data.CSS.j.justify-items valor="normal" %}
* **overflow-position**,  {% include w3api/value_description.html propiedad=site.data.CSS.j.justify-items valor="overflow-position" %}
* **baseline-position**,  {% include w3api/value_description.html propiedad=site.data.CSS.j.justify-items valor="baseline-position" %}
* **left**,  {% include w3api/value_description.html propiedad=site.data.CSS.j.justify-items valor="left" %}
* **center**,  {% include w3api/value_description.html propiedad=site.data.CSS.j.justify-items valor="center" %}
* **right**,  {% include w3api/value_description.html propiedad=site.data.CSS.j.justify-items valor="right" %}
* **stretch**,  {% include w3api/value_description.html propiedad=site.data.CSS.j.justify-items valor="stretch" %}
* **legacy**,  {% include w3api/value_description.html propiedad=site.data.CSS.j.justify-items valor="legacy" %}

## Ejemplo
~~~css
{{ site.data.CSS.j.justify-items.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.CSS.j.justify-items.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
