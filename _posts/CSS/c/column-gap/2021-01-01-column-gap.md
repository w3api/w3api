---
title: column-gap
permalink: /CSS/column-gap/
date: 2021-03-07 03:00:59.744668
key: CSS.c.column-gap
category: css
tags: ['propiedad css']
sidebar: 
  nav: css
---

## Descripción
{{site.data.CSS.c.column-gap.description }}

## Sintaxis
~~~css
column-gap : normal | <length-percentage>
~~~

## Valores
* **length-percentage**,  {% include w3api/value_description.html propiedad=site.data.CSS.c.column-gap valor="length-percentage" %}
* **normal**,  {% include w3api/value_description.html propiedad=site.data.CSS.c.column-gap valor="normal" %}

## Ejemplo
~~~css
{{ site.data.CSS.c.column-gap.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.CSS.c.column-gap.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
