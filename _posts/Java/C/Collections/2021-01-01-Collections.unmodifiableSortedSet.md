---
title: Collections.unmodifiableSortedSet()
permalink: /Java/Collections/unmodifiableSortedSet/
date: 2021-01-11
key: Java.C.Collections
category: Java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Collections.metodos valor="unmodifiableSortedSet" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static <T> SortedSet<T> unmodifiableSortedSet(SortedSet<T> s)
~~~

## Parámetros
* **SortedSet&lt;T&gt; s**,  {% include w3api/param_description.html metodo=_dato parametro="SortedSet<T> s" %}

## Clase Padre
[Collections](/Java/Collections/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
