---
title: NavigableMap.floorEntry()
permalink: Java/NavigableMap/floorEntry
date: 2021-01-11
key: JavaJava.N.NavigableMap
category: java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.N.NavigableMap.metodos valor="floorEntry" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Map.Entry<K,V> floorEntry(K key)
~~~

## Parámetros
* **K key**,  {% include w3api/param_description.html metodo=_dato parametro="K key" %}

## Excepciones
[ClassCastException](/Java/ClassCastException/), [NullPointerException](/Java/NullPointerException/)

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