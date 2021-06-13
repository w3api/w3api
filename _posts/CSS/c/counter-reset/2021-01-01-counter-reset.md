---
title: counter-reset
permalink: /CSS/counter-reset/
date: 2021-03-07 03:01:39.269151
key: CSS.c.counter-reset
category: CSS
tags: ['propiedad css']
sidebar: 
  nav: css
---

## Descripción
{{site.data.CSS.c.counter-reset.description }}

## Sintaxis
~~~css
counter-reset : [ <identifier> <integer>? ]+ | none | inherit
~~~

## Valores
* **none**,  {% include w3api/value_description.html propiedad=site.data.CSS.c.counter-reset valor="none" %}
* **integer**,  {% include w3api/value_description.html propiedad=site.data.CSS.c.counter-reset valor="integer" %}
* **identifier**,  {% include w3api/value_description.html propiedad=site.data.CSS.c.counter-reset valor="identifier" %}
* **inherit**,  {% include w3api/value_description.html propiedad=site.data.CSS.c.counter-reset valor="inherit" %}

## Ejemplo
~~~css
{{ site.data.CSS.c.counter-reset.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.CSS.c.counter-reset.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
