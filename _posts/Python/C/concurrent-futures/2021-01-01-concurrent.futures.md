---
title: concurrent.futures
permalink: /Python/concurrent-futures
date: 2021-01-01
key: Python.C.concurrent.futures
category: python
tags: ['modulo python']
sidebar: 
  nav: python
---

## Descripción
{{site.data.Python.C.concurrentfutures.description }}

## Funciones
* [as_completed](/Python/concurrent-futures/as_completed/)
* [wait](/Python/concurrent-futures/wait/)

## Clases
* [Executor](/Python/concurrent-futures/Executor/)
* [Future](/Python/concurrent-futures/Future/)
* [ProcessPoolExecutor](/Python/concurrent-futures/ProcessPoolExecutor/)
* [ThreadPoolExecutor](/Python/concurrent-futures/ThreadPoolExecutor/)

## Excepciones
* [BrokenExecutor](/Python/concurrent-futures/BrokenExecutor/)
* [BrokenProcessPool](/Python/concurrent-futures/BrokenProcessPool/)
* [BrokenThreadPool](/Python/concurrent-futures/BrokenThreadPool/)
* [CancelledError](/Python/concurrent-futures/CancelledError/)
* [InvalidStateError](/Python/concurrent-futures/InvalidStateError/)
* [TimeoutError](/Python/concurrent-futures/TimeoutError/)

## Ejemplo
~~~python
{{ site.data.Python.C.concurrentfutures.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.Python.C.concurrentfutures.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
