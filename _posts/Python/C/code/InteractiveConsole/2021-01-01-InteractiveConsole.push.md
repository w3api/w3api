---
title: code.InteractiveConsole.push
permalink: /Python/code/InteractiveConsole/push/
date: 2021-01-01
key: Python.C.code.InteractiveConsole.push
category: python
tags: ['metodo python', 'code']
sidebar: 
  nav: python
---

{% include w3api/datos.html clase=site.data.Python.C.code.InteractiveConsole.metodos valor="push" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~python
{{ _dato.sintaxis }}~~~

## Parámetros
* **line**,  {% include w3api/function_param_description.html propiedad=_dato valor="line" %}

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
