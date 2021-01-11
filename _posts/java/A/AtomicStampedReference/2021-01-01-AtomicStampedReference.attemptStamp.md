---
title: AtomicStampedReference.attemptStamp()
permalink: Java/AtomicStampedReference/attemptStamp
date: 2021-01-11
key: JavaJava.A.AtomicStampedReference
category: java
tags: ['java se', 'java.util.concurrent.atomic', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AtomicStampedReference.metodos valor="attemptStamp" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public boolean attemptStamp(V expectedReference, int newStamp)
~~~

## Parámetros
* **int newStamp**,  {% include w3api/param_description.html metodo=_dato parametro="int newStamp" %}
* **V expectedReference**,  {% include w3api/param_description.html metodo=_dato parametro="V expectedReference" %}

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
