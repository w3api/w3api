---
title: JMXConnector.removeConnectionNotificationListener()
permalink: Java/JMXConnector/removeConnectionNotificationListener
date: 2021-01-11
key: JavaJava.J.JMXConnector
category: java
tags: ['java se', 'javax.management.remote', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JMXConnector.metodos valor="removeConnectionNotificationListener" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void removeConnectionNotificationListener(NotificationListener listener) throws ListenerNotFoundException
void removeConnectionNotificationListener(NotificationListener l, NotificationFilter f, Object handback) throws ListenerNotFoundException
~~~

## Parámetros
* **NotificationListener listener**,  {% include w3api/param_description.html metodo=_dato parametro="NotificationListener listener" %}
* **NotificationFilter f**,  {% include w3api/param_description.html metodo=_dato parametro="NotificationFilter f" %}
* **Object handback**,  {% include w3api/param_description.html metodo=_dato parametro="Object handback" %}
* **NotificationListener l**,  {% include w3api/param_description.html metodo=_dato parametro="NotificationListener l" %}

## Excepciones
[ListenerNotFoundException](/Java/ListenerNotFoundException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[JMXConnector](/Java/JMXConnector/)

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
