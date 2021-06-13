---
title: place-items
permalink: /CSS/place-items/
date: 2021-03-07 03:09:48.168773
key: CSS.p.place-items
category: CSS
tags: ['propiedad css']
sidebar: 
  nav: css
---

## Descripción
{{site.data.CSS.p.place-items.description }}

## Sintaxis
~~~css
place-items : <'align-items'> <'justify-items'>?
~~~

## Valores
* **justify-items**,  {% include w3api/value_description.html propiedad=site.data.CSS.p.place-items valor="justify-items" %}
* **align-items**,  {% include w3api/value_description.html propiedad=site.data.CSS.p.place-items valor="align-items" %}

## Ejemplo
~~~css
{{ site.data.CSS.p.place-items.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.CSS.p.place-items.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
