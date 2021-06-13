---
title: ConcurrentHashMap.replace()
permalink: /Java/ConcurrentHashMap/replace/
date: 2021-01-11
key: Java.C.ConcurrentHashMap
category: Java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ConcurrentHashMap.metodos valor="replace" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public V replace(K key, V value)
public boolean replace(K key, V oldValue, V newValue)
~~~

## Parámetros
* **V value**,  {% include w3api/param_description.html metodo=_dato parametro="V value" %}
* **V newValue**,  {% include w3api/param_description.html metodo=_dato parametro="V newValue" %}
* **K key**,  {% include w3api/param_description.html metodo=_dato parametro="K key" %}
* **V oldValue**,  {% include w3api/param_description.html metodo=_dato parametro="V oldValue" %}

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
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
