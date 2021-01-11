---
title: RMIConnection.fetchNotifications()
permalink: Java/RMIConnection/fetchNotifications
date: 2021-01-11
key: JavaJava.R.RMIConnection
category: java
tags: ['java se', 'javax.management.remote.rmi', 'java.management.rmi', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RMIConnection.metodos valor="fetchNotifications" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
NotificationResult fetchNotifications(long clientSequenceNumber, int maxNotifications, long timeout) throws IOException
~~~

## Parámetros
* **long clientSequenceNumber**,  {% include w3api/param_description.html metodo=_dato parametro="long clientSequenceNumber" %}
* **long timeout**,  {% include w3api/param_description.html metodo=_dato parametro="long timeout" %}
* **int maxNotifications**,  {% include w3api/param_description.html metodo=_dato parametro="int maxNotifications" %}

## Excepciones
[IOException](/Java/IOException/)

## Clase Padre
[RMIConnection](/Java/RMIConnection/)

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
