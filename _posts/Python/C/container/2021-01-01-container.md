---
title: container
permalink: /Python/container/
date: 2021-01-01
key: Python.C.container
category: python
tags: ['clase python', 'base']
sidebar: 
  nav: python
---

{% include w3api/datos.html clase=site.data.Python.C.container.metodos valor="container" %}

## Descripción
{{site.data.Python.C.container.description }}

## Sintaxis
~~~python
{{ site.data.Python.C.container.sintaxis }}~~~

## Métodos
* [__iter__](/Python/container/__iter__/)

## Ejemplo
~~~python
{{ site.data.Python.C.container.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.Python.C.container.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
