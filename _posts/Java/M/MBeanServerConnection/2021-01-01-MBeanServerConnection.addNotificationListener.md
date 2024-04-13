---
title: MBeanServerConnection.addNotificationListener()
permalink: /Java/MBeanServerConnection/addNotificationListener/
date: 2021-01-11
key: Java.M.MBeanServerConnection
category: Java
tags: ['java se', 'javax.management', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MBeanServerConnection.metodos valor="addNotificationListener" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void addNotificationListener(ObjectName name, NotificationListener listener, NotificationFilter filter, Object handback) throws InstanceNotFoundException, IOException
void addNotificationListener(ObjectName name, ObjectName listener, NotificationFilter filter, Object handback) throws InstanceNotFoundException, IOException
~~~

## Parámetros
* **NotificationFilter filter**,  {% include w3api/param_description.html metodo=_dato parametro="NotificationFilter filter" %}
* **ObjectName listener**,  {% include w3api/param_description.html metodo=_dato parametro="ObjectName listener" %}
* **NotificationListener listener**,  {% include w3api/param_description.html metodo=_dato parametro="NotificationListener listener" %}
* **ObjectName name**,  {% include w3api/param_description.html metodo=_dato parametro="ObjectName name" %}
* **Object handback**,  {% include w3api/param_description.html metodo=_dato parametro="Object handback" %}

## Excepciones
[InstanceNotFoundException](/Java/InstanceNotFoundException/), [RuntimeOperationsException](/Java/RuntimeOperationsException/), [IOException](/Java/IOException/)

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
