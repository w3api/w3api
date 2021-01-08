---
title: AtomicReferenceFieldUpdater.newUpdater()
permalink: Java/AtomicReferenceFieldUpdater/newUpdater
date: 2021-01-04
key: JavaJava.A.AtomicReferenceFieldUpdater
category: java
tags: ['java se', 'java.util.concurrent.atomic', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AtomicReferenceFieldUpdater.metodos valor="newUpdater" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static <U,W> AtomicReferenceFieldUpdater<U,W> newUpdater(Class<U> tclass, Class<W> vclass, String fieldName)
~~~

## Parámetros
* **Class&lt;W&gt; vclass**,  {% include w3api/param_description.html metodo=_data parametro="Class<W> vclass" %}
* **String fieldName**,  {% include w3api/param_description.html metodo=_data parametro="String fieldName" %}
* **Class&lt;U&gt; tclass**,  {% include w3api/param_description.html metodo=_data parametro="Class<U> tclass" %}

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
