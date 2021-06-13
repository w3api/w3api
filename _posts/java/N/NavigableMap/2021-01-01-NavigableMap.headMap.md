---
title: NavigableMap.headMap()
permalink: Java/NavigableMap/headMap
date: 2021-01-11
key: JavaJava.N.NavigableMap
category: Java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.N.NavigableMap.metodos valor="headMap" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
SortedMap<K,V> headMap(K toKey)
NavigableMap<K,V> headMap(K toKey, boolean inclusive)
~~~

## Parámetros
* **K toKey**,  {% include w3api/param_description.html metodo=_dato parametro="K toKey" %}
* **boolean inclusive**,  {% include w3api/param_description.html metodo=_dato parametro="boolean inclusive" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [ClassCastException](/Java/ClassCastException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[NavigableMap](/Java/NavigableMap/)

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
