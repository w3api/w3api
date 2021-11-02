---
title: traceback.StackSummary.extract
permalink: /Python/traceback/StackSummary/extract/
date: 2021-01-01
key: Python.T.traceback.StackSummary.extract
category: python
tags: ['metodo python', 'traceback']
sidebar: 
  nav: python
---

{% include w3api/datos.html clase=site.data.Python.T.traceback.StackSummary.metodos valor="extract" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~python
{{ _dato.sintaxis }}~~~

## Parámetros
* **\***,  {% include w3api/function_param_description.html propiedad=_dato valor="*" %}
* **capture_locals**,  {% include w3api/function_param_description.html propiedad=_dato valor="capture_locals" %}
* **frame_gen**,  {% include w3api/function_param_description.html propiedad=_dato valor="frame_gen" %}
* **limit**,  {% include w3api/function_param_description.html propiedad=_dato valor="limit" %}
* **lookup_lines**,  {% include w3api/function_param_description.html propiedad=_dato valor="lookup_lines" %}

## Clase Padre
[StackSummary](/Python/traceback/StackSummary/)

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
