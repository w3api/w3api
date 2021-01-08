---
title: ConcurrentNavigableMap.tailMap()
permalink: Java/ConcurrentNavigableMap/tailMap
date: 2021-01-04
key: JavaJava.C.ConcurrentNavigableMap
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ConcurrentNavigableMap.metodos valor="tailMap" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
ConcurrentNavigableMap<K,V> tailMap(K fromKey)
ConcurrentNavigableMap<K,V> tailMap(K fromKey, boolean inclusive)
~~~

## Parámetros
* **K fromKey**,  {% include w3api/param_description.html metodo=_data parametro="K fromKey" %}
* **boolean inclusive**,  {% include w3api/param_description.html metodo=_data parametro="boolean inclusive" %}

## Excepciones
[ClassCastException](/Java/ClassCastException/), [NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[ConcurrentNavigableMap](/Java/ConcurrentNavigableMap/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.ConcurrentNavigableMap.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
