---
title: RelationNotification.RelationNotification()
permalink: Java/RelationNotification/RelationNotification
date: 2021-01-04
key: JavaJava.R.RelationNotification
category: java
tags: ['java se', 'javax.management.relation', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RelationNotification.constructores valor="RelationNotification" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public RelationNotification(String notifType, Object sourceObj, long sequence, long timeStamp, String message, String id, String typeName, ObjectName objectName, String name, List<ObjectName> newValue, List<ObjectName> oldValue) throws IllegalArgumentException
public RelationNotification(String notifType, Object sourceObj, long sequence, long timeStamp, String message, String id, String typeName, ObjectName objectName, List<ObjectName> unregMBeanList) throws IllegalArgumentException
~~~

## Parámetros
* **String notifType**,  {% include w3api/param_description.html metodo=_data parametro="String notifType" %}
* **long timeStamp**,  {% include w3api/param_description.html metodo=_data parametro="long timeStamp" %}
* **String id**,  {% include w3api/param_description.html metodo=_data parametro="String id" %}
* **Object sourceObj**,  {% include w3api/param_description.html metodo=_data parametro="Object sourceObj" %}
* **String message**,  {% include w3api/param_description.html metodo=_data parametro="String message" %}
* **List&lt;ObjectName&gt; newValue**,  {% include w3api/param_description.html metodo=_data parametro="List<ObjectName> newValue" %}
* **String typeName**,  {% include w3api/param_description.html metodo=_data parametro="String typeName" %}
* **long sequence**,  {% include w3api/param_description.html metodo=_data parametro="long sequence" %}
* **List&lt;ObjectName&gt; unregMBeanList**,  {% include w3api/param_description.html metodo=_data parametro="List<ObjectName> unregMBeanList" %}
* **List&lt;ObjectName&gt; oldValue**,  {% include w3api/param_description.html metodo=_data parametro="List<ObjectName> oldValue" %}
* **ObjectName objectName**,  {% include w3api/param_description.html metodo=_data parametro="ObjectName objectName" %}
* **String name**,  {% include w3api/param_description.html metodo=_data parametro="String name" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[RelationNotification](/Java/RelationNotification/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.R.RelationNotification.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
