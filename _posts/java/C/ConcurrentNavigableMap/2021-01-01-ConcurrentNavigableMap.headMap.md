---
title: ConcurrentNavigableMap.headMap()
permalink: /Java/ConcurrentNavigableMap/headMap/
date: 2021-01-11
key: Java.C.ConcurrentNavigableMap
category: Java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ConcurrentNavigableMap.metodos valor="headMap" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
ConcurrentNavigableMap<K,V> headMap(K toKey)
ConcurrentNavigableMap<K,V> headMap(K toKey, boolean inclusive)
~~~

## Parámetros
* **K toKey**,  {% include w3api/param_description.html metodo=_dato parametro="K toKey" %}
* **boolean inclusive**,  {% include w3api/param_description.html metodo=_dato parametro="boolean inclusive" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [ClassCastException](/Java/ClassCastException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[ConcurrentNavigableMap](/Java/ConcurrentNavigableMap/)

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
