---
title: grid-column
permalink: /CSS/grid-column/
date: 2021-03-07 03:04:01.499229
key: CSS.g.grid-column
category: CSS
tags: ['propiedad css']
sidebar: 
  nav: css
---

## Descripción
{{site.data.CSS.g.grid-column.description }}

## Sintaxis
~~~css
grid-column : <grid-line> [ / <grid-line> ]?
~~~

## Valores
* **grid-line**,  {% include w3api/value_description.html propiedad=site.data.CSS.g.grid-column valor="grid-line" %}

## Ejemplo
~~~css
{{ site.data.CSS.g.grid-column.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.CSS.g.grid-column.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
