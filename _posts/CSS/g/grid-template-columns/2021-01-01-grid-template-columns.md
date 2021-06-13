---
title: grid-template-columns
permalink: /CSS/grid-template-columns/
date: 2021-03-07 03:04:46.017634
key: CSS.g.grid-template-columns
category: css
tags: ['propiedad css']
sidebar: 
  nav: css
---

## Descripción
{{site.data.CSS.g.grid-template-columns.description }}

## Sintaxis
~~~css
grid-template-columns : none | <track-list> | <auto-track-list>
~~~

## Valores
* **auto-track-list**,  {% include w3api/value_description.html propiedad=site.data.CSS.g.grid-template-columns valor="auto-track-list" %}
* **none**,  {% include w3api/value_description.html propiedad=site.data.CSS.g.grid-template-columns valor="none" %}
* **track-list**,  {% include w3api/value_description.html propiedad=site.data.CSS.g.grid-template-columns valor="track-list" %}

## Ejemplo
~~~css
{{ site.data.CSS.g.grid-template-columns.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.CSS.g.grid-template-columns.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
