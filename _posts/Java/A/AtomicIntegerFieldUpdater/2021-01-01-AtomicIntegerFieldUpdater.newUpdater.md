---
title: AtomicIntegerFieldUpdater.newUpdater()
permalink: /Java/AtomicIntegerFieldUpdater/newUpdater/
date: 2021-01-11
key: Java.A.AtomicIntegerFieldUpdater
category: Java
tags: ['java se', 'java.util.concurrent.atomic', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AtomicIntegerFieldUpdater.metodos valor="newUpdater" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static <U> AtomicIntegerFieldUpdater<U> newUpdater(Class<U> tclass, String fieldName)
~~~

## Parámetros
* **Class&lt;U&gt; tclass**,  {% include w3api/param_description.html metodo=_dato parametro="Class<U> tclass" %}
* **String fieldName**,  {% include w3api/param_description.html metodo=_dato parametro="String fieldName" %}

## Clase Padre
[AtomicIntegerFieldUpdater](/Java/AtomicIntegerFieldUpdater/)

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
