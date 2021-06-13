---
title: Spliterator.OfInt.forEachRemaining()
permalink: /Java/Spliterator/OfInt/forEachRemaining/
date: 2021-01-11
key: Java.S.Spliterator.OfInt
category: Java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.Spliterator.OfInt.metodos valor="forEachRemaining" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
default void forEachRemaining(Consumer<? super Integer> action)
~~~

## Parámetros
* **Consumer&lt;? super Integer&gt; action**,  {% include w3api/param_description.html metodo=_dato parametro="Consumer<? super Integer> action" %}

## Clase Padre
[Spliterator.OfInt](/Java/Spliterator/OfInt/)

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
