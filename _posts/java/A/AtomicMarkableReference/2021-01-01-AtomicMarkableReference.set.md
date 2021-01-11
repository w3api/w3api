---
title: AtomicMarkableReference.set()
permalink: Java/AtomicMarkableReference/set
date: 2021-01-11
key: JavaJava.A.AtomicMarkableReference
category: java
tags: ['java se', 'java.util.concurrent.atomic', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AtomicMarkableReference.metodos valor="set" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void set(V newReference, boolean newMark)
~~~

## Parámetros
* **boolean newMark**,  {% include w3api/param_description.html metodo=_dato parametro="boolean newMark" %}
* **V newReference**,  {% include w3api/param_description.html metodo=_dato parametro="V newReference" %}

## Clase Padre
[AtomicMarkableReference](/Java/AtomicMarkableReference/)

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
