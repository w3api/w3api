---
title: Spliterator.OfLong.forEachRemaining()
permalink: /Java/Spliterator/OfLong/forEachRemaining/
date: 2021-01-11
key: Java.S.Spliterator.OfLong
category: Java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.Spliterator.OfLong.metodos valor="forEachRemaining" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
default void forEachRemaining(Consumer<? super Long> action)
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
