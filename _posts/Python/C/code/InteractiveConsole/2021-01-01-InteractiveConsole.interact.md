---
title: code.InteractiveConsole.interact
permalink: /Python/code/InteractiveConsole/interact/
date: 2021-01-01
key: Python.C.code.InteractiveConsole.interact
category: python
tags: ['metodo python', 'code']
sidebar: 
  nav: python
---

{% include w3api/datos.html clase=site.data.Python.C.code.InteractiveConsole.metodos valor="interact" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~python
{{ _dato.sintaxis }}~~~

## Parámetros
* **banner**,  {% include w3api/function_param_description.html propiedad=_dato valor="banner" %}
* **exitmsg**,  {% include w3api/function_param_description.html propiedad=_dato valor="exitmsg" %}

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
