---
title: Comparator.comparingDouble()
permalink: Java/Comparator/comparingDouble
date: 2021-01-11
key: JavaJava.C.Comparator
category: java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Comparator.metodos valor="comparingDouble" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static <T> Comparator<T> comparingDouble(ToDoubleFunction<? super T> keyExtractor)
~~~

## Parámetros
* **ToDoubleFunction&lt;? super T&gt; keyExtractor**,  {% include w3api/param_description.html metodo=_dato parametro="ToDoubleFunction<? super T> keyExtractor" %}

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
