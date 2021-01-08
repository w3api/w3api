---
title: AsynchronousChannelGroup.awaitTermination()
permalink: Java/AsynchronousChannelGroup/awaitTermination
date: 2021-01-04
key: JavaJava.A.AsynchronousChannelGroup
category: java
tags: ['java se', 'java.nio.channels', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AsynchronousChannelGroup.metodos valor="awaitTermination" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract boolean awaitTermination(long timeout, TimeUnit unit) throws InterruptedException
~~~

## Parámetros
* **long timeout**,  {% include w3api/param_description.html metodo=_data parametro="long timeout" %}
* **TimeUnit unit**,  {% include w3api/param_description.html metodo=_data parametro="TimeUnit unit" %}

## Excepciones
[InterruptedException](/Java/InterruptedException/)

## Clase Padre
[AsynchronousChannelGroup](/Java/AsynchronousChannelGroup/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AsynchronousChannelGroup.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
