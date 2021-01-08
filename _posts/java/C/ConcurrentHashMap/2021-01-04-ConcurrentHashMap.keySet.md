---
title: ConcurrentHashMap.keySet()
permalink: Java/ConcurrentHashMap/keySet
date: 2021-01-04
key: JavaJava.C.ConcurrentHashMap
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ConcurrentHashMap.metodos valor="keySet" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ConcurrentHashMap.KeySetView<K,V> keySet()
public ConcurrentHashMap.KeySetView<K,V> keySet(V mappedValue)
~~~

## Parámetros
* **V mappedValue**,  {% include w3api/param_description.html metodo=_data parametro="V mappedValue" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[ConcurrentHashMap](/Java/ConcurrentHashMap/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.ConcurrentHashMap.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
