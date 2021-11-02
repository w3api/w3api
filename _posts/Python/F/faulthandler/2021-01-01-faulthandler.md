---
title: faulthandler
permalink: /Python/faulthandler
date: 2021-01-01
key: Python.F.faulthandler
category: python
tags: ['modulo python']
sidebar: 
  nav: python
---

## Descripción
{{site.data.Python.F.faulthandler.description }}

## Funciones
* [cancel_dump_traceback_later](/Python/faulthandler/cancel_dump_traceback_later/)
* [disable](/Python/faulthandler/disable/)
* [dump_traceback](/Python/faulthandler/dump_traceback/)
* [dump_traceback_later](/Python/faulthandler/dump_traceback_later/)
* [enable](/Python/faulthandler/enable/)
* [is_enabled](/Python/faulthandler/is_enabled/)
* [register](/Python/faulthandler/register/)
* [unregister](/Python/faulthandler/unregister/)

## Ejemplo
~~~python
{{ site.data.Python.F.faulthandler.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.Python.F.faulthandler.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
