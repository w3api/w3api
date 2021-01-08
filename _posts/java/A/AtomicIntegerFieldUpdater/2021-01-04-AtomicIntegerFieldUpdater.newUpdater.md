---
title: AtomicIntegerFieldUpdater.newUpdater()
permalink: Java/AtomicIntegerFieldUpdater/newUpdater
date: 2021-01-04
key: JavaJava.A.AtomicIntegerFieldUpdater
category: java
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
* **String fieldName**,  {% include w3api/param_description.html metodo=_data parametro="String fieldName" %}
* **Class&lt;U&gt; tclass**,  {% include w3api/param_description.html metodo=_data parametro="Class<U> tclass" %}

## Clase Padre
[AtomicIntegerFieldUpdater](/Java/AtomicIntegerFieldUpdater/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AtomicIntegerFieldUpdater.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
