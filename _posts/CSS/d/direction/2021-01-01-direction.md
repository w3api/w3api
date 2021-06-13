---
title: direction
permalink: /CSS/direction/
date: 2021-03-07 03:01:51.651717
key: CSS.d.direction
category: CSS
tags: ['propiedad css']
sidebar: 
  nav: css
---

## Descripción
{{site.data.CSS.d.direction.description }}

## Sintaxis
~~~css
direction : ltr | rtl
~~~

## Valores
* **rtl**,  {% include w3api/value_description.html propiedad=site.data.CSS.d.direction valor="rtl" %}
* **ltr**,  {% include w3api/value_description.html propiedad=site.data.CSS.d.direction valor="ltr" %}

## Ejemplo
~~~css
{{ site.data.CSS.d.direction.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.CSS.d.direction.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
