---
title: ModelMBeanNotificationBroadcaster.sendAttributeChangeNotification()
permalink: Java/ModelMBeanNotificationBroadcaster/sendAttributeChangeNotification
date: 2021-01-11
key: JavaJava.M.ModelMBeanNotificationBroadcaster
category: Java
tags: ['java se', 'javax.management.modelmbean', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.ModelMBeanNotificationBroadcaster.metodos valor="sendAttributeChangeNotification" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void sendAttributeChangeNotification(AttributeChangeNotification notification) throws MBeanException, RuntimeOperationsException
void sendAttributeChangeNotification(Attribute oldValue, Attribute newValue) throws MBeanException, RuntimeOperationsException
~~~

## Parámetros
* **Attribute oldValue**,  {% include w3api/param_description.html metodo=_dato parametro="Attribute oldValue" %}
* **Attribute newValue**,  {% include w3api/param_description.html metodo=_dato parametro="Attribute newValue" %}
* **AttributeChangeNotification notification**,  {% include w3api/param_description.html metodo=_dato parametro="AttributeChangeNotification notification" %}

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
