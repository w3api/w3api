---
title: collections
permalink: /Python/collections
date: 2021-01-01
key: Python.C.collections
category: python
tags: ['modulo python']
sidebar: 
  nav: python
---

## Descripción
{{site.data.Python.C.collections.description }}

## Funciones
* [namedtuple](/Python/collections/namedtuple/)

## Clases
* [ChainMap](/Python/collections/ChainMap/)
* [Counter](/Python/collections/Counter/)
* [defaultdict](/Python/collections/defaultdict/)
* [deque](/Python/collections/deque/)
* [OrderedDict](/Python/collections/OrderedDict/)
* [somenamedtuple](/Python/collections/somenamedtuple/)
* [UserDict](/Python/collections/UserDict/)
* [UserList](/Python/collections/UserList/)
* [UserString](/Python/collections/UserString/)

## Ejemplo
~~~python
{{ site.data.Python.C.collections.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.Python.C.collections.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
