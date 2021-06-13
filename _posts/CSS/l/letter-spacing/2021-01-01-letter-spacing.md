---
title: letter-spacing
permalink: /CSS/letter-spacing/
date: 2021-03-07 03:05:28.827095
key: CSS.l.letter-spacing
category: css
tags: ['propiedad css']
sidebar: 
  nav: css
---

## Descripción
{{site.data.CSS.l.letter-spacing.description }}

## Sintaxis
~~~css
letter-spacing : normal | <length>
~~~

## Valores
* **normal**,  {% include w3api/value_description.html propiedad=site.data.CSS.l.letter-spacing valor="normal" %}
* **length**,  {% include w3api/value_description.html propiedad=site.data.CSS.l.letter-spacing valor="length" %}

## Ejemplo
~~~css
{{ site.data.CSS.l.letter-spacing.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.CSS.l.letter-spacing.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
