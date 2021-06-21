---
title: ConcurrentHashMap.newKeySet()
permalink: /Java/ConcurrentHashMap/newKeySet/
date: 2021-01-11
key: Java.C.ConcurrentHashMap
category: Java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ConcurrentHashMap.metodos valor="newKeySet" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static <K> ConcurrentHashMap.KeySetView<K,Boolean> newKeySet()
static <K> ConcurrentHashMap.KeySetView<K,Boolean> newKeySet(int initialCapacity)
~~~

## Parámetros
* **int initialCapacity**,  {% include w3api/param_description.html metodo=_dato parametro="int initialCapacity" %}

## Clase Padre
[ConcurrentHashMap](/Java/ConcurrentHashMap/)

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
