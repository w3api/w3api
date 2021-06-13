---
title: flex-direction
permalink: /CSS/flex-direction/
date: 2021-03-07 03:02:19.763290
key: CSS.f.flex-direction
category: css
tags: ['propiedad css']
sidebar: 
  nav: css
---

## Descripción
{{site.data.CSS.f.flex-direction.description }}

## Sintaxis
~~~css
flex-direction : row | row-reverse | column | column-reverse
~~~

## Valores
* **column-reverse**,  {% include w3api/value_description.html propiedad=site.data.CSS.f.flex-direction valor="column-reverse" %}
* **column**,  {% include w3api/value_description.html propiedad=site.data.CSS.f.flex-direction valor="column" %}
* **row-reverse**,  {% include w3api/value_description.html propiedad=site.data.CSS.f.flex-direction valor="row-reverse" %}
* **row**,  {% include w3api/value_description.html propiedad=site.data.CSS.f.flex-direction valor="row" %}

## Ejemplo
~~~css
{{ site.data.CSS.f.flex-direction.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.CSS.f.flex-direction.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
