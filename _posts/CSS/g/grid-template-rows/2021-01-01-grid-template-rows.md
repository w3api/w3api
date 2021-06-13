---
title: grid-template-rows
permalink: /CSS/grid-template-rows/
date: 2021-03-07 03:04:50.450489
key: CSS.g.grid-template-rows
category: CSS
tags: ['propiedad css']
sidebar: 
  nav: css
---

## Descripción
{{site.data.CSS.g.grid-template-rows.description }}

## Sintaxis
~~~css
grid-template-rows : none | <track-list> | <auto-track-list>
~~~

## Valores
* **auto-track-list**,  {% include w3api/value_description.html propiedad=site.data.CSS.g.grid-template-rows valor="auto-track-list" %}
* **none**,  {% include w3api/value_description.html propiedad=site.data.CSS.g.grid-template-rows valor="none" %}
* **track-list**,  {% include w3api/value_description.html propiedad=site.data.CSS.g.grid-template-rows valor="track-list" %}

## Ejemplo
~~~css
{{ site.data.CSS.g.grid-template-rows.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.CSS.g.grid-template-rows.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
