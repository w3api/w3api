---
title: memoryview.hex
permalink: /Python/memoryview/hex/
date: 2021-01-01
key: Python.M.memoryview.hex
category: python
tags: ['metodo python', 'base']
sidebar: 
  nav: python
---

{% include w3api/datos.html clase=site.data.Python.M.memoryview.metodos valor="hex" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~python
{{ _dato.sintaxis }}~~~

## Parámetros
* **bytes_per_sep**,  {% include w3api/function_param_description.html propiedad=_dato valor="bytes_per_sep" %}
* **sep**,  {% include w3api/function_param_description.html propiedad=_dato valor="sep" %}

## Clase Padre
[memoryview](/Python/memoryview/)

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
