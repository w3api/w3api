---
title: TimerMBean.addNotification()
permalink: Java/TimerMBean/addNotification
date: 2021-01-04
key: JavaJava.T.TimerMBean
category: java
tags: ['java se', 'javax.management.timer', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TimerMBean.metodos valor="addNotification" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Integer addNotification(String type, String message, Object userData, Date date) throws IllegalArgumentException
Integer addNotification(String type, String message, Object userData, Date date, long period) throws IllegalArgumentException
Integer addNotification(String type, String message, Object userData, Date date, long period, long nbOccurences) throws IllegalArgumentException
Integer addNotification(String type, String message, Object userData, Date date, long period, long nbOccurences, boolean fixedRate) throws IllegalArgumentException
~~~

## Parámetros
* **String type**,  {% include w3api/param_description.html metodo=_data parametro="String type" %}
* **String message**,  {% include w3api/param_description.html metodo=_data parametro="String message" %}
* **Object userData**,  {% include w3api/param_description.html metodo=_data parametro="Object userData" %}
* **long period**,  {% include w3api/param_description.html metodo=_data parametro="long period" %}
* **boolean fixedRate**,  {% include w3api/param_description.html metodo=_data parametro="boolean fixedRate" %}
* **long nbOccurences**,  {% include w3api/param_description.html metodo=_data parametro="long nbOccurences" %}
* **Date date**,  {% include w3api/param_description.html metodo=_data parametro="Date date" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[TimerMBean](/Java/TimerMBean/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.T.TimerMBean.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
