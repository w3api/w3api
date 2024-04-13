---
title: Comparator.comparingInt()
permalink: /Java/Comparator/comparingInt/
date: 2021-01-11
key: Java.C.Comparator
category: Java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Comparator.metodos valor="comparingInt" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static <T> Comparator<T> comparingInt(ToIntFunction<? super T> keyExtractor)
~~~

## Parámetros
* **ToIntFunction&lt;? super T&gt; keyExtractor**,  {% include w3api/param_description.html metodo=_dato parametro="ToIntFunction<? super T> keyExtractor" %}

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
