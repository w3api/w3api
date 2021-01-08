---
title: NavigableMap.tailMap()
permalink: Java/NavigableMap/tailMap
date: 2021-01-04
key: JavaJava.N.NavigableMap
category: java
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
* **K fromKey**,  {% include w3api/param_description.html metodo=_data parametro="K fromKey" %}
* **boolean inclusive**,  {% include w3api/param_description.html metodo=_data parametro="boolean inclusive" %}

## Excepciones
[ClassCastException](/Java/ClassCastException/), [NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[NavigableMap](/Java/NavigableMap/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.N.NavigableMap.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
