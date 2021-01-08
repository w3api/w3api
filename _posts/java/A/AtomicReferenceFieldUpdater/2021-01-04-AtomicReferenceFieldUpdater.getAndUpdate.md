---
title: AtomicReferenceFieldUpdater.getAndUpdate()
permalink: Java/AtomicReferenceFieldUpdater/getAndUpdate
date: 2021-01-04
key: JavaJava.A.AtomicReferenceFieldUpdater
category: java
tags: ['java se', 'java.util.concurrent.atomic', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AtomicReferenceFieldUpdater.metodos valor="getAndUpdate" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final V getAndUpdate(T obj, UnaryOperator<V> updateFunction)
~~~

## Parámetros
* **UnaryOperator&lt;V&gt; updateFunction**,  {% include w3api/param_description.html metodo=_data parametro="UnaryOperator<V> updateFunction" %}
* **T obj**,  {% include w3api/param_description.html metodo=_data parametro="T obj" %}

## Clase Padre
[AtomicReferenceFieldUpdater](/Java/AtomicReferenceFieldUpdater/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AtomicReferenceFieldUpdater.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
