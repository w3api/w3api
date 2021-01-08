---
title: PrimitiveIterator.OfLong.forEachRemaining()
permalink: Java/PrimitiveIterator/OfLong/forEachRemaining
date: 2021-01-04
key: JavaJava.P.PrimitiveIterator.OfLong
category: java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PrimitiveIterator.OfLong.metodos valor="forEachRemaining" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
default void forEachRemaining(Consumer<? super Long> action)
default void forEachRemaining(LongConsumer action)
~~~

## Parámetros
* **LongConsumer action**,  {% include w3api/param_description.html metodo=_data parametro="LongConsumer action" %}
* **Consumer&lt;? super Long&gt; action**,  {% include w3api/param_description.html metodo=_data parametro="Consumer<? super Long> action" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[PrimitiveIterator.OfLong](/Java/PrimitiveIterator/OfLong/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.P.PrimitiveIterator.OfLong.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
