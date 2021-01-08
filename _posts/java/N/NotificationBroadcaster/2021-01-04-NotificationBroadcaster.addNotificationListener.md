---
title: NotificationBroadcaster.addNotificationListener()
permalink: Java/NotificationBroadcaster/addNotificationListener
date: 2021-01-04
key: JavaJava.N.NotificationBroadcaster
category: java
tags: ['java se', 'javax.management', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.N.NotificationBroadcaster.metodos valor="addNotificationListener" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void addNotificationListener(NotificationListener listener, NotificationFilter filter, Object handback) throws IllegalArgumentException
~~~

## Parámetros
* **Object handback**,  {% include w3api/param_description.html metodo=_data parametro="Object handback" %}
* **NotificationFilter filter**,  {% include w3api/param_description.html metodo=_data parametro="NotificationFilter filter" %}
* **NotificationListener listener**,  {% include w3api/param_description.html metodo=_data parametro="NotificationListener listener" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[NotificationBroadcaster](/Java/NotificationBroadcaster/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.N.NotificationBroadcaster.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
