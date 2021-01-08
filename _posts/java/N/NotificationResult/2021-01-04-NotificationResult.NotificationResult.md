---
title: NotificationResult.NotificationResult()
permalink: Java/NotificationResult/NotificationResult
date: 2021-01-04
key: JavaJava.N.NotificationResult
category: java
tags: ['java se', 'javax.management.remote', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.N.NotificationResult.constructores valor="NotificationResult" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public NotificationResult(long earliestSequenceNumber, long nextSequenceNumber, TargetedNotification[] targetedNotifications)
~~~

## Parámetros
* **long nextSequenceNumber**,  {% include w3api/param_description.html metodo=_data parametro="long nextSequenceNumber" %}
* **long earliestSequenceNumber**,  {% include w3api/param_description.html metodo=_data parametro="long earliestSequenceNumber" %}
* **TargetedNotification[] targetedNotifications**,  {% include w3api/param_description.html metodo=_data parametro="TargetedNotification[] targetedNotifications" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[NotificationResult](/Java/NotificationResult/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.N.NotificationResult.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
