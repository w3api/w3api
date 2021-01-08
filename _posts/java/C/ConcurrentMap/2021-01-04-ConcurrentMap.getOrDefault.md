---
title: ConcurrentMap.getOrDefault()
permalink: Java/ConcurrentMap/getOrDefault
date: 2021-01-04
key: JavaJava.C.ConcurrentMap
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ConcurrentMap.metodos valor="getOrDefault" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
default V getOrDefault(Object key, V defaultValue)
~~~

## Parámetros
* **Object key**,  {% include w3api/param_description.html metodo=_data parametro="Object key" %}
* **V defaultValue**,  {% include w3api/param_description.html metodo=_data parametro="V defaultValue" %}

## Excepciones
[ClassCastException](/Java/ClassCastException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[ConcurrentMap](/Java/ConcurrentMap/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.ConcurrentMap.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
