---
title: Collections.binarySearch()
permalink: /Java/Collections/binarySearch/
date: 2021-01-11
key: Java.C.Collections
category: Java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Collections.metodos valor="binarySearch" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static <T> int binarySearch(List<? extends Comparable<? super T>> list, T key)
static <T> int binarySearch(List<? extends T> list, T key, Comparator<? super T> c)
~~~

## Parámetros
* **Comparator&lt;? super T&gt; c**,  {% include w3api/param_description.html metodo=_dato parametro="Comparator<? super T> c" %}
* **List&lt;? extends Comparable&lt;? super T&gt;&gt; list**,  {% include w3api/param_description.html metodo=_dato parametro="List<? extends Comparable<? super T>> list" %}
* **T key**,  {% include w3api/param_description.html metodo=_dato parametro="T key" %}
* **List&lt;? extends T&gt; list**,  {% include w3api/param_description.html metodo=_dato parametro="List<? extends T> list" %}

## Clase Padre
[Collections](/Java/Collections/)

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
