---
title: ConcurrentSkipListMap.replace()
permalink: /Java/ConcurrentSkipListMap/replace/
date: 2021-01-11
key: Java.C.ConcurrentSkipListMap
category: Java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ConcurrentSkipListMap.metodos valor="replace" %}

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
[ClassCastException](/Java/ClassCastException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[ConcurrentSkipListMap](/Java/ConcurrentSkipListMap/)

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
