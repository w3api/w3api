---
title: NotificationBroadcasterSupport.handleNotification()
permalink: Java/NotificationBroadcasterSupport/handleNotification
date: 2021-01-04
key: JavaJava.N.NotificationBroadcasterSupport
category: java
tags: ['java se', 'javax.management', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.N.NotificationBroadcasterSupport.metodos valor="handleNotification" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected void handleNotification(NotificationListener listener, Notification notif, Object handback)
~~~

## Parámetros
* **Object handback**,  {% include w3api/param_description.html metodo=_data parametro="Object handback" %}
* **Notification notif**,  {% include w3api/param_description.html metodo=_data parametro="Notification notif" %}
* **NotificationListener listener**,  {% include w3api/param_description.html metodo=_data parametro="NotificationListener listener" %}

## Clase Padre
[NotificationBroadcasterSupport](/Java/NotificationBroadcasterSupport/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.N.NotificationBroadcasterSupport.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
