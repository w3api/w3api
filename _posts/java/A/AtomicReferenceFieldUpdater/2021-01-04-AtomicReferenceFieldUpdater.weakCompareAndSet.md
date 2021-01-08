---
title: AtomicReferenceFieldUpdater.weakCompareAndSet()
permalink: Java/AtomicReferenceFieldUpdater/weakCompareAndSet
date: 2021-01-04
key: JavaJava.A.AtomicReferenceFieldUpdater
category: java
tags: ['java se', 'java.util.concurrent.atomic', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AtomicReferenceFieldUpdater.metodos valor="weakCompareAndSet" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract boolean weakCompareAndSet(T obj, V expect, V update)
~~~

## Parámetros
* **V expect**,  {% include w3api/param_description.html metodo=_data parametro="V expect" %}
* **V update**,  {% include w3api/param_description.html metodo=_data parametro="V update" %}
* **T obj**,  {% include w3api/param_description.html metodo=_data parametro="T obj" %}

## Clase Padre
[AtomicReferenceFieldUpdater](/Java/AtomicReferenceFieldUpdater/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AtomicReferenceFieldUpdater.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
