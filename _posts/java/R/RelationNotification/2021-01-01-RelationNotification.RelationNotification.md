---
title: RelationNotification.RelationNotification()
permalink: Java/RelationNotification/RelationNotification
date: 2021-01-11
key: Java.R.RelationNotification
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
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}
* **List&lt;ObjectName&gt; oldValue**,  {% include w3api/param_description.html metodo=_dato parametro="List<ObjectName> oldValue" %}
* **String notifType**,  {% include w3api/param_description.html metodo=_dato parametro="String notifType" %}
* **long sequence**,  {% include w3api/param_description.html metodo=_dato parametro="long sequence" %}
* **Object sourceObj**,  {% include w3api/param_description.html metodo=_dato parametro="Object sourceObj" %}
* **String message**,  {% include w3api/param_description.html metodo=_dato parametro="String message" %}
* **ObjectName objectName**,  {% include w3api/param_description.html metodo=_dato parametro="ObjectName objectName" %}
* **List&lt;ObjectName&gt; newValue**,  {% include w3api/param_description.html metodo=_dato parametro="List<ObjectName> newValue" %}
* **List&lt;ObjectName&gt; unregMBeanList**,  {% include w3api/param_description.html metodo=_dato parametro="List<ObjectName> unregMBeanList" %}
* **String id**,  {% include w3api/param_description.html metodo=_dato parametro="String id" %}
* **long timeStamp**,  {% include w3api/param_description.html metodo=_dato parametro="long timeStamp" %}
* **String typeName**,  {% include w3api/param_description.html metodo=_dato parametro="String typeName" %}

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
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
