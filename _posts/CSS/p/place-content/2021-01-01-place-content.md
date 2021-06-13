---
title: place-content
permalink: /CSS/place-content/
date: 2021-03-07 03:09:45.379261
key: CSS.p.place-content
category: CSS
tags: ['propiedad css']
sidebar: 
  nav: css
---

## Descripción
{{site.data.CSS.p.place-content.description }}

## Sintaxis
~~~css
place-content : <'align-content'> <'justify-content'>?
~~~

## Valores
* **align-content**,  {% include w3api/value_description.html propiedad=site.data.CSS.p.place-content valor="align-content" %}
* **justify-content**,  {% include w3api/value_description.html propiedad=site.data.CSS.p.place-content valor="justify-content" %}

## Ejemplo
~~~css
{{ site.data.CSS.p.place-content.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.CSS.p.place-content.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
