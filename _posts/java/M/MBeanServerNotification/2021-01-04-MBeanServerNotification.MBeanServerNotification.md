---
title: MBeanServerNotification.MBeanServerNotification()
permalink: Java/MBeanServerNotification/MBeanServerNotification
date: 2021-01-04
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
* **ObjectName objectName**,  {% include w3api/param_description.html metodo=_data parametro="ObjectName objectName" %}
* **long sequenceNumber**,  {% include w3api/param_description.html metodo=_data parametro="long sequenceNumber" %}
* **Object source**,  {% include w3api/param_description.html metodo=_data parametro="Object source" %}
* **String type**,  {% include w3api/param_description.html metodo=_data parametro="String type" %}

## Clase Padre
[MBeanServerNotification](/Java/MBeanServerNotification/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.MBeanServerNotification.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
