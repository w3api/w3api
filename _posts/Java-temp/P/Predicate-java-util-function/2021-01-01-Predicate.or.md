---
title: Predicate.or()
permalink: /Java/Predicate-java-util-function/or/
date: 2021-01-11
key: Java.P.Predicate-java-util-function
category: Java
tags: ['java se', 'java.util.function', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.Predicate-java-util-function.metodos valor="or" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
default Predicate<T> or(Predicate<? super T> other)
~~~

## Parámetros
* **Predicate&lt;? super T&gt; other**,  {% include w3api/param_description.html metodo=_dato parametro="Predicate<? super T> other" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[Predicate](/Java/Predicate-java-util-function/)

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
