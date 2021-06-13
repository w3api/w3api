---
title: image-orientation
permalink: /CSS/image-orientation/
date: 2021-03-07 03:05:05.723868
key: CSS.i.image-orientation
category: css
tags: ['propiedad css']
sidebar: 
  nav: css
---

## Descripción
{{site.data.CSS.i.image-orientation.description }}

## Sintaxis
~~~css
image-orientation : from-image | none | [ <angle> || flip ]
~~~

## Valores
* **angle**,  {% include w3api/value_description.html propiedad=site.data.CSS.i.image-orientation valor="angle" %}
* **from-image**,  {% include w3api/value_description.html propiedad=site.data.CSS.i.image-orientation valor="from-image" %}
* **flip**,  {% include w3api/value_description.html propiedad=site.data.CSS.i.image-orientation valor="flip" %}
* **none**,  {% include w3api/value_description.html propiedad=site.data.CSS.i.image-orientation valor="none" %}

## Ejemplo
~~~css
{{ site.data.CSS.i.image-orientation.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.CSS.i.image-orientation.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
