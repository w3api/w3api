---
title: AtomicReferenceFieldUpdater.set()
permalink: Java/AtomicReferenceFieldUpdater/set
date: 2021-01-11
key: JavaJava.A.AtomicReferenceFieldUpdater
category: java
tags: ['java se', 'java.util.concurrent.atomic', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AtomicReferenceFieldUpdater.metodos valor="set" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract void set(T obj, V newValue)
~~~

## Parámetros
* **V newValue**,  {% include w3api/param_description.html metodo=_dato parametro="V newValue" %}
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
