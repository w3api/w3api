---
title: EventQueue.invokeAndWait()
permalink: Java/EventQueue-java-awt/invokeAndWait
date: 2021-01-04
key: JavaJava.E.EventQueue-java-awt
category: java
tags: ['java se', 'java.awt', 'java.desktop', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.E.EventQueue-java-awt.metodos valor="invokeAndWait" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static void invokeAndWait(Runnable runnable) throws InterruptedException, InvocationTargetException
~~~

## Parámetros
* **Runnable runnable**,  {% include w3api/param_description.html metodo=_data parametro="Runnable runnable" %}

## Excepciones
[InterruptedException](/Java/InterruptedException/), [InvocationTargetException](/Java/InvocationTargetException/)

## Clase Padre
[EventQueue](/Java/EventQueue-java-awt/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.E.EventQueue-java-awt.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
