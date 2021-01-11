---
title: AtomicLongFieldUpdater.newUpdater()
permalink: Java/AtomicLongFieldUpdater/newUpdater
date: 2021-01-11
key: JavaJava.A.AtomicLongFieldUpdater
category: java
tags: ['java se', 'java.util.concurrent.atomic', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AtomicLongFieldUpdater.metodos valor="newUpdater" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static <U> AtomicLongFieldUpdater<U> newUpdater(Class<U> tclass, String fieldName)
~~~

## Parámetros
* **Class&lt;U&gt; tclass**,  {% include w3api/param_description.html metodo=_dato parametro="Class<U> tclass" %}
* **String fieldName**,  {% include w3api/param_description.html metodo=_dato parametro="String fieldName" %}

## Clase Padre
[AtomicLongFieldUpdater](/Java/AtomicLongFieldUpdater/)

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
