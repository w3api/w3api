---
title: Notification.Notification()
permalink: Java/Notification-javax-management/Notification
date: 2021-01-11
key: JavaJava.N.Notification-javax-management
category: Java
tags: ['java se', 'javax.management', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.N.Notification-javax-management.constructores valor="Notification" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Notification(String type, Object source, long sequenceNumber)
public Notification(String type, Object source, long sequenceNumber, long timeStamp)
public Notification(String type, Object source, long sequenceNumber, long timeStamp, String message)
public Notification(String type, Object source, long sequenceNumber, String message)
~~~

## Parámetros
* **Object source**,  {% include w3api/param_description.html metodo=_dato parametro="Object source" %}
* **String message**,  {% include w3api/param_description.html metodo=_dato parametro="String message" %}
* **String type**,  {% include w3api/param_description.html metodo=_dato parametro="String type" %}
* **long timeStamp**,  {% include w3api/param_description.html metodo=_dato parametro="long timeStamp" %}
* **long sequenceNumber**,  {% include w3api/param_description.html metodo=_dato parametro="long sequenceNumber" %}

## Clase Padre
[Notification](/Java/Notification-javax-management/)

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
