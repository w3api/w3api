---
title: SortedMap.tailMap()
permalink: Java/SortedMap/tailMap
date: 2021-01-04
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
* **K fromKey**,  {% include w3api/param_description.html metodo=_data parametro="K fromKey" %}

## Excepciones
[ClassCastException](/Java/ClassCastException/), [NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[SortedMap](/Java/SortedMap/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SortedMap.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
