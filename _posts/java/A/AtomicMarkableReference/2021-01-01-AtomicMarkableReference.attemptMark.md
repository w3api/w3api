---
title: AtomicMarkableReference.attemptMark()
permalink: /Java/AtomicMarkableReference/attemptMark/
date: 2021-01-11
key: Java.A.AtomicMarkableReference
category: Java
tags: ['java se', 'java.util.concurrent.atomic', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AtomicMarkableReference.metodos valor="attemptMark" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public boolean attemptMark(V expectedReference, boolean newMark)
~~~

## Parámetros
* **boolean newMark**,  {% include w3api/param_description.html metodo=_dato parametro="boolean newMark" %}
* **V expectedReference**,  {% include w3api/param_description.html metodo=_dato parametro="V expectedReference" %}

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
