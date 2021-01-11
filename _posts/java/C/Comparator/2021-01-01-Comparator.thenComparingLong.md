---
title: Comparator.thenComparingLong()
permalink: Java/Comparator/thenComparingLong
date: 2021-01-11
key: JavaJava.C.Comparator
category: java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Comparator.metodos valor="thenComparingLong" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
default Comparator<T> thenComparingLong(ToLongFunction<? super T> keyExtractor)
~~~

## Parámetros
* **ToLongFunction&lt;? super T&gt; keyExtractor**,  {% include w3api/param_description.html metodo=_dato parametro="ToLongFunction<? super T> keyExtractor" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[Comparator](/Java/Comparator/)

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
