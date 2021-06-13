---
title: list-style-image
permalink: /CSS/list-style-image/
date: 2021-03-07 03:05:59.007340
key: CSS.l.list-style-image
category: CSS
tags: ['propiedad css']
sidebar: 
  nav: css
---

## Descripción
{{site.data.CSS.l.list-style-image.description }}

## Sintaxis
~~~css
list-style-image : <uri> | none | inherit
~~~

## Valores
* **uri**,  {% include w3api/value_description.html propiedad=site.data.CSS.l.list-style-image valor="uri" %}
* **inherit**,  {% include w3api/value_description.html propiedad=site.data.CSS.l.list-style-image valor="inherit" %}
* **none**,  {% include w3api/value_description.html propiedad=site.data.CSS.l.list-style-image valor="none" %}

## Ejemplo
~~~css
{{ site.data.CSS.l.list-style-image.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.CSS.l.list-style-image.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
