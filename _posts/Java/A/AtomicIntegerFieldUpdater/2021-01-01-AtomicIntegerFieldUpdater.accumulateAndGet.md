---
title: AtomicIntegerFieldUpdater.accumulateAndGet()
permalink: /Java/AtomicIntegerFieldUpdater/accumulateAndGet/
date: 2021-01-11
key: Java.A.AtomicIntegerFieldUpdater
category: Java
tags: ['java se', 'java.util.concurrent.atomic', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AtomicIntegerFieldUpdater.metodos valor="accumulateAndGet" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final int accumulateAndGet(T obj, int x, IntBinaryOperator accumulatorFunction)
~~~

## Parámetros
* **int x**,  {% include w3api/param_description.html metodo=_dato parametro="int x" %}
* **IntBinaryOperator accumulatorFunction**,  {% include w3api/param_description.html metodo=_dato parametro="IntBinaryOperator accumulatorFunction" %}
* **T obj**,  {% include w3api/param_description.html metodo=_dato parametro="T obj" %}

## Clase Padre
[AtomicIntegerFieldUpdater](/Java/AtomicIntegerFieldUpdater/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
