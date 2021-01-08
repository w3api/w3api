---
title: ConcurrentNavigableMap.headMap()
permalink: Java/ConcurrentNavigableMap/headMap
date: 2021-01-04
key: JavaJava.C.ConcurrentNavigableMap
category: java
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
* **boolean inclusive**,  {% include w3api/param_description.html metodo=_data parametro="boolean inclusive" %}
* **K toKey**,  {% include w3api/param_description.html metodo=_data parametro="K toKey" %}

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
