---
title: ModelMBeanNotificationBroadcaster.sendNotification()
permalink: Java/ModelMBeanNotificationBroadcaster/sendNotification
date: 2021-01-11
key: JavaJava.M.ModelMBeanNotificationBroadcaster
category: Java
tags: ['java se', 'javax.management.modelmbean', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.ModelMBeanNotificationBroadcaster.metodos valor="sendNotification" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void sendNotification(String ntfyText) throws MBeanException, RuntimeOperationsException
void sendNotification(Notification ntfyObj) throws MBeanException, RuntimeOperationsException
~~~

## Parámetros
* **Notification ntfyObj**,  {% include w3api/param_description.html metodo=_dato parametro="Notification ntfyObj" %}
* **String ntfyText**,  {% include w3api/param_description.html metodo=_dato parametro="String ntfyText" %}

## Excepciones
[MBeanException](/Java/MBeanException/), [RuntimeOperationsException](/Java/RuntimeOperationsException/)

## Clase Padre
[ModelMBeanNotificationBroadcaster](/Java/ModelMBeanNotificationBroadcaster/)

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
