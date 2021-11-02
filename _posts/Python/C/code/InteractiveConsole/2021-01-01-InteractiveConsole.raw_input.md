---
title: code.InteractiveConsole.raw_input
permalink: /Python/code/InteractiveConsole/raw_input/
date: 2021-01-01
key: Python.C.code.InteractiveConsole.raw_input
category: python
tags: ['metodo python', 'code']
sidebar: 
  nav: python
---

{% include w3api/datos.html clase=site.data.Python.C.code.InteractiveConsole.metodos valor="raw_input" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~python
{{ _dato.sintaxis }}~~~

## Parámetros
* **prompt**,  {% include w3api/function_param_description.html propiedad=_dato valor="prompt" %}

## Clase Padre
[InteractiveConsole](/Python/code/InteractiveConsole/)

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
