---
title: grid-column-gap
permalink: /CSS/grid-column-gap/
date: 2021-03-07 03:04:08.742524
key: CSS.g.grid-column-gap
category: css
tags: ['propiedad css']
sidebar: 
  nav: css
---

## Descripción
{{site.data.CSS.g.grid-column-gap.description }}

## Sintaxis
~~~css
grid-column-gap : normal | <baseline-position> | <content-distribution> | <overflow-position>? <content-position>
~~~

## Valores
* **content-distribution**,  {% include w3api/value_description.html propiedad=site.data.CSS.g.grid-column-gap valor="content-distribution" %}
* **normal**,  {% include w3api/value_description.html propiedad=site.data.CSS.g.grid-column-gap valor="normal" %}
* **content-position**,  {% include w3api/value_description.html propiedad=site.data.CSS.g.grid-column-gap valor="content-position" %}
* **overflow-position**,  {% include w3api/value_description.html propiedad=site.data.CSS.g.grid-column-gap valor="overflow-position" %}
* **baseline-position**,  {% include w3api/value_description.html propiedad=site.data.CSS.g.grid-column-gap valor="baseline-position" %}

## Ejemplo
~~~css
{{ site.data.CSS.g.grid-column-gap.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.CSS.g.grid-column-gap.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
