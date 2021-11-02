---
title: turtledemo
permalink: /Python/turtledemo
date: 2021-01-01
key: Python.T.turtledemo
category: python
tags: ['modulo python']
sidebar: 
  nav: python
---

## Descripción
{{site.data.Python.T.turtledemo.description }}

## Ejemplo
~~~python
{{ site.data.Python.T.turtledemo.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.Python.T.turtledemo.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
