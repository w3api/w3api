---
title: Predicate.and()
permalink: Java/Predicate-java-util-function/and
date: 2021-01-04
key: JavaJava.P.Predicate-java-util-function
category: java
tags: ['java se', 'java.util.function', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.Predicate-java-util-function.metodos valor="and" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
default Predicate<T> and(Predicate<? super T> other)
~~~

## Parámetros
* **Predicate&lt;? super T&gt; other**,  {% include w3api/param_description.html metodo=_data parametro="Predicate<? super T> other" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[Predicate](/Java/Predicate-java-util-function/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.P.Predicate-java-util-function.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
