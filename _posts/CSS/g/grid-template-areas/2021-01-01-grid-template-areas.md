---
title: grid-template-areas
permalink: /CSS/grid-template-areas/
date: 2021-03-07 03:04:41.774386
key: CSS.g.grid-template-areas
category: CSS
tags: ['propiedad css']
sidebar: 
  nav: css
---

## Descripción
{{site.data.CSS.g.grid-template-areas.description }}

## Sintaxis
~~~css
grid-template-areas : none | <string>+
~~~

## Valores
* **string**,  {% include w3api/value_description.html propiedad=site.data.CSS.g.grid-template-areas valor="string" %}
* **none**,  {% include w3api/value_description.html propiedad=site.data.CSS.g.grid-template-areas valor="none" %}

## Ejemplo
~~~css
{{ site.data.CSS.g.grid-template-areas.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.CSS.g.grid-template-areas.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
