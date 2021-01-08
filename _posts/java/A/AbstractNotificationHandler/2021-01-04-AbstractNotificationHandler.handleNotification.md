---
title: AbstractNotificationHandler.handleNotification()
permalink: Java/AbstractNotificationHandler/handleNotification
date: 2021-01-04
key: JavaJava.A.AbstractNotificationHandler
category: java
tags: ['java se', 'com.sun.nio.sctp', 'jdk.sctp', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AbstractNotificationHandler.metodos valor="handleNotification" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public HandlerResult handleNotification(AssociationChangeNotification notification, T attachment)
public HandlerResult handleNotification(Notification notification, T attachment)
public HandlerResult handleNotification(PeerAddressChangeNotification notification, T attachment)
public HandlerResult handleNotification(SendFailedNotification notification, T attachment)
public HandlerResult handleNotification(ShutdownNotification notification, T attachment)
~~~

## Parámetros
* **SendFailedNotification notification**,  {% include w3api/param_description.html metodo=_data parametro="SendFailedNotification notification" %}
* **PeerAddressChangeNotification notification**,  {% include w3api/param_description.html metodo=_data parametro="PeerAddressChangeNotification notification" %}
* **T attachment**,  {% include w3api/param_description.html metodo=_data parametro="T attachment" %}
* **Notification notification**,  {% include w3api/param_description.html metodo=_data parametro="Notification notification" %}
* **ShutdownNotification notification**,  {% include w3api/param_description.html metodo=_data parametro="ShutdownNotification notification" %}
* **AssociationChangeNotification notification**,  {% include w3api/param_description.html metodo=_data parametro="AssociationChangeNotification notification" %}

## Clase Padre
[AbstractNotificationHandler](/Java/AbstractNotificationHandler/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AbstractNotificationHandler.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
