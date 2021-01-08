---
title: ModelMBeanNotificationBroadcaster.addAttributeChangeNotificationListener()
permalink: Java/ModelMBeanNotificationBroadcaster/addAttributeChangeNotificationListener
date: 2021-01-04
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
* **Object handback**,  {% include w3api/param_description.html metodo=_data parametro="Object handback" %}
* **String attributeName**,  {% include w3api/param_description.html metodo=_data parametro="String attributeName" %}
* **NotificationListener listener**,  {% include w3api/param_description.html metodo=_data parametro="NotificationListener listener" %}

## Excepciones
[RuntimeOperationsException](/Java/RuntimeOperationsException/), [MBeanException](/Java/MBeanException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[ModelMBeanNotificationBroadcaster](/Java/ModelMBeanNotificationBroadcaster/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.ModelMBeanNotificationBroadcaster.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
