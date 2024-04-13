---
title: NotificationEmitter.removeNotificationListener()
permalink: /Java/NotificationEmitter/removeNotificationListener/
date: 2021-01-11
key: Java.N.NotificationEmitter
category: Java
tags: ['java se', 'javax.management', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.N.NotificationEmitter.metodos valor="removeNotificationListener" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void removeNotificationListener(NotificationListener listener, NotificationFilter filter, Object handback) throws ListenerNotFoundException
~~~

## Parámetros
* **Object handback**,  {% include w3api/param_description.html metodo=_dato parametro="Object handback" %}
* **NotificationListener listener**,  {% include w3api/param_description.html metodo=_dato parametro="NotificationListener listener" %}
* **NotificationFilter filter**,  {% include w3api/param_description.html metodo=_dato parametro="NotificationFilter filter" %}

## Excepciones
[ListenerNotFoundException](/Java/ListenerNotFoundException/)

## Clase Padre
[NotificationEmitter](/Java/NotificationEmitter/)

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
