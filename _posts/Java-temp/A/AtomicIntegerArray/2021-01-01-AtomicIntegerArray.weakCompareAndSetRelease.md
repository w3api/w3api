---
title: AtomicIntegerArray.weakCompareAndSetRelease()
permalink: /Java/AtomicIntegerArray/weakCompareAndSetRelease/
date: 2021-01-11
key: Java.A.AtomicIntegerArray
category: Java
tags: ['java se', 'java.util.concurrent.atomic', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AtomicIntegerArray.metodos valor="weakCompareAndSetRelease" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final boolean weakCompareAndSetRelease(int i, int expectedValue, int newValue)
~~~

## Parámetros
* **int newValue**,  {% include w3api/param_description.html metodo=_dato parametro="int newValue" %}
* **int i**,  {% include w3api/param_description.html metodo=_dato parametro="int i" %}
* **int expectedValue**,  {% include w3api/param_description.html metodo=_dato parametro="int expectedValue" %}

## Clase Padre
[AtomicIntegerArray](/Java/AtomicIntegerArray/)

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
