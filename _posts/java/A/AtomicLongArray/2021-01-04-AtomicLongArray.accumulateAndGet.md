---
title: AtomicLongArray.accumulateAndGet()
permalink: Java/AtomicLongArray/accumulateAndGet
date: 2021-01-04
key: JavaJava.A.AtomicLongArray
category: java
tags: ['java se', 'java.util.concurrent.atomic', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AtomicLongArray.metodos valor="accumulateAndGet" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final long accumulateAndGet(int i, long x, LongBinaryOperator accumulatorFunction)
~~~

## Parámetros
* **int i**,  {% include w3api/param_description.html metodo=_data parametro="int i" %}
* **long x**,  {% include w3api/param_description.html metodo=_data parametro="long x" %}
* **LongBinaryOperator accumulatorFunction**,  {% include w3api/param_description.html metodo=_data parametro="LongBinaryOperator accumulatorFunction" %}

## Clase Padre
[AtomicLongArray](/Java/AtomicLongArray/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AtomicLongArray.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
