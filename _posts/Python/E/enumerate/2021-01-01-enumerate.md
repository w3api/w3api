---
title: enumerate
permalink: /Python/enumerate/
date: 2021-01-01
key: Python.E.enumerate
category: python
tags: ['funcion python', 'base']
sidebar: 
  nav: python
---

## Descripción
{{site.data.Python.E.enumerate.description }}

## Sintaxis
~~~python
{{ site.data.Python.E.enumerate.sintaxis }}~~~

## Parámetros
* **iterable**,  {% include w3api/function_param_description.html propiedad=site.data.Python.E.enumerate valor="iterable" %}
* **start**,  {% include w3api/function_param_description.html propiedad=site.data.Python.E.enumerate valor="start" %}

## Ejemplo
~~~python
{{ site.data.Python.E.enumerate.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.Python.E.enumerate.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
