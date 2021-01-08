---
title: MBeanServerNotificationFilter.isNotificationEnabled()
permalink: Java/MBeanServerNotificationFilter/isNotificationEnabled
date: 2021-01-04
key: JavaJava.M.MBeanServerNotificationFilter
category: java
tags: ['java se', 'javax.management.relation', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MBeanServerNotificationFilter.metodos valor="isNotificationEnabled" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public boolean isNotificationEnabled(Notification notif) throws IllegalArgumentException
~~~

## Parámetros
* **Notification notif**,  {% include w3api/param_description.html metodo=_data parametro="Notification notif" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[MBeanServerNotificationFilter](/Java/MBeanServerNotificationFilter/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.MBeanServerNotificationFilter.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
