---
title: visibility
permalink: /CSS/visibility/
date: 2021-03-07 03:13:17.265190
key: CSS.v.visibility
category: css
tags: ['propiedad css']
sidebar: 
  nav: css
---

## Descripción
{{site.data.CSS.v.visibility.description }}

## Sintaxis
~~~css
visibility : visible | hidden | collapse | inherit
~~~

## Valores
* **visible**,  {% include w3api/value_description.html propiedad=site.data.CSS.v.visibility valor="visible" %}
* **hidden**,  {% include w3api/value_description.html propiedad=site.data.CSS.v.visibility valor="hidden" %}
* **inherit**,  {% include w3api/value_description.html propiedad=site.data.CSS.v.visibility valor="inherit" %}
* **collapse**,  {% include w3api/value_description.html propiedad=site.data.CSS.v.visibility valor="collapse" %}

## Ejemplo
~~~css
{{ site.data.CSS.v.visibility.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.CSS.v.visibility.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
