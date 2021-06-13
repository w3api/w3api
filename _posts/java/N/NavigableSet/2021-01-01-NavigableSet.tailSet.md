---
title: NavigableSet.tailSet()
permalink: /Java/NavigableSet/tailSet/
date: 2021-01-11
key: Java.N.NavigableSet
category: Java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.N.NavigableSet.metodos valor="tailSet" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
SortedSet<E> tailSet(E fromElement)
NavigableSet<E> tailSet(E fromElement, boolean inclusive)
~~~

## Parámetros
* **E fromElement**,  {% include w3api/param_description.html metodo=_dato parametro="E fromElement" %}
* **boolean inclusive**,  {% include w3api/param_description.html metodo=_dato parametro="boolean inclusive" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [ClassCastException](/Java/ClassCastException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[NavigableSet](/Java/NavigableSet/)

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
