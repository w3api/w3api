---
title: MBeanServerNotification.MBeanServerNotification()
permalink: Java/MBeanServerNotification/MBeanServerNotification
date: 2021-01-11
key: JavaJava.M.MBeanServerNotification
category: java
tags: ['java se', 'javax.management', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MBeanServerNotification.constructores valor="MBeanServerNotification" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public MBeanServerNotification(String type, Object source, long sequenceNumber, ObjectName objectName)
~~~

## Parámetros
* **Object source**,  {% include w3api/param_description.html metodo=_dato parametro="Object source" %}
* **long sequenceNumber**,  {% include w3api/param_description.html metodo=_dato parametro="long sequenceNumber" %}
* **ObjectName objectName**,  {% include w3api/param_description.html metodo=_dato parametro="ObjectName objectName" %}
* **String type**,  {% include w3api/param_description.html metodo=_dato parametro="String type" %}

## Clase Padre
[MBeanServerNotification](/Java/MBeanServerNotification/)

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
