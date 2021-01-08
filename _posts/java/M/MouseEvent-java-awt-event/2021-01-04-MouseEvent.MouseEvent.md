---
title: MouseEvent.MouseEvent()
permalink: Java/MouseEvent-java-awt-event/MouseEvent
date: 2021-01-04
key: JavaJava.M.MouseEvent-java-awt-event
category: java
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
* **int xAbs**,  {% include w3api/param_description.html metodo=_data parametro="int xAbs" %}
* **int y**,  {% include w3api/param_description.html metodo=_data parametro="int y" %}
* **int id**,  {% include w3api/param_description.html metodo=_data parametro="int id" %}
* **int yAbs**,  {% include w3api/param_description.html metodo=_data parametro="int yAbs" %}
* **Component source**,  {% include w3api/param_description.html metodo=_data parametro="Component source" %}
* **int modifiers**,  {% include w3api/param_description.html metodo=_data parametro="int modifiers" %}
* **int button**,  {% include w3api/param_description.html metodo=_data parametro="int button" %}
* **long when**,  {% include w3api/param_description.html metodo=_data parametro="long when" %}
* **int clickCount**,  {% include w3api/param_description.html metodo=_data parametro="int clickCount" %}
* **boolean popupTrigger**,  {% include w3api/param_description.html metodo=_data parametro="boolean popupTrigger" %}
* **int x**,  {% include w3api/param_description.html metodo=_data parametro="int x" %}

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
{%- for _ldc in site.data.Java.M.MouseEvent-java-awt-event.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
