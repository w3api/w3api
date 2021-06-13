---
title: AtomicStampedReference.set()
permalink: /Java/AtomicStampedReference/set/
date: 2021-01-11
key: Java.A.AtomicStampedReference
category: Java
tags: ['java se', 'java.util.concurrent.atomic', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AtomicStampedReference.metodos valor="set" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void set(V newReference, int newStamp)
~~~

## Parámetros
* **int newStamp**,  {% include w3api/param_description.html metodo=_dato parametro="int newStamp" %}
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
