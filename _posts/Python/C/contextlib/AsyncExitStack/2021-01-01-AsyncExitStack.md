---
title: contextlib.AsyncExitStack
permalink: /Python/contextlib/AsyncExitStack/
date: 2021-01-01
key: Python.C.contextlib.AsyncExitStack
category: python
tags: ['clase python', 'contextlib']
sidebar: 
  nav: python
---

{% include w3api/datos.html clase=site.data.Python.C.contextlib.AsyncExitStack.metodos valor="contextlib/AsyncExitStack" %}

## Descripción
{{site.data.Python.C.contextlib.AsyncExitStack.description }}

## Sintaxis
~~~python
{{ site.data.Python.C.contextlib.AsyncExitStack.sintaxis }}~~~

## Constructores
* [AsyncExitStack](/Python/contextlib/AsyncExitStack/AsyncExitStack/)

## Métodos
* [aclose](/Python/contextlib/AsyncExitStack/aclose/)
* [enter_async_context](/Python/contextlib/AsyncExitStack/enter_async_context/)
* [push_async_callback](/Python/contextlib/AsyncExitStack/push_async_callback/)
* [push_async_exit](/Python/contextlib/AsyncExitStack/push_async_exit/)

## Ejemplo
~~~python
{{ site.data.Python.C.contextlib.AsyncExitStack.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.Python.C.contextlib.AsyncExitStack.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
