---
title: site.getusersitepackages
permalink: /Python/site/getusersitepackages/
date: 2021-01-01
key: Python.S.site.getusersitepackages
category: python
tags: ['funcion python', 'site']
sidebar: 
  nav: python
---

## Descripción
{{site.data.Python.S.site.getusersitepackages.description }}

## Sintaxis
~~~python
{{ site.data.Python.S.site.getusersitepackages.sintaxis }}~~~

## Ejemplo
~~~python
{{ site.data.Python.S.site.getusersitepackages.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.Python.S.site.getusersitepackages.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
