---
title: tracemalloc
permalink: /Python/tracemalloc
date: 2021-01-01
key: Python.T.tracemalloc
category: python
tags: ['modulo python']
sidebar: 
  nav: python
---

## Descripción
{{site.data.Python.T.tracemalloc.description }}

## Funciones
* [clear_traces](/Python/tracemalloc/clear_traces/)
* [get_object_traceback](/Python/tracemalloc/get_object_traceback/)
* [get_traceback_limit](/Python/tracemalloc/get_traceback_limit/)
* [get_traced_memory](/Python/tracemalloc/get_traced_memory/)
* [get_tracemalloc_memory](/Python/tracemalloc/get_tracemalloc_memory/)
* [is_tracing](/Python/tracemalloc/is_tracing/)
* [reset_peak](/Python/tracemalloc/reset_peak/)
* [start](/Python/tracemalloc/start/)
* [stop](/Python/tracemalloc/stop/)
* [take_snapshot](/Python/tracemalloc/take_snapshot/)

## Clases
* [DomainFilter](/Python/tracemalloc/DomainFilter/)
* [Filter](/Python/tracemalloc/Filter/)
* [Frame](/Python/tracemalloc/Frame/)
* [Snapshot](/Python/tracemalloc/Snapshot/)
* [Statistic](/Python/tracemalloc/Statistic/)
* [StatisticDiff](/Python/tracemalloc/StatisticDiff/)
* [Trace](/Python/tracemalloc/Trace/)
* [Traceback](/Python/tracemalloc/Traceback/)

## Ejemplo
~~~python
{{ site.data.Python.T.tracemalloc.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.Python.T.tracemalloc.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
