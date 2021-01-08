---
title: JMXConnector.addConnectionNotificationListener()
permalink: Java/JMXConnector/addConnectionNotificationListener
date: 2021-01-04
key: JavaJava.J.JMXConnector
category: java
tags: ['java se', 'javax.management.remote', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JMXConnector.metodos valor="addConnectionNotificationListener" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void addConnectionNotificationListener(NotificationListener listener, NotificationFilter filter, Object handback)
~~~

## Parámetros
* **Object handback**,  {% include w3api/param_description.html metodo=_data parametro="Object handback" %}
* **NotificationFilter filter**,  {% include w3api/param_description.html metodo=_data parametro="NotificationFilter filter" %}
* **NotificationListener listener**,  {% include w3api/param_description.html metodo=_data parametro="NotificationListener listener" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[JMXConnector](/Java/JMXConnector/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.J.JMXConnector.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
