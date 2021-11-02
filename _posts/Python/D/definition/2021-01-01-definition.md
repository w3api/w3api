---
title: definition
permalink: /Python/definition/
date: 2021-01-01
key: Python.D.definition
category: python
tags: ['clase python', 'base']
sidebar: 
  nav: python
---

{% include w3api/datos.html clase=site.data.Python.D.definition.metodos valor="definition" %}

## Descripción
{{site.data.Python.D.definition.description }}

## Sintaxis
~~~python
{{ site.data.Python.D.definition.sintaxis }}~~~

## Atributos
* [__name__](/Python/definition/__name__/)
* [__qualname__](/Python/definition/__qualname__/)

## Ejemplo
~~~python
{{ site.data.Python.D.definition.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.Python.D.definition.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
