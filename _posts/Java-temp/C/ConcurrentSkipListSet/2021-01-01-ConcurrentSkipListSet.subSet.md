---
title: ConcurrentSkipListSet.subSet()
permalink: /Java/ConcurrentSkipListSet/subSet/
date: 2021-01-11
key: Java.C.ConcurrentSkipListSet
category: Java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ConcurrentSkipListSet.metodos valor="subSet" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public NavigableSet<E> subSet(E fromElement, boolean fromInclusive, E toElement, boolean toInclusive)
public NavigableSet<E> subSet(E fromElement, E toElement)
~~~

## Parámetros
* **E toElement**,  {% include w3api/param_description.html metodo=_dato parametro="E toElement" %}
* **boolean fromInclusive**,  {% include w3api/param_description.html metodo=_dato parametro="boolean fromInclusive" %}
* **E fromElement**,  {% include w3api/param_description.html metodo=_dato parametro="E fromElement" %}
* **boolean toInclusive**,  {% include w3api/param_description.html metodo=_dato parametro="boolean toInclusive" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [ClassCastException](/Java/ClassCastException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[ConcurrentSkipListSet](/Java/ConcurrentSkipListSet/)

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
