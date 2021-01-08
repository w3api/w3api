---
title: Comparator.compare()
permalink: Java/Comparator/compare
date: 2021-01-04
key: JavaJava.C.Comparator
category: java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Comparator.metodos valor="compare" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
int compare(T o1, T o2)
~~~

## Parámetros
* **T o1**,  {% include w3api/param_description.html metodo=_data parametro="T o1" %}
* **T o2**,  {% include w3api/param_description.html metodo=_data parametro="T o2" %}

## Excepciones
[ClassCastException](/Java/ClassCastException/), [NullPointerException](/Java/NullPointerException/)

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
