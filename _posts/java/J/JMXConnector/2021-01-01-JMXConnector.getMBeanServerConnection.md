---
title: JMXConnector.getMBeanServerConnection()
permalink: Java/JMXConnector/getMBeanServerConnection
date: 2021-01-11
key: JavaJava.J.JMXConnector
category: java
tags: ['java se', 'javax.management.remote', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JMXConnector.metodos valor="getMBeanServerConnection" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
MBeanServerConnection getMBeanServerConnection() throws IOException
MBeanServerConnection getMBeanServerConnection(Subject delegationSubject) throws IOException
~~~

## Parámetros
* **Subject delegationSubject**,  {% include w3api/param_description.html metodo=_dato parametro="Subject delegationSubject" %}

## Excepciones
[IOException](/Java/IOException/)

## Clase Padre
[JMXConnector](/Java/JMXConnector/)

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
