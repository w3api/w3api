---
title: ActionEvent.ActionEvent()
permalink: /Java/ActionEvent-java-awt-event/ActionEvent/
date: 2021-01-11
key: Java.A.ActionEvent-java-awt-event
category: Java
tags: ['java se', 'java.awt.event', 'java.desktop', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.ActionEvent-java-awt-event.constructores valor="ActionEvent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ActionEvent(Object source, int id, String command)
public ActionEvent(Object source, int id, String command, int modifiers)
public ActionEvent(Object source, int id, String command, long when, int modifiers)
~~~

## Parámetros
* **int modifiers**,  {% include w3api/param_description.html metodo=_dato parametro="int modifiers" %}
* **long when**,  {% include w3api/param_description.html metodo=_dato parametro="long when" %}
* **int id**,  {% include w3api/param_description.html metodo=_dato parametro="int id" %}
* **Object source**,  {% include w3api/param_description.html metodo=_dato parametro="Object source" %}
* **String command**,  {% include w3api/param_description.html metodo=_dato parametro="String command" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[ActionEvent](/Java/ActionEvent-java-awt-event/)

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
