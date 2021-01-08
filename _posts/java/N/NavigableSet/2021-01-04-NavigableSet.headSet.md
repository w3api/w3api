---
title: NavigableSet.headSet()
permalink: Java/NavigableSet/headSet
date: 2021-01-04
key: JavaJava.N.NavigableSet
category: java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.N.NavigableSet.metodos valor="headSet" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
SortedSet<E> headSet(E toElement)
NavigableSet<E> headSet(E toElement, boolean inclusive)
~~~

## Parámetros
* **E toElement**,  {% include w3api/param_description.html metodo=_data parametro="E toElement" %}
* **boolean inclusive**,  {% include w3api/param_description.html metodo=_data parametro="boolean inclusive" %}

## Excepciones
[ClassCastException](/Java/ClassCastException/), [NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[NavigableSet](/Java/NavigableSet/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.N.NavigableSet.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
