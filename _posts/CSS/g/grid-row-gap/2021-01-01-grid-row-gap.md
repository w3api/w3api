---
title: grid-row-gap
permalink: /CSS/grid-row-gap/
date: 2021-03-07 03:04:28.162724
key: CSS.g.grid-row-gap
category: css
tags: ['propiedad css']
sidebar: 
  nav: css
---

## Descripción
{{site.data.CSS.g.grid-row-gap.description }}

## Sintaxis
~~~css
grid-row-gap : normal | <baseline-position> | <content-distribution> | <overflow-position>? <content-position>
~~~

## Valores
* **content-distribution**,  {% include w3api/value_description.html propiedad=site.data.CSS.g.grid-row-gap valor="content-distribution" %}
* **normal**,  {% include w3api/value_description.html propiedad=site.data.CSS.g.grid-row-gap valor="normal" %}
* **content-position**,  {% include w3api/value_description.html propiedad=site.data.CSS.g.grid-row-gap valor="content-position" %}
* **overflow-position**,  {% include w3api/value_description.html propiedad=site.data.CSS.g.grid-row-gap valor="overflow-position" %}
* **baseline-position**,  {% include w3api/value_description.html propiedad=site.data.CSS.g.grid-row-gap valor="baseline-position" %}

## Ejemplo
~~~css
{{ site.data.CSS.g.grid-row-gap.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.CSS.g.grid-row-gap.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
