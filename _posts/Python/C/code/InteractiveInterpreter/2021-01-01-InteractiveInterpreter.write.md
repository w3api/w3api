---
title: code.InteractiveInterpreter.write
permalink: /Python/code/InteractiveInterpreter/write/
date: 2021-01-01
key: Python.C.code.InteractiveInterpreter.write
category: python
tags: ['metodo python', 'code']
sidebar: 
  nav: python
---

{% include w3api/datos.html clase=site.data.Python.C.code.InteractiveInterpreter.metodos valor="write" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~python
{{ _dato.sintaxis }}~~~

## Parámetros
* **data**,  {% include w3api/function_param_description.html propiedad=_dato valor="data" %}

## Clase Padre
[InteractiveInterpreter](/Python/code/InteractiveInterpreter/)

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
