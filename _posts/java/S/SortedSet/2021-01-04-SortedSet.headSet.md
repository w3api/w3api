---
title: SortedSet.headSet()
permalink: Java/SortedSet/headSet
date: 2021-01-04
key: JavaJava.S.SortedSet
category: java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SortedSet.metodos valor="headSet" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
SortedSet<E> headSet(E toElement)
~~~

## Parámetros
* **E toElement**,  {% include w3api/param_description.html metodo=_data parametro="E toElement" %}

## Excepciones
[ClassCastException](/Java/ClassCastException/), [NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[SortedSet](/Java/SortedSet/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SortedSet.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
