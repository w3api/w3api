---
title: ConcurrentSkipListSet.subSet()
permalink: Java/ConcurrentSkipListSet/subSet
date: 2021-01-04
key: JavaJava.C.ConcurrentSkipListSet
category: java
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
* **boolean fromInclusive**,  {% include w3api/param_description.html metodo=_data parametro="boolean fromInclusive" %}
* **E fromElement**,  {% include w3api/param_description.html metodo=_data parametro="E fromElement" %}
* **E toElement**,  {% include w3api/param_description.html metodo=_data parametro="E toElement" %}
* **boolean toInclusive**,  {% include w3api/param_description.html metodo=_data parametro="boolean toInclusive" %}

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
