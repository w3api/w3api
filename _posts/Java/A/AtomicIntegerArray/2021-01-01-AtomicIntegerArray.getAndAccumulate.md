---
title: AtomicIntegerArray.getAndAccumulate()
permalink: /Java/AtomicIntegerArray/getAndAccumulate/
date: 2021-01-11
key: Java.A.AtomicIntegerArray
category: Java
tags: ['java se', 'java.util.concurrent.atomic', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AtomicIntegerArray.metodos valor="getAndAccumulate" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final int getAndAccumulate(int i, int x, IntBinaryOperator accumulatorFunction)
~~~

## Parámetros
* **int x**,  {% include w3api/param_description.html metodo=_dato parametro="int x" %}
* **IntBinaryOperator accumulatorFunction**,  {% include w3api/param_description.html metodo=_dato parametro="IntBinaryOperator accumulatorFunction" %}
* **int i**,  {% include w3api/param_description.html metodo=_dato parametro="int i" %}

## Clase Padre
[AtomicIntegerArray](/Java/AtomicIntegerArray/)

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
