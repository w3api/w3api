---
title: AtomicIntegerFieldUpdater.getAndSet()
permalink: /Java/AtomicIntegerFieldUpdater/getAndSet/
date: 2021-01-11
key: Java.A.AtomicIntegerFieldUpdater
category: Java
tags: ['java se', 'java.util.concurrent.atomic', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AtomicIntegerFieldUpdater.metodos valor="getAndSet" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public int getAndSet(T obj, int newValue)
~~~

## Parámetros
* **int newValue**,  {% include w3api/param_description.html metodo=_dato parametro="int newValue" %}
* **T obj**,  {% include w3api/param_description.html metodo=_dato parametro="T obj" %}

## Clase Padre
[AtomicIntegerFieldUpdater](/Java/AtomicIntegerFieldUpdater/)

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
