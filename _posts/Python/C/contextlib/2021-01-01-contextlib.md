---
title: contextlib
permalink: /Python/contextlib
date: 2021-01-01
key: Python.C.contextlib
category: python
tags: ['modulo python']
sidebar: 
  nav: python
---

## Descripción
{{site.data.Python.C.contextlib.description }}

## Funciones
* [asynccontextmanager](/Python/contextlib/asynccontextmanager/)
* [closing](/Python/contextlib/closing/)
* [contextmanager](/Python/contextlib/contextmanager/)
* [nullcontext](/Python/contextlib/nullcontext/)
* [redirect_stderr](/Python/contextlib/redirect_stderr/)
* [redirect_stdout](/Python/contextlib/redirect_stdout/)
* [suppress](/Python/contextlib/suppress/)

## Clases
* [AbstractAsyncContextManager](/Python/contextlib/AbstractAsyncContextManager/)
* [AbstractContextManager](/Python/contextlib/AbstractContextManager/)
* [aclosing](/Python/contextlib/aclosing/)
* [AsyncContextDecorator](/Python/contextlib/AsyncContextDecorator/)
* [AsyncExitStack](/Python/contextlib/AsyncExitStack/)
* [ContextDecorator](/Python/contextlib/ContextDecorator/)
* [ExitStack](/Python/contextlib/ExitStack/)

## Ejemplo
~~~python
{{ site.data.Python.C.contextlib.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.Python.C.contextlib.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
