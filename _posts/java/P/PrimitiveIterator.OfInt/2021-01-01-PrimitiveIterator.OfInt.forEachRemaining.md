---
title: PrimitiveIterator.OfInt.forEachRemaining()
permalink: Java/PrimitiveIterator/OfInt/forEachRemaining
date: 2021-01-11
key: JavaJava.P.PrimitiveIterator.OfInt
category: java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PrimitiveIterator.OfInt.metodos valor="forEachRemaining" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
default void forEachRemaining(Consumer<? super Integer> action)
default void forEachRemaining(IntConsumer action)
~~~

## Parámetros
* **IntConsumer action**,  {% include w3api/param_description.html metodo=_dato parametro="IntConsumer action" %}
* **Consumer&lt;? super Integer&gt; action**,  {% include w3api/param_description.html metodo=_dato parametro="Consumer<? super Integer> action" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[PrimitiveIterator.OfInt](/Java/PrimitiveIterator/OfInt/)

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
