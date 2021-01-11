---
title: ModelMBeanNotificationBroadcaster.addAttributeChangeNotificationListener()
permalink: Java/ModelMBeanNotificationBroadcaster/addAttributeChangeNotificationListener
date: 2021-01-11
key: JavaJava.M.ModelMBeanNotificationBroadcaster
category: java
tags: ['java se', 'javax.management.modelmbean', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.ModelMBeanNotificationBroadcaster.metodos valor="addAttributeChangeNotificationListener" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void addAttributeChangeNotificationListener(NotificationListener listener, String attributeName, Object handback) throws MBeanException, RuntimeOperationsException, IllegalArgumentException
~~~

## Parámetros
* **String attributeName**,  {% include w3api/param_description.html metodo=_dato parametro="String attributeName" %}
* **NotificationListener listener**,  {% include w3api/param_description.html metodo=_dato parametro="NotificationListener listener" %}
* **Object handback**,  {% include w3api/param_description.html metodo=_dato parametro="Object handback" %}

## Excepciones
[MBeanException](/Java/MBeanException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [RuntimeOperationsException](/Java/RuntimeOperationsException/)

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
