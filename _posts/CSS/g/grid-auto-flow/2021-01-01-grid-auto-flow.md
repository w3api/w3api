---
title: grid-auto-flow
permalink: /CSS/grid-auto-flow/
date: 2021-03-07 03:03:52.829973
key: CSS.g.grid-auto-flow
category: css
tags: ['propiedad css']
sidebar: 
  nav: css
---

## Descripción
{{site.data.CSS.g.grid-auto-flow.description }}

## Sintaxis
~~~css
grid-auto-flow : [ row | column ] || dense
~~~

## Valores
* **column**,  {% include w3api/value_description.html propiedad=site.data.CSS.g.grid-auto-flow valor="column" %}
* **dense**,  {% include w3api/value_description.html propiedad=site.data.CSS.g.grid-auto-flow valor="dense" %}
* **row**,  {% include w3api/value_description.html propiedad=site.data.CSS.g.grid-auto-flow valor="row" %}

## Ejemplo
~~~css
{{ site.data.CSS.g.grid-auto-flow.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.CSS.g.grid-auto-flow.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
