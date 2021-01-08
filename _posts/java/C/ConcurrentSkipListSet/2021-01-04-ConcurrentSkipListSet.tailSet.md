---
title: ConcurrentSkipListSet.tailSet()
permalink: Java/ConcurrentSkipListSet/tailSet
date: 2021-01-04
key: JavaJava.C.ConcurrentSkipListSet
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ConcurrentSkipListSet.metodos valor="tailSet" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public NavigableSet<E> tailSet(E fromElement)
public NavigableSet<E> tailSet(E fromElement, boolean inclusive)
~~~

## Parámetros
* **E fromElement**,  {% include w3api/param_description.html metodo=_data parametro="E fromElement" %}
* **boolean inclusive**,  {% include w3api/param_description.html metodo=_data parametro="boolean inclusive" %}

## Excepciones
[ClassCastException](/Java/ClassCastException/), [NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[ConcurrentSkipListSet](/Java/ConcurrentSkipListSet/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.ConcurrentSkipListSet.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
