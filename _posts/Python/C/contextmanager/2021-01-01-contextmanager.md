---
title: contextmanager
permalink: /Python/contextmanager/
date: 2021-01-01
key: Python.C.contextmanager
category: python
tags: ['clase python', 'base']
sidebar: 
  nav: python
---

{% include w3api/datos.html clase=site.data.Python.C.contextmanager.metodos valor="contextmanager" %}

## Descripción
{{site.data.Python.C.contextmanager.description }}

## Sintaxis
~~~python
{{ site.data.Python.C.contextmanager.sintaxis }}~~~

## Métodos
* [__enter__](/Python/contextmanager/__enter__/)
* [__exit__](/Python/contextmanager/__exit__/)

## Ejemplo
~~~python
{{ site.data.Python.C.contextmanager.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.Python.C.contextmanager.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
