---
title: counter-increment
permalink: /CSS/counter-increment/
date: 2021-03-07 03:01:32.275880
key: CSS.c.counter-increment
category: CSS
tags: ['propiedad css']
sidebar: 
  nav: css
---

## Descripción
{{site.data.CSS.c.counter-increment.description }}

## Sintaxis
~~~css
counter-increment : [ <identifier> <integer>? ]+ | none | inherit
~~~

## Valores
* **none**,  {% include w3api/value_description.html propiedad=site.data.CSS.c.counter-increment valor="none" %}
* **integer**,  {% include w3api/value_description.html propiedad=site.data.CSS.c.counter-increment valor="integer" %}
* **identifier**,  {% include w3api/value_description.html propiedad=site.data.CSS.c.counter-increment valor="identifier" %}
* **inherit**,  {% include w3api/value_description.html propiedad=site.data.CSS.c.counter-increment valor="inherit" %}

## Ejemplo
~~~css
{{ site.data.CSS.c.counter-increment.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.CSS.c.counter-increment.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
