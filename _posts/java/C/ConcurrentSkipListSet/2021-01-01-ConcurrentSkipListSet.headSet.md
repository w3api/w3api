---
title: ConcurrentSkipListSet.headSet()
permalink: /Java/ConcurrentSkipListSet/headSet/
date: 2021-01-11
key: Java.C.ConcurrentSkipListSet
category: Java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ConcurrentSkipListSet.metodos valor="headSet" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public NavigableSet<E> headSet(E toElement)
public NavigableSet<E> headSet(E toElement, boolean inclusive)
~~~

## Parámetros
* **E toElement**,  {% include w3api/param_description.html metodo=_dato parametro="E toElement" %}
* **boolean inclusive**,  {% include w3api/param_description.html metodo=_dato parametro="boolean inclusive" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [ClassCastException](/Java/ClassCastException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[ConcurrentSkipListSet](/Java/ConcurrentSkipListSet/)

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
