---
title: ConcurrentSkipListMap.getOrDefault()
permalink: Java/ConcurrentSkipListMap/getOrDefault
date: 2021-01-04
key: JavaJava.C.ConcurrentSkipListMap
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ConcurrentSkipListMap.metodos valor="getOrDefault" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public V getOrDefault(Object key, V defaultValue)
~~~

## Parámetros
* **Object key**,  {% include w3api/param_description.html metodo=_data parametro="Object key" %}
* **V defaultValue**,  {% include w3api/param_description.html metodo=_data parametro="V defaultValue" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[ConcurrentSkipListMap](/Java/ConcurrentSkipListMap/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.ConcurrentSkipListMap.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
