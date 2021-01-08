---
title: WindowEvent.WindowEvent()
permalink: Java/WindowEvent-java-awt-event/WindowEvent
date: 2021-01-04
key: JavaJava.W.WindowEvent-java-awt-event
category: java
tags: ['java se', 'java.awt.event', 'java.desktop', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.W.WindowEvent-java-awt-event.constructores valor="WindowEvent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public WindowEvent(Window source, int id)
public WindowEvent(Window source, int id, int oldState, int newState)
public WindowEvent(Window source, int id, Window opposite)
public WindowEvent(Window source, int id, Window opposite, int oldState, int newState)
~~~

## Parámetros
* **int id**,  {% include w3api/param_description.html metodo=_data parametro="int id" %}
* **Window source**,  {% include w3api/param_description.html metodo=_data parametro="Window source" %}
* **int oldState**,  {% include w3api/param_description.html metodo=_data parametro="int oldState" %}
* **int newState**,  {% include w3api/param_description.html metodo=_data parametro="int newState" %}
* **Window opposite**,  {% include w3api/param_description.html metodo=_data parametro="Window opposite" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[WindowEvent](/Java/WindowEvent-java-awt-event/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.W.WindowEvent-java-awt-event.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
