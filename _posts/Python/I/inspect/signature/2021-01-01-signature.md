---
title: inspect.Signature
permalink: /Python/inspect/Signature/
date: 2021-01-01
key: Python.I.inspect.Signature
category: python
tags: ['clase python', 'inspect']
sidebar: 
  nav: python
---

{% include w3api/datos.html clase=site.data.Python.I.inspect.Signature.metodos valor="inspect/Signature" %}

## Descripción
{{site.data.Python.I.inspect.Signature.description }}

## Sintaxis
~~~python
{{ site.data.Python.I.inspect.Signature.sintaxis }}~~~

## Constructores
* [Signature](/Python/inspect/Signature/Signature/)

## Métodos
* [bind](/Python/inspect/Signature/bind/)
* [bind_partial](/Python/inspect/Signature/bind_partial/)
* [from_callable](/Python/inspect/Signature/from_callable/)
* [replace](/Python/inspect/Signature/replace/)

## Atributos
* [empty](/Python/inspect/Signature/empty/)
* [parameters](/Python/inspect/Signature/parameters/)
* [return_annotation](/Python/inspect/Signature/return_annotation/)

## Ejemplo
~~~python
{{ site.data.Python.I.inspect.Signature.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.Python.I.inspect.Signature.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
