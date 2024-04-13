---
title: AtomicLongArray.getAndAccumulate()
permalink: /Java/AtomicLongArray/getAndAccumulate/
date: 2021-01-11
key: Java.A.AtomicLongArray
category: Java
tags: ['java se', 'java.util.concurrent.atomic', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AtomicLongArray.metodos valor="getAndAccumulate" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final long getAndAccumulate(int i, long x, LongBinaryOperator accumulatorFunction)
~~~

## Parámetros
* **long x**,  {% include w3api/param_description.html metodo=_dato parametro="long x" %}
* **int i**,  {% include w3api/param_description.html metodo=_dato parametro="int i" %}
* **LongBinaryOperator accumulatorFunction**,  {% include w3api/param_description.html metodo=_dato parametro="LongBinaryOperator accumulatorFunction" %}

## Clase Padre
[AtomicLongArray](/Java/AtomicLongArray/)

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
