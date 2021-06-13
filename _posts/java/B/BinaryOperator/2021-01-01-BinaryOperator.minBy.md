---
title: BinaryOperator.minBy()
permalink: /Java/BinaryOperator/minBy/
date: 2021-01-11
key: JavaJava.B.BinaryOperator
category: java
tags: ['java se', 'java.util.function', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BinaryOperator.metodos valor="minBy" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static <T> BinaryOperator<T> minBy(Comparator<? super T> comparator)
~~~

## Parámetros
* **Comparator&lt;? super T&gt; comparator**,  {% include w3api/param_description.html metodo=_dato parametro="Comparator<? super T> comparator" %}

## Clase Padre
[BinaryOperator](/Java/BinaryOperator/)

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
