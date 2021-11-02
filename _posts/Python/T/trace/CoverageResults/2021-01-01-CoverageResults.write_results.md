---
title: trace.CoverageResults.write_results
permalink: /Python/trace/CoverageResults/write_results/
date: 2021-01-01
key: Python.T.trace.CoverageResults.write_results
category: python
tags: ['metodo python', 'trace']
sidebar: 
  nav: python
---

{% include w3api/datos.html clase=site.data.Python.T.trace.CoverageResults.metodos valor="write_results" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~python
{{ _dato.sintaxis }}~~~

## Parámetros
* **coverdir**,  {% include w3api/function_param_description.html propiedad=_dato valor="coverdir" %}
* **show_missing**,  {% include w3api/function_param_description.html propiedad=_dato valor="show_missing" %}
* **summary**,  {% include w3api/function_param_description.html propiedad=_dato valor="summary" %}

## Clase Padre
[CoverageResults](/Python/trace/CoverageResults/)

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
