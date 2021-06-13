---
title: list-style-position
permalink: /CSS/list-style-position/
date: 2021-03-07 03:06:05.754765
key: CSS.l.list-style-position
category: CSS
tags: ['propiedad css']
sidebar: 
  nav: css
---

## Descripción
{{site.data.CSS.l.list-style-position.description }}

## Sintaxis
~~~css
list-style-position : inside | outside | inherit
~~~

## Valores
* **inside**,  {% include w3api/value_description.html propiedad=site.data.CSS.l.list-style-position valor="inside" %}
* **outside**,  {% include w3api/value_description.html propiedad=site.data.CSS.l.list-style-position valor="outside" %}
* **inherit**,  {% include w3api/value_description.html propiedad=site.data.CSS.l.list-style-position valor="inherit" %}

## Ejemplo
~~~css
{{ site.data.CSS.l.list-style-position.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.CSS.l.list-style-position.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
