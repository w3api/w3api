---
title: PrimitiveIterator.OfLong.forEachRemaining()
permalink: /Java/PrimitiveIterator/OfLong/forEachRemaining/
date: 2021-01-11
key: Java.P.PrimitiveIterator.OfLong
category: Java
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
* **Consumer&lt;? super Long&gt; action**,  {% include w3api/param_description.html metodo=_dato parametro="Consumer<? super Long> action" %}
* **LongConsumer action**,  {% include w3api/param_description.html metodo=_dato parametro="LongConsumer action" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[PrimitiveIterator.OfLong](/Java/PrimitiveIterator/OfLong/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
