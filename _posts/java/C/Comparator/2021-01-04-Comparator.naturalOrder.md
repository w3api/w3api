---
title: Comparator.naturalOrder()
permalink: Java/Comparator/naturalOrder
date: 2021-01-04
key: JavaJava.C.Comparator
category: java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Comparator.metodos valor="naturalOrder" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static <T extends Comparable<? super T>>Comparator<T> naturalOrder()
~~~

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
