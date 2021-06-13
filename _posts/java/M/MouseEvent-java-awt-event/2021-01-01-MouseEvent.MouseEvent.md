---
title: MouseEvent.MouseEvent()
permalink: /Java/MouseEvent-java-awt-event/MouseEvent/
date: 2021-01-11
key: Java.M.MouseEvent-java-awt-event
category: Java
tags: ['java se', 'java.awt.event', 'java.desktop', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MouseEvent-java-awt-event.constructores valor="MouseEvent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public MouseEvent(Component source, int id, long when, int modifiers, int x, int y, int clickCount, boolean popupTrigger)
public MouseEvent(Component source, int id, long when, int modifiers, int x, int y, int clickCount, boolean popupTrigger, int button)
public MouseEvent(Component source, int id, long when, int modifiers, int x, int y, int xAbs, int yAbs, int clickCount, boolean popupTrigger, int button)
~~~

## Parámetros
* **int modifiers**,  {% include w3api/param_description.html metodo=_dato parametro="int modifiers" %}
* **long when**,  {% include w3api/param_description.html metodo=_dato parametro="long when" %}
* **int id**,  {% include w3api/param_description.html metodo=_dato parametro="int id" %}
* **int y**,  {% include w3api/param_description.html metodo=_dato parametro="int y" %}
* **int clickCount**,  {% include w3api/param_description.html metodo=_dato parametro="int clickCount" %}
* **int button**,  {% include w3api/param_description.html metodo=_dato parametro="int button" %}
* **boolean popupTrigger**,  {% include w3api/param_description.html metodo=_dato parametro="boolean popupTrigger" %}
* **int xAbs**,  {% include w3api/param_description.html metodo=_dato parametro="int xAbs" %}
* **int x**,  {% include w3api/param_description.html metodo=_dato parametro="int x" %}
* **int yAbs**,  {% include w3api/param_description.html metodo=_dato parametro="int yAbs" %}
* **Component source**,  {% include w3api/param_description.html metodo=_dato parametro="Component source" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[MouseEvent](/Java/MouseEvent-java-awt-event/)

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
