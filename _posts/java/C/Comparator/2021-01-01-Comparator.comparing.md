---
title: Comparator.comparing()
permalink: Java/Comparator/comparing
date: 2021-01-11
key: JavaJava.C.Comparator
category: java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Comparator.metodos valor="comparing" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static <T,U extends Comparable<? super U>>Comparator<T> comparing(Function<? super T,? extends U> keyExtractor)
static <T,U> Comparator<T> comparing(Function<? super T,? extends U> keyExtractor, Comparator<? super U> keyComparator)
~~~

## Parámetros
* **Comparator&lt;? super U&gt; keyComparator**,  {% include w3api/param_description.html metodo=_dato parametro="Comparator<? super U> keyComparator" %}
* **? extends U&gt; keyExtractor**,  {% include w3api/param_description.html metodo=_dato parametro="? extends U> keyExtractor" %}
* **Function&lt;? super T**,  {% include w3api/param_description.html metodo=_dato parametro="Function<? super T" %}

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
