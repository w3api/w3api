---
title: ConcurrentSkipListMap.put()
permalink: Java/ConcurrentSkipListMap/put
date: 2021-01-11
key: JavaJava.C.ConcurrentSkipListMap
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ConcurrentSkipListMap.metodos valor="put" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public V put(K key, V value)
~~~

## Parámetros
* **V value**,  {% include w3api/param_description.html metodo=_dato parametro="V value" %}
* **K key**,  {% include w3api/param_description.html metodo=_dato parametro="K key" %}

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