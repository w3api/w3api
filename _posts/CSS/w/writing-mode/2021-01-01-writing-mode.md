---
title: writing-mode
permalink: /CSS/writing-mode/
date: 2021-03-07 03:14:02.237546
key: CSS.w.writing-mode
category: CSS
tags: ['propiedad css']
sidebar: 
  nav: css
---

## Descripción
{{site.data.CSS.w.writing-mode.description }}

## Sintaxis
~~~css
writing-mode : horizontal-tb | vertical-rl | vertical-lr | sideways-rl | sideways-lr
~~~

## Valores
* **sideways-rl**,  {% include w3api/value_description.html propiedad=site.data.CSS.w.writing-mode valor="sideways-rl" %}
* **vertical-lr**,  {% include w3api/value_description.html propiedad=site.data.CSS.w.writing-mode valor="vertical-lr" %}
* **horizontal-tb**,  {% include w3api/value_description.html propiedad=site.data.CSS.w.writing-mode valor="horizontal-tb" %}
* **sideways-lr**,  {% include w3api/value_description.html propiedad=site.data.CSS.w.writing-mode valor="sideways-lr" %}
* **vertical-rl**,  {% include w3api/value_description.html propiedad=site.data.CSS.w.writing-mode valor="vertical-rl" %}

## Ejemplo
~~~css
{{ site.data.CSS.w.writing-mode.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.CSS.w.writing-mode.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
