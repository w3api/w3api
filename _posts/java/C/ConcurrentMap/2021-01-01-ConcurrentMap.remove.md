---
title: ConcurrentMap.remove()
permalink: /Java/ConcurrentMap/remove/
date: 2021-01-11
key: Java.C.ConcurrentMap
category: Java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ConcurrentMap.metodos valor="remove" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
boolean remove(Object key, Object value)
~~~

## Parámetros
* **Object key**,  {% include w3api/param_description.html metodo=_dato parametro="Object key" %}
* **Object value**,  {% include w3api/param_description.html metodo=_dato parametro="Object value" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [ClassCastException](/Java/ClassCastException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/)

## Clase Padre
[ConcurrentMap](/Java/ConcurrentMap/)

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
