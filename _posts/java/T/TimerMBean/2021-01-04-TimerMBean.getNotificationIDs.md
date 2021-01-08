---
title: TimerMBean.getNotificationIDs()
permalink: Java/TimerMBean/getNotificationIDs
date: 2021-01-04
key: JavaJava.T.TimerMBean
category: java
tags: ['java se', 'javax.management.timer', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TimerMBean.metodos valor="getNotificationIDs" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Vector<Integer> getNotificationIDs(String type)
~~~

## Parámetros
* **String type**,  {% include w3api/param_description.html metodo=_data parametro="String type" %}

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
