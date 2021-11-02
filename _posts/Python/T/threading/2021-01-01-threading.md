---
title: threading
permalink: /Python/threading
date: 2021-01-01
key: Python.T.threading
category: python
tags: ['modulo python']
sidebar: 
  nav: python
---

## Descripción
{{site.data.Python.T.threading.description }}

## Funciones
* [active_count](/Python/threading/active_count/)
* [current_thread](/Python/threading/current_thread/)
* [enumerate](/Python/threading/enumerate/)
* [excepthook](/Python/threading/excepthook/)
* [getprofile](/Python/threading/getprofile/)
* [gettrace](/Python/threading/gettrace/)
* [get_ident](/Python/threading/get_ident/)
* [get_native_id](/Python/threading/get_native_id/)
* [main_thread](/Python/threading/main_thread/)
* [setprofile](/Python/threading/setprofile/)
* [settrace](/Python/threading/settrace/)
* [stack_size](/Python/threading/stack_size/)

## Clases
* [Barrier](/Python/threading/Barrier/)
* [BoundedSemaphore](/Python/threading/BoundedSemaphore/)
* [Condition](/Python/threading/Condition/)
* [Event](/Python/threading/Event/)
* [local](/Python/threading/local/)
* [Lock](/Python/threading/Lock/)
* [RLock](/Python/threading/RLock/)
* [Semaphore](/Python/threading/Semaphore/)
* [Thread](/Python/threading/Thread/)
* [Timer](/Python/threading/Timer/)

## Excepciones
* [BrokenBarrierError](/Python/threading/BrokenBarrierError/)

## Constantes
* [TIMEOUT_MAX](/Python/threading/TIMEOUT_MAX/)
* [__excepthook__](/Python/threading/__excepthook__/)

## Ejemplo
~~~python
{{ site.data.Python.T.threading.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.Python.T.threading.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
