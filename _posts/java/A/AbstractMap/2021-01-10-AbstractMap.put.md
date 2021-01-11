---
title: AbstractMap.put()
permalink: Java/AbstractMap/put
date: 2021-01-10
key: JavaJava.A.AbstractMap
category: java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AbstractMap.metodos valor="put" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public V put(K key, V value)
~~~

## Parámetros
* **K key**,  {% include w3api/param_description.html metodo=_dato parametro="K key" %}
* **V value**,  {% include w3api/param_description.html metodo=_dato parametro="V value" %}

## Excepciones
[ClassCastException](/Java/ClassCastException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[AbstractMap](/Java/AbstractMap/)

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
