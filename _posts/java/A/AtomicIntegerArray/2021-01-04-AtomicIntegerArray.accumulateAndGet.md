---
title: AtomicIntegerArray.accumulateAndGet()
permalink: Java/AtomicIntegerArray/accumulateAndGet
date: 2021-01-04
key: JavaJava.A.AtomicIntegerArray
category: java
tags: ['java se', 'java.util.concurrent.atomic', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AtomicIntegerArray.metodos valor="accumulateAndGet" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final int accumulateAndGet(int i, int x, IntBinaryOperator accumulatorFunction)
~~~

## Parámetros
* **int i**,  {% include w3api/param_description.html metodo=_data parametro="int i" %}
* **IntBinaryOperator accumulatorFunction**,  {% include w3api/param_description.html metodo=_data parametro="IntBinaryOperator accumulatorFunction" %}
* **int x**,  {% include w3api/param_description.html metodo=_data parametro="int x" %}

## Clase Padre
[AtomicIntegerArray](/Java/AtomicIntegerArray/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AtomicIntegerArray.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
