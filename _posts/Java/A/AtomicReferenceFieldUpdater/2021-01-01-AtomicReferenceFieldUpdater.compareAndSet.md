---
title: AtomicReferenceFieldUpdater.compareAndSet()
permalink: /Java/AtomicReferenceFieldUpdater/compareAndSet/
date: 2021-01-11
key: Java.A.AtomicReferenceFieldUpdater
category: Java
tags: ['java se', 'java.util.concurrent.atomic', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AtomicReferenceFieldUpdater.metodos valor="compareAndSet" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract boolean compareAndSet(T obj, V expect, V update)
~~~

## Parámetros
* **V update**,  {% include w3api/param_description.html metodo=_dato parametro="V update" %}
* **V expect**,  {% include w3api/param_description.html metodo=_dato parametro="V expect" %}
* **T obj**,  {% include w3api/param_description.html metodo=_dato parametro="T obj" %}

## Clase Padre
[AtomicReferenceFieldUpdater](/Java/AtomicReferenceFieldUpdater/)

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
