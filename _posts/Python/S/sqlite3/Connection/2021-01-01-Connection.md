---
title: sqlite3.Connection
permalink: /Python/sqlite3/Connection/
date: 2021-01-01
key: Python.S.sqlite3.Connection
category: python
tags: ['clase python', 'sqlite3']
sidebar: 
  nav: python
---

{% include w3api/datos.html clase=site.data.Python.S.sqlite3.Connection.metodos valor="sqlite3/Connection" %}

## Descripción
{{site.data.Python.S.sqlite3.Connection.description }}

## Sintaxis
~~~python
{{ site.data.Python.S.sqlite3.Connection.sintaxis }}~~~

## Constructores
* [Connection](/Python/sqlite3/Connection/Connection/)

## Métodos
* [backup](/Python/sqlite3/Connection/backup/)
* [close](/Python/sqlite3/Connection/close/)
* [commit](/Python/sqlite3/Connection/commit/)
* [create_aggregate](/Python/sqlite3/Connection/create_aggregate/)
* [create_collation](/Python/sqlite3/Connection/create_collation/)
* [create_function](/Python/sqlite3/Connection/create_function/)
* [cursor](/Python/sqlite3/Connection/cursor/)
* [enable_load_extension](/Python/sqlite3/Connection/enable_load_extension/)
* [execute](/Python/sqlite3/Connection/execute/)
* [executemany](/Python/sqlite3/Connection/executemany/)
* [executescript](/Python/sqlite3/Connection/executescript/)
* [interrupt](/Python/sqlite3/Connection/interrupt/)
* [iterdump](/Python/sqlite3/Connection/iterdump/)
* [load_extension](/Python/sqlite3/Connection/load_extension/)
* [rollback](/Python/sqlite3/Connection/rollback/)
* [set_authorizer](/Python/sqlite3/Connection/set_authorizer/)
* [set_progress_handler](/Python/sqlite3/Connection/set_progress_handler/)
* [set_trace_callback](/Python/sqlite3/Connection/set_trace_callback/)

## Atributos
* [in_transaction](/Python/sqlite3/Connection/in_transaction/)
* [isolation_level](/Python/sqlite3/Connection/isolation_level/)
* [row_factory](/Python/sqlite3/Connection/row_factory/)
* [text_factory](/Python/sqlite3/Connection/text_factory/)
* [total_changes](/Python/sqlite3/Connection/total_changes/)

## Ejemplo
~~~python
{{ site.data.Python.S.sqlite3.Connection.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.Python.S.sqlite3.Connection.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
