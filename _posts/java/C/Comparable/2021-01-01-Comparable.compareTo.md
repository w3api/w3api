---
title: Comparable.compareTo()
permalink: Java/Comparable/compareTo
date: 2021-01-11
key: JavaJava.C.Comparable
category: java
tags: ['java se', 'java.lang', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Comparable.metodos valor="compareTo" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
int compareTo(T o)
~~~

## Parámetros
* **T o**,  {% include w3api/param_description.html metodo=_dato parametro="T o" %}

## Excepciones
[ClassCastException](/Java/ClassCastException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[Comparable](/Java/Comparable/)

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
