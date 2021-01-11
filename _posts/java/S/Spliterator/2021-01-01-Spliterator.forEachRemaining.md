---
title: Spliterator.forEachRemaining()
permalink: Java/Spliterator/forEachRemaining
date: 2021-01-11
key: JavaJava.S.Spliterator
category: java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.Spliterator.metodos valor="forEachRemaining" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
default void forEachRemaining(Consumer<? super T> action)
~~~

## Parámetros
* **Consumer&lt;? super T&gt; action**,  {% include w3api/param_description.html metodo=_dato parametro="Consumer<? super T> action" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[Spliterator](/Java/Spliterator/)

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
