---
title: inspect.getmembers
permalink: /Python/inspect/getmembers/
date: 2021-01-01
key: Python.I.inspect.getmembers
category: python
tags: ['funcion python', 'inspect']
sidebar: 
  nav: python
---

## Descripción
{{site.data.Python.I.inspect.getmembers.description }}

## Sintaxis
~~~python
{{ site.data.Python.I.inspect.getmembers.sintaxis }}~~~

## Parámetros
* **object**,  {% include w3api/function_param_description.html propiedad=site.data.Python.I.inspect.getmembers valor="object" %}
* **predicate**,  {% include w3api/function_param_description.html propiedad=site.data.Python.I.inspect.getmembers valor="predicate" %}

## Ejemplo
~~~python
{{ site.data.Python.I.inspect.getmembers.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.Python.I.inspect.getmembers.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
