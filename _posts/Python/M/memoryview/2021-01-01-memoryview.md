---
title: memoryview
permalink: /Python/memoryview/
date: 2021-01-01
key: Python.M.memoryview
category: python
tags: ['clase python', 'base']
sidebar: 
  nav: python
---

{% include w3api/datos.html clase=site.data.Python.M.memoryview.metodos valor="memoryview" %}

## Descripción
{{site.data.Python.M.memoryview.description }}

## Sintaxis
~~~python
{{ site.data.Python.M.memoryview.sintaxis }}~~~

## Constructores
* [memoryview](/Python/memoryview/memoryview/)

## Métodos
* [cast](/Python/memoryview/cast/)
* [hex](/Python/memoryview/hex/)
* [release](/Python/memoryview/release/)
* [tobytes](/Python/memoryview/tobytes/)
* [tolist](/Python/memoryview/tolist/)
* [toreadonly](/Python/memoryview/toreadonly/)
* [__eq__](/Python/memoryview/__eq__/)

## Atributos
* [contiguous](/Python/memoryview/contiguous/)
* [c_contiguous](/Python/memoryview/c_contiguous/)
* [format](/Python/memoryview/format/)
* [f_contiguous](/Python/memoryview/f_contiguous/)
* [itemsize](/Python/memoryview/itemsize/)
* [nbytes](/Python/memoryview/nbytes/)
* [ndim](/Python/memoryview/ndim/)
* [obj](/Python/memoryview/obj/)
* [readonly](/Python/memoryview/readonly/)
* [shape](/Python/memoryview/shape/)
* [strides](/Python/memoryview/strides/)
* [suboffsets](/Python/memoryview/suboffsets/)

## Ejemplo
~~~python
{{ site.data.Python.M.memoryview.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.Python.M.memoryview.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
