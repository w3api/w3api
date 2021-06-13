---
title: list-style
permalink: /CSS/list-style/
date: 2021-03-07 03:05:52.249116
key: CSS.l.list-style
category: css
tags: ['propiedad css']
sidebar: 
  nav: css
---

## Descripción
{{site.data.CSS.l.list-style.description }}

## Sintaxis
~~~css
list-style : [ <'list-style-type'> || <'list-style-position'> || <'list-style-image'> ] | inherit
~~~

## Valores
* **list-style-type**,  {% include w3api/value_description.html propiedad=site.data.CSS.l.list-style valor="list-style-type" %}
* **inherit**,  {% include w3api/value_description.html propiedad=site.data.CSS.l.list-style valor="inherit" %}
* **list-style-image**,  {% include w3api/value_description.html propiedad=site.data.CSS.l.list-style valor="list-style-image" %}
* **list-style-position**,  {% include w3api/value_description.html propiedad=site.data.CSS.l.list-style valor="list-style-position" %}

## Ejemplo
~~~css
{{ site.data.CSS.l.list-style.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.CSS.l.list-style.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
