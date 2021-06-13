---
title: MBeanServerInvocationHandler.newProxyInstance()
permalink: Java/MBeanServerInvocationHandler/newProxyInstance
date: 2021-01-11
key: JavaJava.M.MBeanServerInvocationHandler
category: Java
tags: ['java se', 'javax.management', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MBeanServerInvocationHandler.metodos valor="newProxyInstance" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static <T> T newProxyInstance(MBeanServerConnection connection, ObjectName objectName, Class<T> interfaceClass, boolean notificationBroadcaster)
~~~

## Parámetros
* **MBeanServerConnection connection**,  {% include w3api/param_description.html metodo=_dato parametro="MBeanServerConnection connection" %}
* **Class&lt;T&gt; interfaceClass**,  {% include w3api/param_description.html metodo=_dato parametro="Class<T> interfaceClass" %}
* **ObjectName objectName**,  {% include w3api/param_description.html metodo=_dato parametro="ObjectName objectName" %}
* **boolean notificationBroadcaster**,  {% include w3api/param_description.html metodo=_dato parametro="boolean notificationBroadcaster" %}

## Clase Padre
[MBeanServerInvocationHandler](/Java/MBeanServerInvocationHandler/)

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
