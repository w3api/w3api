---
title: ModelMBeanNotificationBroadcaster.removeAttributeChangeNotificationListener()
permalink: Java/ModelMBeanNotificationBroadcaster/removeAttributeChangeNotificationListener
date: 2021-01-11
key: JavaJava.M.ModelMBeanNotificationBroadcaster
category: Java
tags: ['java se', 'javax.management.modelmbean', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.ModelMBeanNotificationBroadcaster.metodos valor="removeAttributeChangeNotificationListener" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void removeAttributeChangeNotificationListener(NotificationListener listener, String attributeName) throws MBeanException, RuntimeOperationsException, ListenerNotFoundException
~~~

## Parámetros
* **String attributeName**,  {% include w3api/param_description.html metodo=_dato parametro="String attributeName" %}
* **NotificationListener listener**,  {% include w3api/param_description.html metodo=_dato parametro="NotificationListener listener" %}

## Excepciones
[MBeanException](/Java/MBeanException/), [ListenerNotFoundException](/Java/ListenerNotFoundException/), [RuntimeOperationsException](/Java/RuntimeOperationsException/)

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
