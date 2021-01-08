---
title: AtomicLongFieldUpdater.accumulateAndGet()
permalink: Java/AtomicLongFieldUpdater/accumulateAndGet
date: 2021-01-04
key: JavaJava.A.AtomicLongFieldUpdater
category: java
tags: ['java se', 'java.util.concurrent.atomic', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AtomicLongFieldUpdater.metodos valor="accumulateAndGet" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final long accumulateAndGet(T obj, long x, LongBinaryOperator accumulatorFunction)
~~~

## Parámetros
* **long x**,  {% include w3api/param_description.html metodo=_data parametro="long x" %}
* **LongBinaryOperator accumulatorFunction**,  {% include w3api/param_description.html metodo=_data parametro="LongBinaryOperator accumulatorFunction" %}
* **T obj**,  {% include w3api/param_description.html metodo=_data parametro="T obj" %}

## Clase Padre
[AtomicLongFieldUpdater](/Java/AtomicLongFieldUpdater/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AtomicLongFieldUpdater.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
