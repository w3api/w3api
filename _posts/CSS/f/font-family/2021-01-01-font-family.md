---
title: font-family
permalink: /CSS/font-family/
date: 2021-03-07 03:02:58.823713
key: CSS.f.font-family
category: css
tags: ['propiedad css']
sidebar: 
  nav: css
---

## Descripción
{{site.data.CSS.f.font-family.description }}

## Sintaxis
~~~css
font-family : [ <family-name> | <generic-family> ] #
~~~

## Valores
* **family-name**,  {% include w3api/value_description.html propiedad=site.data.CSS.f.font-family valor="family-name" %}
* **generic-family**,  {% include w3api/value_description.html propiedad=site.data.CSS.f.font-family valor="generic-family" %}

## Ejemplo
~~~css
{{ site.data.CSS.f.font-family.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.CSS.f.font-family.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
