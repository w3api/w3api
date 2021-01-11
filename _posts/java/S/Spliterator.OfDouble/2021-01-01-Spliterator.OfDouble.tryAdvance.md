---
title: Spliterator.OfDouble.tryAdvance()
permalink: Java/Spliterator/OfDouble/tryAdvance
date: 2021-01-11
key: JavaJava.S.Spliterator.OfDouble
category: java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.Spliterator.OfDouble.metodos valor="tryAdvance" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
default boolean tryAdvance(Consumer<? super Double> action)
~~~

## Parámetros
* **Consumer&lt;? super Double&gt; action**,  {% include w3api/param_description.html metodo=_dato parametro="Consumer<? super Double> action" %}

## Clase Padre
[Spliterator.OfDouble](/Java/Spliterator/OfDouble/)

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