---
title: hanging-punctuation
permalink: /CSS/hanging-punctuation/
date: 2021-03-07 03:04:53.574877
key: CSS.h.hanging-punctuation
category: CSS
tags: ['propiedad css']
sidebar: 
  nav: css
---

## Descripción
{{site.data.CSS.h.hanging-punctuation.description }}

## Sintaxis
~~~css
hanging-punctuation : none | [ first || [ force-end | allow-end ] || last ]
~~~

## Valores
* **first**,  {% include w3api/value_description.html propiedad=site.data.CSS.h.hanging-punctuation valor="first" %}
* **none**,  {% include w3api/value_description.html propiedad=site.data.CSS.h.hanging-punctuation valor="none" %}
* **last**,  {% include w3api/value_description.html propiedad=site.data.CSS.h.hanging-punctuation valor="last" %}
* **allow-end**,  {% include w3api/value_description.html propiedad=site.data.CSS.h.hanging-punctuation valor="allow-end" %}
* **force-end**,  {% include w3api/value_description.html propiedad=site.data.CSS.h.hanging-punctuation valor="force-end" %}

## Ejemplo
~~~css
{{ site.data.CSS.h.hanging-punctuation.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.CSS.h.hanging-punctuation.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
