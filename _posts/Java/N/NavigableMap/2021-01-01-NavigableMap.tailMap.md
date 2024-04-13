---
title: NavigableMap.tailMap()
permalink: /Java/NavigableMap/tailMap/
date: 2021-01-11
key: Java.N.NavigableMap
category: Java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.N.NavigableMap.metodos valor="tailMap" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
SortedMap<K,V> tailMap(K fromKey)
NavigableMap<K,V> tailMap(K fromKey, boolean inclusive)
~~~

## Parámetros
* **K fromKey**,  {% include w3api/param_description.html metodo=_dato parametro="K fromKey" %}
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
