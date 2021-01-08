---
title: JMXConnectionNotification.JMXConnectionNotification()
permalink: Java/JMXConnectionNotification/JMXConnectionNotification
date: 2021-01-04
key: JavaJava.J.JMXConnectionNotification
category: java
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
* **String connectionId**,  {% include w3api/param_description.html metodo=_data parametro="String connectionId" %}
* **String type**,  {% include w3api/param_description.html metodo=_data parametro="String type" %}
* **String message**,  {% include w3api/param_description.html metodo=_data parametro="String message" %}
* **long sequenceNumber**,  {% include w3api/param_description.html metodo=_data parametro="long sequenceNumber" %}
* **Object userData**,  {% include w3api/param_description.html metodo=_data parametro="Object userData" %}
* **Object source**,  {% include w3api/param_description.html metodo=_data parametro="Object source" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[JMXConnectionNotification](/Java/JMXConnectionNotification/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.J.JMXConnectionNotification.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
