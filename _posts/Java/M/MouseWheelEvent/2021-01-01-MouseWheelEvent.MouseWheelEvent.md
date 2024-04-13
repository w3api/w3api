---
title: MouseWheelEvent.MouseWheelEvent()
permalink: /Java/MouseWheelEvent/MouseWheelEvent/
date: 2021-01-11
key: Java.M.MouseWheelEvent
category: Java
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
* **int modifiers**,  {% include w3api/param_description.html metodo=_dato parametro="int modifiers" %}
* **long when**,  {% include w3api/param_description.html metodo=_dato parametro="long when" %}
* **int id**,  {% include w3api/param_description.html metodo=_dato parametro="int id" %}
* **double preciseWheelRotation**,  {% include w3api/param_description.html metodo=_dato parametro="double preciseWheelRotation" %}
* **int y**,  {% include w3api/param_description.html metodo=_dato parametro="int y" %}
* **int clickCount**,  {% include w3api/param_description.html metodo=_dato parametro="int clickCount" %}
* **int scrollAmount**,  {% include w3api/param_description.html metodo=_dato parametro="int scrollAmount" %}
* **boolean popupTrigger**,  {% include w3api/param_description.html metodo=_dato parametro="boolean popupTrigger" %}
* **int xAbs**,  {% include w3api/param_description.html metodo=_dato parametro="int xAbs" %}
* **int x**,  {% include w3api/param_description.html metodo=_dato parametro="int x" %}
* **int scrollType**,  {% include w3api/param_description.html metodo=_dato parametro="int scrollType" %}
* **int yAbs**,  {% include w3api/param_description.html metodo=_dato parametro="int yAbs" %}
* **int wheelRotation**,  {% include w3api/param_description.html metodo=_dato parametro="int wheelRotation" %}
* **Component source**,  {% include w3api/param_description.html metodo=_dato parametro="Component source" %}

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
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
