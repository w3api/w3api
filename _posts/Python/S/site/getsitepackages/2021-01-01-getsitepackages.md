---
title: site.getsitepackages
permalink: /Python/site/getsitepackages/
date: 2021-01-01
key: Python.S.site.getsitepackages
category: python
tags: ['funcion python', 'site']
sidebar: 
  nav: python
---

## Descripción
{{site.data.Python.S.site.getsitepackages.description }}

## Sintaxis
~~~python
{{ site.data.Python.S.site.getsitepackages.sintaxis }}~~~

## Ejemplo
~~~python
{{ site.data.Python.S.site.getsitepackages.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.Python.S.site.getsitepackages.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
