---
title: Comparator.nullsLast()
permalink: /Java/Comparator/nullsLast/
date: 2021-01-11
key: Java.C.Comparator
category: Java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Comparator.metodos valor="nullsLast" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static <T> Comparator<T> nullsLast(Comparator<? super T> comparator)
~~~

## Parámetros
* **Comparator&lt;? super T&gt; comparator**,  {% include w3api/param_description.html metodo=_dato parametro="Comparator<? super T> comparator" %}

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
