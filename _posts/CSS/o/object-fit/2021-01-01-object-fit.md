---
title: object-fit
permalink: /CSS/object-fit/
date: 2021-03-07 03:08:08.639092
key: CSS.o.object-fit
category: css
tags: ['propiedad css']
sidebar: 
  nav: css
---

## Descripción
{{site.data.CSS.o.object-fit.description }}

## Sintaxis
~~~css
object-fit : fill | contain | cover | none | scale-down
~~~

## Valores
* **scale-down**,  {% include w3api/value_description.html propiedad=site.data.CSS.o.object-fit valor="scale-down" %}
* **none**,  {% include w3api/value_description.html propiedad=site.data.CSS.o.object-fit valor="none" %}
* **cover**,  {% include w3api/value_description.html propiedad=site.data.CSS.o.object-fit valor="cover" %}
* **fill**,  {% include w3api/value_description.html propiedad=site.data.CSS.o.object-fit valor="fill" %}
* **contain**,  {% include w3api/value_description.html propiedad=site.data.CSS.o.object-fit valor="contain" %}

## Ejemplo
~~~css
{{ site.data.CSS.o.object-fit.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.CSS.o.object-fit.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
