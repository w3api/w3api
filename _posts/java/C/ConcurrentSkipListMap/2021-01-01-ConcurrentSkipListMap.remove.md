---
title: ConcurrentSkipListMap.remove()
permalink: /Java/ConcurrentSkipListMap/remove/
date: 2021-01-11
key: Java.C.ConcurrentSkipListMap
category: Java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ConcurrentSkipListMap.metodos valor="remove" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public V remove(Object key)
public boolean remove(Object key, Object value)
~~~

## Parámetros
* **Object key**,  {% include w3api/param_description.html metodo=_dato parametro="Object key" %}
* **Object value**,  {% include w3api/param_description.html metodo=_dato parametro="Object value" %}

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
