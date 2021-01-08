---
title: PrimitiveIterator.OfDouble.forEachRemaining()
permalink: Java/PrimitiveIterator/OfDouble/forEachRemaining
date: 2021-01-04
key: JavaJava.P.PrimitiveIterator.OfDouble
category: java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PrimitiveIterator.OfDouble.metodos valor="forEachRemaining" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
default void forEachRemaining(Consumer<? super Double> action)
default void forEachRemaining(DoubleConsumer action)
~~~

## Parámetros
* **DoubleConsumer action**,  {% include w3api/param_description.html metodo=_data parametro="DoubleConsumer action" %}
* **Consumer&lt;? super Double&gt; action**,  {% include w3api/param_description.html metodo=_data parametro="Consumer<? super Double> action" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[PrimitiveIterator.OfDouble](/Java/PrimitiveIterator/OfDouble/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.P.PrimitiveIterator.OfDouble.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
