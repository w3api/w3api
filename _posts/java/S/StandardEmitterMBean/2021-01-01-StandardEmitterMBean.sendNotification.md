---
title: StandardEmitterMBean.sendNotification()
permalink: Java/StandardEmitterMBean/sendNotification
date: 2021-01-11
key: JavaJava.S.StandardEmitterMBean
category: java
tags: ['java se', 'javax.management', 'java.management', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StandardEmitterMBean.metodos valor="sendNotification" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void sendNotification(Notification n)
~~~

## Parámetros
* **Notification n**,  {% include w3api/param_description.html metodo=_dato parametro="Notification n" %}

## Excepciones
[ClassCastException](/Java/ClassCastException/)

## Clase Padre
[StandardEmitterMBean](/Java/StandardEmitterMBean/)

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
