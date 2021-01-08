---
title: LongPredicate.and()
permalink: Java/LongPredicate/and
date: 2021-01-04
key: JavaJava.L.LongPredicate
category: java
tags: ['java se', 'java.util.function', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LongPredicate.metodos valor="and" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
default LongPredicate and(LongPredicate other)
~~~

## Parámetros
* **LongPredicate other**,  {% include w3api/param_description.html metodo=_data parametro="LongPredicate other" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[LongPredicate](/Java/LongPredicate/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.L.LongPredicate.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
