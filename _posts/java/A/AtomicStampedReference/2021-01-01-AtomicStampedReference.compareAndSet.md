---
title: AtomicStampedReference.compareAndSet()
permalink: /Java/AtomicStampedReference/compareAndSet/
date: 2021-01-11
key: Java.A.AtomicStampedReference
category: Java
tags: ['java se', 'java.util.concurrent.atomic', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AtomicStampedReference.metodos valor="compareAndSet" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public boolean compareAndSet(V expectedReference, V newReference, int expectedStamp, int newStamp)
~~~

## Parámetros
* **int newStamp**,  {% include w3api/param_description.html metodo=_dato parametro="int newStamp" %}
* **int expectedStamp**,  {% include w3api/param_description.html metodo=_dato parametro="int expectedStamp" %}
* **V expectedReference**,  {% include w3api/param_description.html metodo=_dato parametro="V expectedReference" %}
* **V newReference**,  {% include w3api/param_description.html metodo=_dato parametro="V newReference" %}

## Clase Padre
[AtomicStampedReference](/Java/AtomicStampedReference/)

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
