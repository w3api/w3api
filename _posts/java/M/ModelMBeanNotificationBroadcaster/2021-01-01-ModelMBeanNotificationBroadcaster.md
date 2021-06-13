---
title: ModelMBeanNotificationBroadcaster
permalink: /Java/ModelMBeanNotificationBroadcaster/
date: 2021-01-11
key: Java.M.ModelMBeanNotificationBroadcaster
category: Java
tags: ['java se', 'javax.management.modelmbean', 'java.management', 'interface java', 'Java 1.5']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.M.ModelMBeanNotificationBroadcaster.description }}

## Sintaxis
~~~java
public interface ModelMBeanNotificationBroadcaster extends NotificationBroadcaster
~~~

## Métodos
* [addAttributeChangeNotificationListener()](/Java/ModelMBeanNotificationBroadcaster/addAttributeChangeNotificationListener)
* [removeAttributeChangeNotificationListener()](/Java/ModelMBeanNotificationBroadcaster/removeAttributeChangeNotificationListener)
* [sendAttributeChangeNotification()](/Java/ModelMBeanNotificationBroadcaster/sendAttributeChangeNotification)
* [sendNotification()](/Java/ModelMBeanNotificationBroadcaster/sendNotification)

## Ejemplo
~~~java
{{ site.data.Java.M.ModelMBeanNotificationBroadcaster.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.ModelMBeanNotificationBroadcaster.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
