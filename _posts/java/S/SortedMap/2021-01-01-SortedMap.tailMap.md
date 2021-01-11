---
title: SortedMap.tailMap()
permalink: Java/SortedMap/tailMap
date: 2021-01-11
key: JavaJava.S.SortedMap
category: java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SortedMap.metodos valor="tailMap" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
SortedMap<K,V> tailMap(K fromKey)
~~~

## Parámetros
* **K fromKey**,  {% include w3api/param_description.html metodo=_dato parametro="K fromKey" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [ClassCastException](/Java/ClassCastException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[SortedMap](/Java/SortedMap/)

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
