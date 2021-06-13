---
title: grid-template
permalink: /CSS/grid-template/
date: 2021-03-07 03:04:37.120133
key: CSS.g.grid-template
category: CSS
tags: ['propiedad css']
sidebar: 
  nav: css
---

## Descripción
{{site.data.CSS.g.grid-template.description }}

## Sintaxis
~~~css
grid-template : none | [ <'grid-template-rows'> / <'grid-template-columns'> ] | [ <line-names>? <string> <track-size>? <line-names>? ]+ [ / <explicit-track-list> ]?
~~~

## Valores
* **grid-template-columns**,  {% include w3api/value_description.html propiedad=site.data.CSS.g.grid-template valor="grid-template-columns" %}
* **none**,  {% include w3api/value_description.html propiedad=site.data.CSS.g.grid-template valor="none" %}
* **explicit-track-list**,  {% include w3api/value_description.html propiedad=site.data.CSS.g.grid-template valor="explicit-track-list" %}
* **grid-template-rows**,  {% include w3api/value_description.html propiedad=site.data.CSS.g.grid-template valor="grid-template-rows" %}
* **track-size**,  {% include w3api/value_description.html propiedad=site.data.CSS.g.grid-template valor="track-size" %}
* **string**,  {% include w3api/value_description.html propiedad=site.data.CSS.g.grid-template valor="string" %}
* **line-names**,  {% include w3api/value_description.html propiedad=site.data.CSS.g.grid-template valor="line-names" %}

## Ejemplo
~~~css
{{ site.data.CSS.g.grid-template.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.CSS.g.grid-template.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
