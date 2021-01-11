---
title: MBeanServerConnection.removeNotificationListener()
permalink: Java/MBeanServerConnection/removeNotificationListener
date: 2021-01-11
key: JavaJava.M.MBeanServerConnection
category: java
tags: ['java se', 'javax.management', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MBeanServerConnection.metodos valor="removeNotificationListener" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void removeNotificationListener(ObjectName name, NotificationListener listener) throws InstanceNotFoundException, ListenerNotFoundException, IOException
void removeNotificationListener(ObjectName name, NotificationListener listener, NotificationFilter filter, Object handback) throws InstanceNotFoundException, ListenerNotFoundException, IOException
void removeNotificationListener(ObjectName name, ObjectName listener) throws InstanceNotFoundException, ListenerNotFoundException, IOException
void removeNotificationListener(ObjectName name, ObjectName listener, NotificationFilter filter, Object handback) throws InstanceNotFoundException, ListenerNotFoundException, IOException
~~~

## Parámetros
* **NotificationFilter filter**,  {% include w3api/param_description.html metodo=_dato parametro="NotificationFilter filter" %}
* **ObjectName listener**,  {% include w3api/param_description.html metodo=_dato parametro="ObjectName listener" %}
* **NotificationListener listener**,  {% include w3api/param_description.html metodo=_dato parametro="NotificationListener listener" %}
* **ObjectName name**,  {% include w3api/param_description.html metodo=_dato parametro="ObjectName name" %}
* **Object handback**,  {% include w3api/param_description.html metodo=_dato parametro="Object handback" %}

## Excepciones
[InstanceNotFoundException](/Java/InstanceNotFoundException/), [ListenerNotFoundException](/Java/ListenerNotFoundException/), [IOException](/Java/IOException/)

## Clase Padre
[MBeanServerConnection](/Java/MBeanServerConnection/)

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
