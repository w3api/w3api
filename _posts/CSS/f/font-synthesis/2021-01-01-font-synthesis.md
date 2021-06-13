---
title: font-synthesis
permalink: /CSS/font-synthesis/
date: 2021-03-07 03:03:11.661427
key: CSS.f.font-synthesis
category: css
tags: ['propiedad css']
sidebar: 
  nav: css
---

## Descripción
{{site.data.CSS.f.font-synthesis.description }}

## Sintaxis
~~~css
font-synthesis : none | [ weight || style ]
~~~

## Valores
* **weight**,  {% include w3api/value_description.html propiedad=site.data.CSS.f.font-synthesis valor="weight" %}
* **none**,  {% include w3api/value_description.html propiedad=site.data.CSS.f.font-synthesis valor="none" %}
* **style**,  {% include w3api/value_description.html propiedad=site.data.CSS.f.font-synthesis valor="style" %}

## Ejemplo
~~~css
{{ site.data.CSS.f.font-synthesis.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.CSS.f.font-synthesis.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
