---
title: inspect.Signature.bind
permalink: /Python/inspect/Signature/bind/
date: 2021-01-01
key: Python.I.inspect.Signature.bind
category: python
tags: ['metodo python', 'inspect']
sidebar: 
  nav: python
---

{% include w3api/datos.html clase=site.data.Python.I.inspect.Signature.metodos valor="bind" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~python
{{ _dato.sintaxis }}~~~

## Parámetros
* **args**,  {% include w3api/function_param_description.html propiedad=_dato valor="args" %}
* **kwargs**,  {% include w3api/function_param_description.html propiedad=_dato valor="kwargs" %}

## Clase Padre
[Signature](/Python/inspect/Signature/)

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
