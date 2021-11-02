---
title: code.InteractiveInterpreter.runcode
permalink: /Python/code/InteractiveInterpreter/runcode/
date: 2021-01-01
key: Python.C.code.InteractiveInterpreter.runcode
category: python
tags: ['metodo python', 'code']
sidebar: 
  nav: python
---

{% include w3api/datos.html clase=site.data.Python.C.code.InteractiveInterpreter.metodos valor="runcode" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~python
{{ _dato.sintaxis }}~~~

## Parámetros
* **code**,  {% include w3api/function_param_description.html propiedad=_dato valor="code" %}

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
