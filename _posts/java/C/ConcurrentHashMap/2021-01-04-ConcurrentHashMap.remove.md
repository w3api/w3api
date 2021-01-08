---
title: ConcurrentHashMap.remove()
permalink: Java/ConcurrentHashMap/remove
date: 2021-01-04
key: JavaJava.C.ConcurrentHashMap
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ConcurrentHashMap.metodos valor="remove" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public V remove(Object key)
public boolean remove(Object key, Object value)
~~~

## Parámetros
* **Object key**,  {% include w3api/param_description.html metodo=_data parametro="Object key" %}
* **Object value**,  {% include w3api/param_description.html metodo=_data parametro="Object value" %}

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
