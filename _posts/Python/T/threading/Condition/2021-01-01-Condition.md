---
title: threading.Condition
permalink: /Python/threading/Condition/
date: 2021-01-01
key: Python.T.threading.Condition
category: python
tags: ['clase python', 'threading']
sidebar: 
  nav: python
---

{% include w3api/datos.html clase=site.data.Python.T.threading.Condition.metodos valor="threading/Condition" %}

## Descripción
{{site.data.Python.T.threading.Condition.description }}

## Sintaxis
~~~python
{{ site.data.Python.T.threading.Condition.sintaxis }}~~~

## Constructores
* [Condition](/Python/threading/Condition/Condition/)

## Métodos
* [acquire](/Python/threading/Condition/acquire/)
* [notify](/Python/threading/Condition/notify/)
* [notify_all](/Python/threading/Condition/notify_all/)
* [release](/Python/threading/Condition/release/)
* [wait](/Python/threading/Condition/wait/)
* [wait_for](/Python/threading/Condition/wait_for/)

## Ejemplo
~~~python
{{ site.data.Python.T.threading.Condition.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.Python.T.threading.Condition.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
