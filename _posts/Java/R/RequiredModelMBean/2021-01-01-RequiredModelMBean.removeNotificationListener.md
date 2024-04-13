---
title: RequiredModelMBean.removeNotificationListener()
permalink: /Java/RequiredModelMBean/removeNotificationListener/
date: 2021-01-11
key: Java.R.RequiredModelMBean
category: Java
tags: ['java se', 'javax.management.modelmbean', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RequiredModelMBean.metodos valor="removeNotificationListener" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void removeNotificationListener(NotificationListener listener) throws ListenerNotFoundException
~~~

## Parámetros
* **NotificationListener listener**,  {% include w3api/param_description.html metodo=_dato parametro="NotificationListener listener" %}

## Excepciones
[ListenerNotFoundException](/Java/ListenerNotFoundException/)

## Clase Padre
[RequiredModelMBean](/Java/RequiredModelMBean/)

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
