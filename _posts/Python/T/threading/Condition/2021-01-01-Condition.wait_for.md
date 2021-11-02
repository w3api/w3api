---
title: threading.Condition.wait_for
permalink: /Python/threading/Condition/wait_for/
date: 2021-01-01
key: Python.T.threading.Condition.wait_for
category: python
tags: ['metodo python', 'threading']
sidebar: 
  nav: python
---

{% include w3api/datos.html clase=site.data.Python.T.threading.Condition.metodos valor="wait_for" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~python
{{ _dato.sintaxis }}~~~

## Parámetros
* **predicate**,  {% include w3api/function_param_description.html propiedad=_dato valor="predicate" %}
* **timeout**,  {% include w3api/function_param_description.html propiedad=_dato valor="timeout" %}

## Clase Padre
[Condition](/Python/threading/Condition/)

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
