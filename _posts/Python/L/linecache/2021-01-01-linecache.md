---
title: linecache
permalink: /Python/linecache
date: 2021-01-01
key: Python.L.linecache
category: python
tags: ['modulo python']
sidebar: 
  nav: python
---

## Descripción
{{site.data.Python.L.linecache.description }}

## Funciones
* [checkcache](/Python/linecache/checkcache/)
* [clearcache](/Python/linecache/clearcache/)
* [getline](/Python/linecache/getline/)
* [lazycache](/Python/linecache/lazycache/)

## Ejemplo
~~~python
{{ site.data.Python.L.linecache.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.Python.L.linecache.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
