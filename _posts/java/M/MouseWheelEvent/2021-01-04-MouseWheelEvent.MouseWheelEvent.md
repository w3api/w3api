---
title: MouseWheelEvent.MouseWheelEvent()
permalink: Java/MouseWheelEvent/MouseWheelEvent
date: 2021-01-04
key: JavaJava.M.MouseWheelEvent
category: java
tags: ['java se', 'java.awt.event', 'java.desktop', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MouseWheelEvent.constructores valor="MouseWheelEvent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public MouseWheelEvent(Component source, int id, long when, int modifiers, int x, int y, int clickCount, boolean popupTrigger, int scrollType, int scrollAmount, int wheelRotation)
public MouseWheelEvent(Component source, int id, long when, int modifiers, int x, int y, int xAbs, int yAbs, int clickCount, boolean popupTrigger, int scrollType, int scrollAmount, int wheelRotation)
public MouseWheelEvent(Component source, int id, long when, int modifiers, int x, int y, int xAbs, int yAbs, int clickCount, boolean popupTrigger, int scrollType, int scrollAmount, int wheelRotation, double preciseWheelRotation)
~~~

## Parámetros
* **int xAbs**,  {% include w3api/param_description.html metodo=_data parametro="int xAbs" %}
* **int y**,  {% include w3api/param_description.html metodo=_data parametro="int y" %}
* **int id**,  {% include w3api/param_description.html metodo=_data parametro="int id" %}
* **int wheelRotation**,  {% include w3api/param_description.html metodo=_data parametro="int wheelRotation" %}
* **int yAbs**,  {% include w3api/param_description.html metodo=_data parametro="int yAbs" %}
* **double preciseWheelRotation**,  {% include w3api/param_description.html metodo=_data parametro="double preciseWheelRotation" %}
* **int scrollAmount**,  {% include w3api/param_description.html metodo=_data parametro="int scrollAmount" %}
* **Component source**,  {% include w3api/param_description.html metodo=_data parametro="Component source" %}
* **int modifiers**,  {% include w3api/param_description.html metodo=_data parametro="int modifiers" %}
* **long when**,  {% include w3api/param_description.html metodo=_data parametro="long when" %}
* **int clickCount**,  {% include w3api/param_description.html metodo=_data parametro="int clickCount" %}
* **int scrollType**,  {% include w3api/param_description.html metodo=_data parametro="int scrollType" %}
* **boolean popupTrigger**,  {% include w3api/param_description.html metodo=_data parametro="boolean popupTrigger" %}
* **int x**,  {% include w3api/param_description.html metodo=_data parametro="int x" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[MouseWheelEvent](/Java/MouseWheelEvent/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.MouseWheelEvent.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
