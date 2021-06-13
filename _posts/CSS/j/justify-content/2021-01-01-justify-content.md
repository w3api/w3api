---
title: justify-content
permalink: /CSS/justify-content/
date: 2021-03-07 03:05:12.839749
key: CSS.j.justify-content
category: css
tags: ['propiedad css']
sidebar: 
  nav: css
---

## Descripción
{{site.data.CSS.j.justify-content.description }}

## Sintaxis
~~~css
justify-content : normal | <content-distribution> | <overflow-position>? [ <content-position> | left | right ]
~~~

## Valores
* **content-distribution**,  {% include w3api/value_description.html propiedad=site.data.CSS.j.justify-content valor="content-distribution" %}
* **normal**,  {% include w3api/value_description.html propiedad=site.data.CSS.j.justify-content valor="normal" %}
* **content-position**,  {% include w3api/value_description.html propiedad=site.data.CSS.j.justify-content valor="content-position" %}
* **overflow-position**,  {% include w3api/value_description.html propiedad=site.data.CSS.j.justify-content valor="overflow-position" %}
* **left**,  {% include w3api/value_description.html propiedad=site.data.CSS.j.justify-content valor="left" %}
* **right**,  {% include w3api/value_description.html propiedad=site.data.CSS.j.justify-content valor="right" %}

## Ejemplo
~~~css
{{ site.data.CSS.j.justify-content.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.CSS.j.justify-content.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
