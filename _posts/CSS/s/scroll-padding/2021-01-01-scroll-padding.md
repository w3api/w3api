---
title: scroll-padding
permalink: /CSS/scroll-padding/
date: 2021-03-07 03:10:54.230784
key: CSS.s.scroll-padding
category: CSS
tags: ['propiedad css']
sidebar: 
  nav: css
---

## Descripción
{{site.data.CSS.s.scroll-padding.description }}

## Sintaxis
~~~css
scroll-padding : [ auto | <length-percentage> ]{1,4}
~~~

## Valores
* **length-percentage**,  {% include w3api/value_description.html propiedad=site.data.CSS.s.scroll-padding valor="length-percentage" %}
* **auto**,  {% include w3api/value_description.html propiedad=site.data.CSS.s.scroll-padding valor="auto" %}

## Ejemplo
~~~css
{{ site.data.CSS.s.scroll-padding.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.CSS.s.scroll-padding.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
