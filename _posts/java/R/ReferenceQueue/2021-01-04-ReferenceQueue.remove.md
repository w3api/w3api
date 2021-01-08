---
title: ReferenceQueue.remove()
permalink: Java/ReferenceQueue/remove
date: 2021-01-04
key: JavaJava.R.ReferenceQueue
category: java
tags: ['java se', 'java.lang.ref', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.ReferenceQueue.metodos valor="remove" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Reference<? extends T> remove() throws InterruptedException
public Reference<? extends T> remove(long timeout) throws IllegalArgumentException, InterruptedException
~~~

## Parámetros
* **long timeout**,  {% include w3api/param_description.html metodo=_data parametro="long timeout" %}

## Excepciones
[InterruptedException](/Java/InterruptedException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[ReferenceQueue](/Java/ReferenceQueue/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.R.ReferenceQueue.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
