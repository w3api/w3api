---
title: TimerNotification.TimerNotification()
permalink: /Java/TimerNotification/TimerNotification/
date: 2021-01-11
key: Java.T.TimerNotification
category: Java
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
* **Object source**,  {% include w3api/param_description.html metodo=_dato parametro="Object source" %}
* **String msg**,  {% include w3api/param_description.html metodo=_dato parametro="String msg" %}
* **String type**,  {% include w3api/param_description.html metodo=_dato parametro="String type" %}
* **long timeStamp**,  {% include w3api/param_description.html metodo=_dato parametro="long timeStamp" %}
* **long sequenceNumber**,  {% include w3api/param_description.html metodo=_dato parametro="long sequenceNumber" %}
* **Integer id**,  {% include w3api/param_description.html metodo=_dato parametro="Integer id" %}

## Clase Padre
[TimerNotification](/Java/TimerNotification/)

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
