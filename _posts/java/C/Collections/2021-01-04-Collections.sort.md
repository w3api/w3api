---
title: Collections.sort()
permalink: Java/Collections/sort
date: 2021-01-04
key: JavaJava.C.Collections
category: java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Collections.metodos valor="sort" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static <T extends Comparable<? super T>>void sort(List<T> list)
static <T> void sort(List<T> list, Comparator<? super T> c)
~~~

## Parámetros
* **Comparator&lt;? super T&gt; c**,  {% include w3api/param_description.html metodo=_data parametro="Comparator<? super T> c" %}
* **List&lt;T&gt; list**,  {% include w3api/param_description.html metodo=_data parametro="List<T> list" %}

## Clase Padre
[Collections](/Java/Collections/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.Collections.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
