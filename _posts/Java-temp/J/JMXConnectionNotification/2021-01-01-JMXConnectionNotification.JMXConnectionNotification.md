---
title: JMXConnectionNotification.JMXConnectionNotification()
permalink: /Java/JMXConnectionNotification/JMXConnectionNotification/
date: 2021-01-11
key: Java.J.JMXConnectionNotification
category: Java
tags: ['java se', 'javax.management.remote', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JMXConnectionNotification.constructores valor="JMXConnectionNotification" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public JMXConnectionNotification(String type, Object source, String connectionId, long sequenceNumber, String message, Object userData)
~~~

## Parámetros
* **Object source**,  {% include w3api/param_description.html metodo=_dato parametro="Object source" %}
* **String message**,  {% include w3api/param_description.html metodo=_dato parametro="String message" %}
* **Object userData**,  {% include w3api/param_description.html metodo=_dato parametro="Object userData" %}
* **String connectionId**,  {% include w3api/param_description.html metodo=_dato parametro="String connectionId" %}
* **String type**,  {% include w3api/param_description.html metodo=_dato parametro="String type" %}
* **long sequenceNumber**,  {% include w3api/param_description.html metodo=_dato parametro="long sequenceNumber" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[JMXConnectionNotification](/Java/JMXConnectionNotification/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
