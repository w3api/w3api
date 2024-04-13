---
title: Spliterator.OfDouble.forEachRemaining()
permalink: /Java/Spliterator/OfDouble/forEachRemaining/
date: 2021-01-11
key: Java.S.Spliterator.OfDouble
category: Java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.Spliterator.OfDouble.metodos valor="forEachRemaining" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
default void forEachRemaining(Consumer<? super Double> action)
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
