---
title: AtomicReferenceFieldUpdater.newUpdater()
permalink: /Java/AtomicReferenceFieldUpdater/newUpdater/
date: 2021-01-11
key: Java.A.AtomicReferenceFieldUpdater
category: Java
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
* **Class&lt;W&gt; vclass**,  {% include w3api/param_description.html metodo=_dato parametro="Class<W> vclass" %}
* **Class&lt;U&gt; tclass**,  {% include w3api/param_description.html metodo=_dato parametro="Class<U> tclass" %}
* **String fieldName**,  {% include w3api/param_description.html metodo=_dato parametro="String fieldName" %}

## Clase Padre
[AtomicReferenceFieldUpdater](/Java/AtomicReferenceFieldUpdater/)

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
