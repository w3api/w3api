---
title: AtomicLongFieldUpdater.compareAndSet()
permalink: Java/AtomicLongFieldUpdater/compareAndSet
date: 2021-01-11
key: JavaJava.A.AtomicLongFieldUpdater
category: java
tags: ['java se', 'java.util.concurrent.atomic', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AtomicLongFieldUpdater.metodos valor="compareAndSet" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract boolean compareAndSet(T obj, long expect, long update)
~~~

## Parámetros
* **long expect**,  {% include w3api/param_description.html metodo=_dato parametro="long expect" %}
* **T obj**,  {% include w3api/param_description.html metodo=_dato parametro="T obj" %}
* **long update**,  {% include w3api/param_description.html metodo=_dato parametro="long update" %}

## Clase Padre
[AtomicLongFieldUpdater](/Java/AtomicLongFieldUpdater/)

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
