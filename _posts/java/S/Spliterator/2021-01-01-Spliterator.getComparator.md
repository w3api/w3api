---
title: Spliterator.getComparator()
permalink: Java/Spliterator/getComparator
date: 2021-01-11
key: JavaJava.S.Spliterator
category: java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.Spliterator.metodos valor="getComparator" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
default Comparator<? super T> getComparator()
~~~

## Excepciones
[IllegalStateException](/Java/IllegalStateException/)

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
