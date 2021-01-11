---
title: AbstractNotificationHandler.handleNotification()
permalink: Java/AbstractNotificationHandler/handleNotification
date: 2021-01-11
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
* **Notification notification**,  {% include w3api/param_description.html metodo=_dato parametro="Notification notification" %}
* **T attachment**,  {% include w3api/param_description.html metodo=_dato parametro="T attachment" %}
* **AssociationChangeNotification notification**,  {% include w3api/param_description.html metodo=_dato parametro="AssociationChangeNotification notification" %}
* **PeerAddressChangeNotification notification**,  {% include w3api/param_description.html metodo=_dato parametro="PeerAddressChangeNotification notification" %}
* **ShutdownNotification notification**,  {% include w3api/param_description.html metodo=_dato parametro="ShutdownNotification notification" %}
* **SendFailedNotification notification**,  {% include w3api/param_description.html metodo=_dato parametro="SendFailedNotification notification" %}

## Clase Padre
[AbstractNotificationHandler](/Java/AbstractNotificationHandler/)

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
