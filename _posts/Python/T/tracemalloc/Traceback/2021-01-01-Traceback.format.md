---
title: tracemalloc.Traceback.format
permalink: /Python/tracemalloc/Traceback/format/
date: 2021-01-01
key: Python.T.tracemalloc.Traceback.format
category: python
tags: ['metodo python', 'tracemalloc']
sidebar: 
  nav: python
---

{% include w3api/datos.html clase=site.data.Python.T.tracemalloc.Traceback.metodos valor="format" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~python
{{ _dato.sintaxis }}~~~

## Parámetros
* **limit**,  {% include w3api/function_param_description.html propiedad=_dato valor="limit" %}
* **most_recent_first**,  {% include w3api/function_param_description.html propiedad=_dato valor="most_recent_first" %}

## Clase Padre
[Traceback](/Python/tracemalloc/Traceback/)

## Ejemplo
~~~python
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
