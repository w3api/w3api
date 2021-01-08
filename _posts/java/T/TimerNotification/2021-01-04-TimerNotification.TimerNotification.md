---
title: TimerNotification.TimerNotification()
permalink: Java/TimerNotification/TimerNotification
date: 2021-01-04
key: JavaJava.T.TimerNotification
category: java
tags: ['java se', 'javax.management.timer', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TimerNotification.constructores valor="TimerNotification" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public TimerNotification(String type, Object source, long sequenceNumber, long timeStamp, String msg, Integer id)
~~~

## Parámetros
* **Integer id**,  {% include w3api/param_description.html metodo=_data parametro="Integer id" %}
* **String type**,  {% include w3api/param_description.html metodo=_data parametro="String type" %}
* **long timeStamp**,  {% include w3api/param_description.html metodo=_data parametro="long timeStamp" %}
* **long sequenceNumber**,  {% include w3api/param_description.html metodo=_data parametro="long sequenceNumber" %}
* **String msg**,  {% include w3api/param_description.html metodo=_data parametro="String msg" %}
* **Object source**,  {% include w3api/param_description.html metodo=_data parametro="Object source" %}

## Clase Padre
[TimerNotification](/Java/TimerNotification/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.T.TimerNotification.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
