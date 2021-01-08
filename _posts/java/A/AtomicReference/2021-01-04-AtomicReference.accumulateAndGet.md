---
title: AtomicReference.accumulateAndGet()
permalink: Java/AtomicReference/accumulateAndGet
date: 2021-01-04
key: JavaJava.A.AtomicReference
category: java
tags: ['java se', 'java.util.concurrent.atomic', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AtomicReference.metodos valor="accumulateAndGet" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final V accumulateAndGet(V x, BinaryOperator<V> accumulatorFunction)
~~~

## Parámetros
* **BinaryOperator&lt;V&gt; accumulatorFunction**,  {% include w3api/param_description.html metodo=_data parametro="BinaryOperator<V> accumulatorFunction" %}
* **V x**,  {% include w3api/param_description.html metodo=_data parametro="V x" %}

## Clase Padre
[AtomicReference](/Java/AtomicReference/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AtomicReference.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
