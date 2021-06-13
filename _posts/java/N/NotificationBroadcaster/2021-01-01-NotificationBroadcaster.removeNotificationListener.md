---
title: NotificationBroadcaster.removeNotificationListener()
permalink: /Java/NotificationBroadcaster/removeNotificationListener/
date: 2021-01-11
key: Java.N.NotificationBroadcaster
category: Java
tags: ['java se', 'javax.management', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.N.NotificationBroadcaster.metodos valor="removeNotificationListener" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void removeNotificationListener(NotificationListener listener) throws ListenerNotFoundException
~~~

## Parámetros
* **NotificationListener listener**,  {% include w3api/param_description.html metodo=_dato parametro="NotificationListener listener" %}

## Excepciones
[ListenerNotFoundException](/Java/ListenerNotFoundException/)

## Clase Padre
[NotificationBroadcaster](/Java/NotificationBroadcaster/)

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
