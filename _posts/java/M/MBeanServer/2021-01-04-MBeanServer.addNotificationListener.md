---
title: MBeanServer.addNotificationListener()
permalink: Java/MBeanServer/addNotificationListener
date: 2021-01-04
key: JavaJava.M.MBeanServer
category: java
tags: ['java se', 'javax.management', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MBeanServer.metodos valor="addNotificationListener" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void addNotificationListener(ObjectName name, NotificationListener listener, NotificationFilter filter, Object handback) throws InstanceNotFoundException
void addNotificationListener(ObjectName name, ObjectName listener, NotificationFilter filter, Object handback) throws InstanceNotFoundException
~~~

## Parámetros
* **ObjectName listener**,  {% include w3api/param_description.html metodo=_data parametro="ObjectName listener" %}
* **NotificationListener listener**,  {% include w3api/param_description.html metodo=_data parametro="NotificationListener listener" %}
* **Object handback**,  {% include w3api/param_description.html metodo=_data parametro="Object handback" %}
* **ObjectName name**,  {% include w3api/param_description.html metodo=_data parametro="ObjectName name" %}
* **NotificationFilter filter**,  {% include w3api/param_description.html metodo=_data parametro="NotificationFilter filter" %}

## Excepciones
[InstanceNotFoundException](/Java/InstanceNotFoundException/), [RuntimeOperationsException](/Java/RuntimeOperationsException/)

## Clase Padre
[MBeanServer](/Java/MBeanServer/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.MBeanServer.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
