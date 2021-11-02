---
title: queue.SimpleQueue.put
permalink: /Python/queue/SimpleQueue/put/
date: 2021-01-01
key: Python.Q.queue.SimpleQueue.put
category: python
tags: ['metodo python', 'queue']
sidebar: 
  nav: python
---

{% include w3api/datos.html clase=site.data.Python.Q.queue.SimpleQueue.metodos valor="put" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~python
{{ _dato.sintaxis }}~~~

## Parámetros
* **block**,  {% include w3api/function_param_description.html propiedad=_dato valor="block" %}
* **item**,  {% include w3api/function_param_description.html propiedad=_dato valor="item" %}
* **timeout**,  {% include w3api/function_param_description.html propiedad=_dato valor="timeout" %}

## Clase Padre
[SimpleQueue](/Python/queue/SimpleQueue/)

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
