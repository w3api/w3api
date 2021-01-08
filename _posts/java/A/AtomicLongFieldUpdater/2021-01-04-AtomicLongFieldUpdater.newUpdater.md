---
title: AtomicLongFieldUpdater.newUpdater()
permalink: Java/AtomicLongFieldUpdater/newUpdater
date: 2021-01-04
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
* **String fieldName**,  {% include w3api/param_description.html metodo=_data parametro="String fieldName" %}
* **Class&lt;U&gt; tclass**,  {% include w3api/param_description.html metodo=_data parametro="Class<U> tclass" %}

## Clase Padre
[AtomicLongFieldUpdater](/Java/AtomicLongFieldUpdater/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AtomicLongFieldUpdater.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
