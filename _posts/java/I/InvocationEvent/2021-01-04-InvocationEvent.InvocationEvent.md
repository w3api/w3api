---
title: InvocationEvent.InvocationEvent()
permalink: Java/InvocationEvent/InvocationEvent
date: 2021-01-04
key: JavaJava.I.InvocationEvent
category: java
tags: ['java se', 'java.awt.event', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.InvocationEvent.constructores valor="InvocationEvent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected InvocationEvent(Object source, int id, Runnable runnable, Object notifier, boolean catchThrowables)
public InvocationEvent(Object source, Runnable runnable)
public InvocationEvent(Object source, Runnable runnable, Object notifier, boolean catchThrowables)
public InvocationEvent(Object source, Runnable runnable, Runnable listener, boolean catchThrowables)
~~~

## Parámetros
* **int id**,  {% include w3api/param_description.html metodo=_data parametro="int id" %}
* **Object notifier**,  {% include w3api/param_description.html metodo=_data parametro="Object notifier" %}
* **Runnable runnable**,  {% include w3api/param_description.html metodo=_data parametro="Runnable runnable" %}
* **boolean catchThrowables**,  {% include w3api/param_description.html metodo=_data parametro="boolean catchThrowables" %}
* **Runnable listener**,  {% include w3api/param_description.html metodo=_data parametro="Runnable listener" %}
* **Object source**,  {% include w3api/param_description.html metodo=_data parametro="Object source" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[InvocationEvent](/Java/InvocationEvent/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.I.InvocationEvent.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
