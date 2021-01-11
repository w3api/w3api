---
title: Spliterator.OfLong.tryAdvance()
permalink: Java/Spliterator/OfLong/tryAdvance
date: 2021-01-11
key: JavaJava.S.Spliterator.OfLong
category: java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.Spliterator.OfLong.metodos valor="tryAdvance" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
default boolean tryAdvance(Consumer<? super Long> action)
~~~

## Parámetros
* **Consumer&lt;? super Long&gt; action**,  {% include w3api/param_description.html metodo=_dato parametro="Consumer<? super Long> action" %}

## Clase Padre
[Spliterator.OfLong](/Java/Spliterator/OfLong/)

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
