---
title: AtomicStampedReference.get()
permalink: /Java/AtomicStampedReference/get/
date: 2021-01-11
key: Java.A.AtomicStampedReference
category: Java
tags: ['java se', 'java.util.concurrent.atomic', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AtomicStampedReference.metodos valor="get" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public V get(int[] stampHolder)
~~~

## Parámetros
* **int[] stampHolder**,  {% include w3api/param_description.html metodo=_dato parametro="int[] stampHolder" %}

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
