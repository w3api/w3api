---
title: Comparator.thenComparingInt()
permalink: Java/Comparator/thenComparingInt
date: 2021-01-04
key: JavaJava.C.Comparator
category: java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Comparator.metodos valor="thenComparingInt" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
default Comparator<T> thenComparingInt(ToIntFunction<? super T> keyExtractor)
~~~

## Parámetros
* **ToIntFunction&lt;? super T&gt; keyExtractor**,  {% include w3api/param_description.html metodo=_data parametro="ToIntFunction<? super T> keyExtractor" %}

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
{%- for _ldc in site.data.Java.C.Comparator.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
