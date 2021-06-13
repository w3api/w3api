---
title: font-style
permalink: /CSS/font-style/
date: 2021-03-07 03:03:09.299752
key: CSS.f.font-style
category: css
tags: ['propiedad css']
sidebar: 
  nav: css
---

## Descripción
{{site.data.CSS.f.font-style.description }}

## Sintaxis
~~~css
font-style : normal | italic | oblique
~~~

## Valores
* **normal**,  {% include w3api/value_description.html propiedad=site.data.CSS.f.font-style valor="normal" %}
* **oblique**,  {% include w3api/value_description.html propiedad=site.data.CSS.f.font-style valor="oblique" %}
* **italic**,  {% include w3api/value_description.html propiedad=site.data.CSS.f.font-style valor="italic" %}

## Ejemplo
~~~css
{{ site.data.CSS.f.font-style.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.CSS.f.font-style.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
